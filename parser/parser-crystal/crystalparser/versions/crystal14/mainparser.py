from nomadcore.simple_parser import SimpleMatcher as SM
from nomadcore.baseclasses import MainHierarchicalParser
import logging
logger = logging.getLogger("nomad")


#===============================================================================
class CrystalMainParser(MainHierarchicalParser):
    """The main parser class for crystal. This main parser will take the
    crystal output file path as an argument.
    """
    def __init__(self, file_path, parser_context):
        """Initialize an output parser.
        """
        super(CrystalMainParser, self).__init__(file_path, parser_context)

        # Define the output parsing tree for this version
        self.root_matcher = SM("",
            forwardMatch=True,
        )
        #=======================================================================
        # The cache settings
        self.caching_level_for_metaname = {
        }

    #===========================================================================
    # The functions that trigger when sections are closed
    def onClose_section_method(self, backend, gIndex, section):
        pass

    #===========================================================================
    # adHoc functions that are used to do custom parsing. Primarily these
    # functions are used for data that is formatted as a table or a list.
    def adHoc_section_XC_functionals(self):
        pass
