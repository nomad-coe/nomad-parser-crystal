import os
import re
import logging
import importlib
from nomadcore.baseclasses import ParserInterface
logger = logging.getLogger(__name__)


#===============================================================================
class CrystalParser(ParserInterface):
    """This class handles the initial setup before any parsing can happen. It
    determines which version of the software was used to generate the output
    and then sets up a correct main parser.

    After the implementation has been setup, you can parse the files with
    parse().
    """
    def __init__(self, main_file, metainfo_to_keep=None, backend=None, default_units=None, metainfo_units=None, debug=None, log_level=logging.ERROR):
        super(CrystalParser, self).__init__(main_file, metainfo_to_keep, backend, default_units, metainfo_units, debug, log_level)

    def setup_version(self):
        """Setups the version by looking at the output file and the version
        specified in it.
        """
        # Search for the version specification and initialize a correct
        # main parser for this version.

        version_regex = re.compile(
            r" \*\s+CRYSTAL(\d+)\s+\*"
        )
        version_id = None
        with open(self.parser_context.main_file, 'r') as fin:
            for line in fin:
                match = version_regex.match(line)
                if match:
                    version_id = match.groups()[0]
        if not version_id:
            logger.error("Could not find a version specification from the given main file.")

        self.setup_main_parser(version_id)

    def get_metainfo_filename(self):
        return "crystal.nomadmetainfo.json"

    def get_parser_info(self):
        return {'name': 'crystal-parser', 'version': '1.0'}

    def setup_main_parser(self, version_id, run_type=None):
        # Currently the version id is a pure integer, so it can directly be mapped
        # into a package name.
        base = "crystalparser.versions.crystal{}.".format(version_id)
        try:
            parser_class = importlib.import_module(base + "mainparser").CrystalMainParser
        except ImportError:
            logger.debug("A parser with the version id '{}' could not be found. Defaulting to the base implementation based on CRYSTAL14 public 1.0.3 ".format(version_id))
            base = "crystalparser.versions.crystal14."
            parser_class = importlib.import_module(base + "mainparser").CrystalMainParser
        self.main_parser = parser_class(self.parser_context.main_file, self.parser_context)
