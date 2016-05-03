import sys
import re
from nomadcore.simple_parser import SimpleMatcher as SM
from nomadcore.baseclasses import MainHierarchicalParser
from nomadcore.caching_backend import CachingLevel
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
        self.regex_f = "-?\d+\.\d+(?:E(?:\+|-)\d+)?"  # Regex for a floating point value
        self.regex_i = "-?\d+"  # Regex for an integer
        self.regex_date = re.compile(r'(\d{2}) (\d{2}) (\d{4})')

        # Define the output parsing tree for this version
        self.root_matcher = SM("",
            forwardMatch=True,
            sections=['section_run', "section_system_description", "section_method"],
            subMatchers=[
                SM( r"^input data in .+$",
                    forwardMatch=True,
                    sections=['crystal_section_filenames'],
                    subMatchers=[
                        SM( r"^input data in (?P<crystal_input_filename>.+)$"),
                    ]
                ),
                SM( r"^ [\*]{22,}$",
                    forwardMatch=True,
                    sections=['crystal_section_programinformation'],
                    subMatchers=[
                        SM( r"^ \*[ ]{10,}CRYSTAL(?P<program_version>\d+)[ ]{10,}\*$"),
                       SM( r"^ \*[ ]{10,}public \: (?P<crystal_version_minor>[\d\.]+) \- [A-Z]{1}[a-z]{2} \d+[a-z]{2}, \d{4}[ ]{10,}\*$"),
                    ]
                ),
                SM( r"^\s+\w+\s+STARTING\s+DATE\s+\d{2} \d{2} \d{4} TIME \d{2}\:\d{2}\:\d{2}\.\d{1}$",
                    forwardMatch=True,
                    sections=['crystal_section_startinformation'],
                    subMatchers=[
                        SM( r"^\s+\w+\s+STARTING\s+DATE\s+(?P<crystal_run_start_date>\d{2} \d{2} \d{4}) TIME (?P<crystal_run_start_time>\d{2}\:\d{2}\:\d{2})\.\d{1}$")
                    ]
                ),
            ]
        )
        #=======================================================================
        # The cache settings
        self.caching_level_for_metaname = {
           'crystal_version_minor': CachingLevel.Cache,
           'crystal_run_start_date': CachingLevel.Cache,
        }

    #===========================================================================
    # The functions that trigger when sections are closed
    def onClose_crystal_section_programinformation(self, backend, gIndex, section):
        """Tidy version number
        """
        version_minor = section["crystal_version_minor"][0]
        if version_minor is not None:
            version_minor = version_minor.replace('.', '')
            backend.superBackend.addValue("crystal_version_minor", version_minor)
        pass

    def onClose_crystal_section_startinformation(self, backend, gIndex, section):
        """Format date properly
        """
        datestr = section["crystal_run_start_date"];
        if datestr is not None:
            datestr = datestr[0]
            if datestr is not None:
                datestr = self.regex_date.match(datestr);
                if datestr is not None:
                    datestr = datestr.group(3) + '-' + datestr.group(2) + '-' + datestr.group(1)
                    backend.superBackend.addValue("crystal_run_start_date", datestr)
        pass

    def onClose_section_method(self, backend, gIndex, section):
        pass

    #===========================================================================
    # adHoc functions that are used to do custom parsing. Primarily these
    # functions are used for data that is formatted as a table or a list.
    def adHoc_section_XC_functionals(self):
        pass
