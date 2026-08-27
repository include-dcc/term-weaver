import argparse
import logging
import ssl
import urllib.request
from pathlib import Path

import pyhornedowl
from car_utils import setup_logging

logger = logging.getLogger(__name__)


def convert_owl(url: str, output_filepath: Path, convert_type: str):
    """Converts a file to RDF/XML format and saves it at user-specified location.
    Args:
        url: The URL of the OWL file to be converted to RDF/XML.
        output_filepath: The filepath for saving the converted file.
        convert_type: The type of file to be converted.
    """
    if convert_type == "fowl2owl":
        ssl._create_default_https_context = ssl._create_unverified_context
        output_filepath.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(url) as response:
            data = response.read().decode("utf-8")

        onto = pyhornedowl.open_ontology_from_string(data)
        onto.save_to_file(str(output_filepath))
        logger.info(f"Converted {url} to RDF/XML.")


def exec():
    parser = argparse.ArgumentParser(
        description="Convert OWL2 Functional-Style Syntax to RDF/XML"
    )
    parser.add_argument(
        "-log",
        "--log-level",
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Logging level tolerated (default is INFO)",
    )
    parser.add_argument(
        "-u",
        "--url",
        required=True,
        help="URL of the OWL2 Functional-Style Syntax file to convert.",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="Output filename for the converted RDF/XML file.",
    )
    parser.add_argument(
        "-c",
        "--convert-type",
        choices=["fowl2owl"],
        default="fowl2owl",
        required=False,
        help="The type of file to convert to RDF/XML format.",
    )
    args = parser.parse_args()
    setup_logging(level=args.log_level)

    convert_owl(args.url, args.output, args.convert_type)
