"""Data model package for cam-expanded-enums."""

from pathlib import Path
from .cam_expanded_enums import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "cam_expanded_enums.yaml"
