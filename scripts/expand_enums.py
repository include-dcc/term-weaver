import argparse
import logging
import subprocess
from pathlib import Path

import yaml


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

            reachable = enum.get("reachable_from") or {}
            source_onto = reachable.get("source_ontology")
            if not source_onto:
                continue
            ontology = source_onto.split(":")[1]

            result = subprocess.run(
                [
                    "dragon_search",
                    "-o",
                    str(ontology),
                    "-i",
                    str(iri),
                    "-f",
                    str(expanded_enum),
                    "-d",
                ],
                capture_output=True,
                text=True,
            )
            enum_count += 1
            if result.returncode != 0:
                logging.error(f"Failed for {name}: {result.stdout}")
                logging.error(f"Failed for {name}: {result.stderr}")
            else:
                expanded_count += 1
                logging.info(f"Expanded enumeration: {name}")

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
    parser.add_argument(
        "-i",
        "--iri",
        required=True,
        help="A string value containing the iri for the code",
    )

    args = parser.parse_args()

    enums = expand(
        local_filepath=args.source, output_filepath=args.output, iri=args.iri
    )
