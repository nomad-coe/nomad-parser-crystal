import os
import re
import logging
from nomadcore.baseclasses import ParserInterface
from crystalparser.versions.versionsetup import get_main_parser
logger = logging.getLogger(__name__)


#===============================================================================
class CrystalParser(ParserInterface):
    """This class handles the initial setup before any parsing can happen. It
    determines which version of the software was used to generate the output
    and then sets up a correct main parser.

    After the implementation has been setup, you can parse the files with
    parse().
    """
    def __init__(self, main_file, metainfo_to_keep=None, backend=None, default_units=None, metainfo_units=None):
        super(CrystalParser, self).__init__(main_file, metainfo_to_keep, backend, default_units, metainfo_units)

    def setup_version(self):
        """Setups the version by looking at the output file and the version
        specified in it.
        """
        # Search for the version specification and initialize a correct
        # main parser for this version.

        # Setup the correct main parser based on the version id. If no match
        # for the version is found, use the main parser for CP2K 2.6.2
        # self.main_parser = get_main_parser(version_id)(self.parser_context.main_file, self.parser_context)

    def get_metainfo_filename(self):
        return "crystal.nomadmetainfo.json"

    def get_parser_info(self):
        return {'name': 'crystal-parser', 'version': '1.0'}
