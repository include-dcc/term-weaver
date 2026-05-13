import logging
import sys
from argparse import ArgumentParser  # , FileType

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


def exec(args: list[str] | None = None):
    parser = ArgumentParser(
        prog="term-weaver",
        description="""Materializing Enumerations since 2026""",
    )
    parser.add_argument(
        "-log",
        "--log-level",
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Logging level tolerated (default is INFO)",
    )

    args = parser.parse_args(args)
    # Initialize the logger with whatever the user requested
    init_logging(args.log_level)

    logging.info(f"You have chose to use: {args}")
    logging.warn(f"Hello")
    logging.error("world")
    logging.debug("Goodbye")
