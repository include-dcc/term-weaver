from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("term-weaver")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"
