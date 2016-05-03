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
        # for the version is found, use the main parser for Crystal14
        # self.main_parser = get_main_parser(version_id)(self.parser_context.main_file, self.parser_context)
        regex1 = re.compile(r" [\*]{22,}\n")
        regex2 = re.compile(r" \*[ ]{20,}\*\n")
        regex3 = re.compile(r" \*[ ]{10,}CRYSTAL([\d]+)[ ]{10,}\*\n")
        regex4 = re.compile(r" \*[ ]{10,}public \: ([\d\.]+) \- [A-Z]{1}[a-z]{2} [\d]+[a-z]{2}, [\d]{4}[ ]{10,}\*\n")
        line1 = line2 = line3 = line4 = line5 = ""
        version_minor = version_major = version_id = ""
        with open(self.parser_context.main_file, 'r') as outputfile:
            while True:
                line5 = next(outputfile)
                if not line5:
                    break
                line1 = line2
                line2 = line3
                line3 = line4
                line4 = line5
                if regex1.match(line1) and regex2.match(line2):
                    result3 = regex3.match(line3)
                    if not result3:
                        continue
                    result4 = regex4.match(line4)
                    if not result4:
                        continue
                    version_major = result3.group(1)
                    version_minor = result4.group(1).replace('.', '')
                    version_id = version_major + "_" + version_minor;
                    break
        if not version_id:
            logger.error("Could not find a version specification from the given main file.")
        self.main_parser = get_main_parser(version_id)(self.parser_context.main_file, self.parser_context)

    def get_metainfo_filename(self):
        return "crystal.nomadmetainfo.json"

    def get_parser_info(self):
        return {'name': 'crystal-parser', 'version': '1.0'}
