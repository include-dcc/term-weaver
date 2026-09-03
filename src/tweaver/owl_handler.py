import argparse
import logging
import ssl
import urllib.request
from pathlib import Path

import pyhornedowl
from car_utils import setup_logging

logger = logging.getLogger(__name__)


def fowl2owl(url: str, output_filepath: Path):
    """Converts an OWL2 Functional-Style Syntax file to RDF/XML format and saves it at user-specified location.
    Args:
        url: The URL of the OWL file to be converted to RDF/XML.
        output_filepath: The filepath for saving the converted file.
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    output_filepath.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8")

    onto = pyhornedowl.open_ontology_from_string(data)
    onto.save_to_file(str(output_filepath))
    logger.info(f"Converted {url} to RDF/XML.")


def save_owl(url: str, output_filepath: Path):
    output_filepath.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8")
    onto = pyhornedowl.open_ontology_from_string(data)
    onto.save_to_file(str(output_filepath))
    logger.info(f"Saved {url} to {output_filepath}")


def open_owl(url: str):
    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8")
    return pyhornedowl.open_ontology_from_string(data)


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
        # required=True,
        type=Path,
        help="Output filename for the converted RDF/XML file.",
    )
    parser.add_argument(
        "-a",
        "--action",
        choices=["fowl2owl", "save", "open"],
        default="fowl2owl",
        required=False,
        help="The type of file to convert to RDF/XML format.",
    )
    args = parser.parse_args()
    setup_logging(level=args.log_level)

    if args.action == "fowl2owl":
        fowl2owl(args.url, args.output)
    if args.action == "save":
        save_owl(args.url, args.output)
    if args.action == "open":
        open_owl(args.url)
