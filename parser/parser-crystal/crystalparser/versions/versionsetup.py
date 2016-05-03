"""Returns the main parser class based on the given version identifier.
The different version are grouped into subpackages.
"""
import importlib
import logging
logger = logging.getLogger("nomad")


def get_main_parser(version_id):

    # Currently the version id is a pure integer, so it can directly be mapped
    # into a package name.
    base = "crystalparser.parsing.versions.crystal{}.".format(version_id)
    try:
        main_parser = importlib.import_module(base + "mainparser").CrystalMainParser
    except ImportError:
        logger.debug("A parser with the version id '{}' could not be found. Defaulting to the base implementation based on CRYSTAL14 public 1.0.3 ".format(version_id))
        base = "crystalparser.versions.crystal14."
        main_parser = importlib.import_module(base + "mainparser").CrystalMainParser
    return main_parser
