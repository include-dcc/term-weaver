import argparse
import csv
import io
import logging
import subprocess
import sys
from pathlib import Path

import yaml

from tweaver.__init__ import __version__

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


def parsed_csv(csv_text: str, endpoint: str) -> dict:
    """Parse dragon_search CSV output into permissible_values object for enum yaml file."""
    reader = csv.DictReader(io.StringIO(csv_text))
    permissible_values = {}
    argument = "children" if endpoint == "-c" else "descendants"
    for row in reader:
        code = row["descendant_code"]
        if code.lower() == "no results":
            print(f"No {argument} found for {row['parent_code']}")
            continue
        permissible_values[code] = {
            "text": code,
            "description": row.get("description", ""),
            "title": row.get("display", ""),
        }
    return permissible_values


class IndentedDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow=flow, indentless=False)


def expand(
    local_filepath: Path | None = None,
    output_filepath: Path | None = None,
    iri: str | None = None,
):
    """Extract Enums from a monolithic LinkML model into individual YAML files
    Args:
        local_filepath: The file containing the monolithic linkml model
        output_filepath: The directory where the enum YAMLs are to be written
        iri: Optional iri if a specific iri is desired other than the iri derived programattically
    Returns:
        list of enum names
    """
    if output_filepath is None:
        output_filepath = Path("output")

    output_filepath.mkdir(parents=True, exist_ok=True)
    enum_count = 0
    expanded_count = 0
    enum_names = []
    for enum_file in local_filepath.glob("Enum*.yaml"):
        raw_enum = enum_file.read_text()
        parsed = yaml.safe_load(raw_enum)

        enums = parsed.get("enums", {})
        for name, enum in enums.items():
            enum_names.append(name)
            expanded_enum = output_filepath / f"{name}.yaml"

            has_permissible = (
                "permissible_values" in (enum) and enum["permissible_values"]
            )

            has_reachable = enum.get("reachable_from") or {}
            has_ontology = has_reachable.get("source_ontology")
            has_nodes = has_reachable.get("source_nodes")
            has_direct = has_reachable.get("is_direct")

            endpoint = "-c" if has_direct else "-d"

            if has_permissible or not has_ontology:
                expanded_enum.write_text(raw_enum)
                logging.info(f"Copied {name} (does not require expansion)")
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
                    cmd,
                    capture_output=True,
                    text=True,
                )
                enum_count += 1
                if result.returncode != 0:
                    logging.error(f"Failed for {name}: {result.stdout}")
                    logging.error(f"Failed for {name}: {result.stderr}")
                    node_failed = True
                else:
                    parsed_nodes = parsed_csv(expanded_enum.read_text(), endpoint)
                    all_permissible_values.update(parsed_nodes)
                    logging.info(f"Expanded enumeration: {name}")

                if all_permissible_values:
                    parsed["enums"][name]["permissible_values"] = all_permissible_values
                    expanded_enum.write_text(
                        yaml.dump(
                            parsed,
                            Dumper=IndentedDumper,
                            default_flow_style=False,
                            sort_keys=False,
                            allow_unicode=True,
                        )
                    )
                    if not node_failed:
                        expanded_count += 1

    if expanded_count != enum_count:
        logging.error(f"{enum_count - expanded_count} failed to be expanded.")
    return enum_names


def update_imports(enum_list: list[str], model_filepath: Path):
    """
    Writes the name of each enum to "imports" property in model file.

    Opens file containing the master LinkML model and gets the data under the 'imports' key.
    Appends the name of each extracted enumeration to any imports that may already exist, if it is not already there.
    Writes the file with enum updates to the same filepath.
    """
    with model_filepath.open() as imports:
        imports_parsed = yaml.safe_load(imports)

    existing_imports = imports_parsed.get("imports", [])
    updated_imports = existing_imports + [
        n for n in enum_list if n not in existing_imports
    ]
    imports_parsed["imports"] = updated_imports

    with model_filepath.open("w") as f:
        yaml.dump(
            imports_parsed,
            f,
            sort_keys=False,
            Dumper=IndentedDumper,
            indent=2,
            default_flow_style=False,
        )


def exec(args: list[str] | None = None):

    parser = argparse.ArgumentParser(
        description="Expand enums from a monolithic LinkML model"
    )
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
        required=True,
        type=Path,
        help="The source file containing the enumerations to be expanded",
    )
    parser.add_argument(
        "-m",
        "--model",
        required=False,
        type=Path,
        help="The path of the model YAML file",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        type=Path,
        help="The directory where expanded output YAML files will be written",
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

    args = parser.parse_args()
    # Initialize the logger with whatever the user requested
    init_logging(args.log_level)

    enums = expand(
        local_filepath=args.source,
        output_filepath=args.output,
        iri=args.iri,
    )

    update_imports(enum_list=enums, model_filepath=args.model)
