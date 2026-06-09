import argparse
import csv
import io
import logging
import subprocess
from pathlib import Path

import yaml


def parsed_csv(csv_text: str) -> dict:
    """Parse dragon_search CSV output into permissible_values object for enum yaml file."""
    reader = csv.DictReader(io.StringIO(csv_text))
    permissible_values = {}
    for row in reader:
        code = row["descendant_code"]
        if code.lower() == "no results":
            continue
        description = row.get("description", "")
        if description.startswith("['") and description.endswith("']"):
            description = description[2:-2]
        permissible_values[code] = {
            "text": code,
            "description": description,
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
        model_filepath: The file containing master LinkML model, used to get the id property to reuse for enums
        output_filepath: The directory where the enum YAMLs are to be written
    Returns:
        list of enum names
    """
    if output_filepath is None:
        output_filepath = Path("output")

    output_filepath.mkdir(parents=True, exist_ok=True)
    enum_count = 0
    expanded_count = 0
    for enum_file in local_filepath.glob("Enum*.yaml"):
        raw_enum = enum_file.read_text()
        parsed = yaml.safe_load(raw_enum)

        enums = parsed.get("enums", {})
        for name, enum in enums.items():
            expanded_enum = output_filepath / f"{name}.yaml"

            if "permissible_values" in (enum) and enum["permissible_values"]:
                expanded_enum.write_text(raw_enum)
                logging.info(f"Copied {name} (permissible_values already exists)")
                enum_count += 1
                expanded_count += 1
                continue

            reachable_from = enum.get("reachable_from") or {}
            source_onto = reachable_from.get("source_ontology")
            source_nodes = reachable_from.get("source_nodes")
            if not source_onto:
                continue
            ontology = source_onto.split(":")[1]
            if not source_nodes:
                continue

            all_permissible_values = {}
            node_failed = False
            for node in source_nodes:
                result = subprocess.run(
                    [
                        "dragon_search",
                        "-ak",
                        str(node),
                        "-o",
                        str(ontology),
                        "-f",
                        str(expanded_enum),
                        "-d",
                        "-s",
                        "0",
                    ],
                    capture_output=True,
                    text=True,
                )
                enum_count += 1
                if result.returncode != 0:
                    logging.error(f"Failed for {name}: {result.stdout}")
                    logging.error(f"Failed for {name}: {result.stderr}")
                    node_failed = True
                else:
                    parsed_nodes = parsed_csv(expanded_enum.read_text())
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


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(
        description="Expand enums from a monolithic LinkML model"
    )
    parser.add_argument(
        "-s",
        "--source",
        required=True,
        type=Path,
        help="The source file containing the enumerations to be expanded",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        type=Path,
        help="The directory where expanded output YAML files will be written",
    )

    args = parser.parse_args()

    enums = expand(local_filepath=args.source, output_filepath=args.output)
