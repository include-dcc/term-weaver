import argparse
import csv
import io
import logging
import re
import subprocess
import sys
from pathlib import Path

import yaml
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install

from tweaver.__init__ import __version__

logger = logging.getLogger(__name__)
# Rich Logging if rich is installed
if sys.stderr.isatty():
    from rich.console import Console
    from rich.logging import RichHandler
    from rich.traceback import install


def init_logging(loglevel: str | None = None):
    # When we are in the terminal, let's use the rich logging
    if loglevel is None:
        loglevel = "WARN"
    DATEFMT = "%Y-%m-%dT%H:%M:%SZ"
    if sys.stderr.isatty():
        install(show_locals=True)

        handler = RichHandler(
            level=loglevel,
            console=Console(stderr=True),
            show_time=False,
            show_level=True,
            markup=True,
            rich_tracebacks=True,
        )
        FORMAT = "%(message)s"
    else:
        FORMAT = "%(asctime)s\t%(levelname)s\t%(message)s"
        handler = logging.StreamHandler()

    logging.basicConfig(
        level=loglevel, format=FORMAT, datefmt=DATEFMT, handlers=[handler]
    )


prefix_dict = {"SNOMED": "snomedct", "SNOMEDCT": "snomedct", "SNOMEDCT_US": "snomedct"}


def parsed_csv(csv_text: str, endpoint: str, source_nodes: list) -> dict:
    """Parse dragon_search CSV output into permissible_values object for enum yaml file."""
    reader = csv.DictReader(io.StringIO(csv_text))
    permissible_values = {}
    argument = "children" if endpoint == "-c" else "descendants"
    for row in reader:
        code = row["descendant_code"]
        for key, value in prefix_dict.items():
            code = code.replace(key, value)
        if code.lower() == "no results":
            print(f"No {argument} found for {row['parent_code']}")
            continue
        for node in source_nodes:
            if code.split(":")[0].upper() == node.split(":")[0].upper():
                code = code.replace(code.split(":")[0], node.split(":")[0])
        permissible_values[code] = {
            "title": row.get("display", ""),
            "description": row.get("description"),
            "meaning": code,
        }
        if not permissible_values[code]["description"]:
            del permissible_values[code]["description"]
    return permissible_values


class IndentedDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow=flow, indentless=False)


def expand(
    local_filepath: Path,
    iri: str | None = None,
):
    """Extract Enums from a monolithic LinkML model into individual YAML files
    Args:
        local_filepath: The file containing the monolithic linkml model
        iri: Optional iri if a specific iri is desired other than the iri derived programattically
    Returns:
        list of enum names
    """

    model_filename = local_filepath.parent.name + ".yaml"
    model_file = local_filepath / model_filename

    enum_count = 0
    expanded_count = 0
    enum_names = []

    if not model_file.exists():
        logger.error(f"{model_file} not found.")
        return enum_names

    model_parsed = yaml.safe_load(model_file.read_text())
    imports = model_parsed.get("imports", [])

    for imp in imports:
        if not imp.split("/")[-1].startswith("Enum"):
            continue
        filename = imp.split("/")[-1]
        matches = list(local_filepath.resolve().glob(f"**/{filename}.yaml"))
        if not matches:
            logger.warning(f"{imp} file not found.")
            continue
        enum_file = matches[0]
        if not enum_file.exists():
            logger.warning(f"{enum_file} not found.")
            continue
        raw_enum = enum_file.read_text()
        parsed = yaml.safe_load(raw_enum)

        enums = parsed.get("enums", {})
        for name, enum in enums.items():
            enum_names.append(name)
            expanded_enum = enum_file

            has_permissible = (
                "permissible_values" in (enum) and enum["permissible_values"]
            )

            has_reachable = enum.get("reachable_from") or {}
            has_ontology = has_reachable.get("source_ontology")
            has_nodes = has_reachable.get("source_nodes")
            has_direct = has_reachable.get("is_direct")

            endpoint = "-c" if has_direct else "-d"

            if has_permissible or not has_ontology:
                logger.info(f"Skipping {name}. Does not require expansion")
                enum_count += 1
                expanded_count += 1
                continue

            if not has_ontology:
                continue
            ontology = has_ontology.split(":")[1]
            if not has_nodes:
                continue

            all_permissible_values = {}
            node_failed = False
            minus = has_reachable.get("minus", [])
            minus_codes = set()
            if isinstance(minus, dict):
                minus_codes.update(minus.get("permissible_values", []))
            else:
                for minus_item in minus:
                    if isinstance(minus_item, str):
                        minus_codes.add(minus_item)
                        continue
                    if "permissible_values" in minus_item:
                        minus_codes.update(minus_item["permissible_values"])
                        continue
                    minus_reachable = minus_item.get("reachable_from", {})
                    minus_nodes = minus_reachable.get("source_nodes", [])
                    minus_codes.update(minus_nodes)

            for node in has_nodes:
                cmd = [
                    "dragon_search",
                    "-ak",
                    str(node),
                    "-o",
                    str(ontology),
                    "-f",
                    str(expanded_enum),
                    str(endpoint),
                    "-s",
                    "0",
                ]
                if has_reachable.get("include_self"):
                    cmd.append("-p")
                if iri:
                    cmd.extend(["-i", str(iri)])

                result = subprocess.run(
                    cmd, capture_output=True, text=True, check=False
                )
                enum_count += 1
                if result.returncode != 0:
                    logger.error(f"Failed for {name}: {result.stdout}")
                    logger.error(f"Failed for {name}: {result.stderr}")
                    node_failed = True
                    logger.info(f"dragon_search exit code: {result.returncode}")
                else:
                    parsed_nodes = parsed_csv(
                        expanded_enum.read_text(), endpoint, has_nodes
                    )
                    all_permissible_values.update(parsed_nodes)
                    all_permissible_values = {
                        k: v
                        for k, v in all_permissible_values.items()
                        if k not in minus_codes
                    }
                    logger.info(f"Expanded enumeration: {name}")
                    if minus_codes:
                        logger.info(f"Excluding {minus_codes}")

                if all_permissible_values:
                    parsed["enums"][name]["permissible_values"] = all_permissible_values
                    expanded_enum.write_text(
                        yaml.dump(
                            parsed,
                            Dumper=IndentedDumper,
                            default_flow_style=False,
                            sort_keys=False,
                            allow_unicode=True,
                            explicit_start=True,
                        )
                    )
                    if not node_failed:
                        expanded_count += 1

    if expanded_count != enum_count:
        logger.warning(f"{enum_count - expanded_count} failed to be expanded.")
    return enum_names


def restricted_chars(arg: str):
    allowed_chars = re.search(r"^[\w-]+$", arg)
    if not allowed_chars:
        parser.error(
            f"Invalid input '{arg}'. Model names can only contain alphanumeric characters, underscores, and dashes. See LinkML docs for more details: https://linkml.io/linkml/schemas/models.html#model-level-metadata-and-directives"
        )
    return arg


def clear_permissible_values(filepath: Path):
    """Remove the permissible_values block from an enum YAML file."""
    parsed = yaml.safe_load(filepath.read_text())
    enums = parsed.get("enums", {})
    for name in enums:
        if "permissible_values" in enums[name]:
            del enums[name]["permissible_values"]
    filepath.write_text(
        yaml.dump(
            parsed,
            Dumper=IndentedDumper,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            explicit_start=True,
        )
    )
    logger.info(f"Cleared permissible_values from {filepath}")


parser = argparse.ArgumentParser(
    description="Expand enums from a monolithic LinkML model"
)


def exec(cli_args: list[str] | None = None):

    parser.add_argument(
        "-log",
        "--log-level",
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Logging level tolerated (default is INFO)",
    )
    parser.add_argument(
        "-s",
        "--source",
        required=False,
        type=Path,
        help="The source file containing the enumerations to be expanded",
    )

    parser.add_argument(
        "-i",
        "--iri",
        required=False,
        default=None,
        help="Optional iri for the parent code to pull descendants.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{__version__}",
        help="Pulls the version from the __init__.py file",
    )
    parser.add_argument(
        "--clear",
        required=False,
        type=Path,
        help="Clears permissible_values property from a speficied enum YAML file.",
    )

    args = parser.parse_args(cli_args)
    # Initialize the logger with whatever the user requested
    init_logging(args.log_level)

    if args.clear:
        clear_permissible_values(args.clear)
        return

    if not args.source:
        parser.error("-s/--source is required when not using --clear")
    expand(
        local_filepath=args.source,
        iri=args.iri,
    )
    logger.info("Script completed successfully")
    return args
