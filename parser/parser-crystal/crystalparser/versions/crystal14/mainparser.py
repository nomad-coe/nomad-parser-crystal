import re
from nomadcore.simple_parser import SimpleMatcher as SM
from nomadcore.baseclasses import MainHierarchicalParser
from nomadcore.caching_backend import CachingLevel
import logging
import numpy as np
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
        self.regex_i = "-?\d+" # Regex for an integer
        self.regex_date = re.compile(r'(\d{2}) (\d{2}) (\d{4})')
        self.float_match = '(' + self.regex_f + ')'
        self.bohr_angstrom = 0

        self.spacegroups = [ 'P 1', 'P -1', 'P 2', 'P 21', 'C 2', 'P M', 'P C', 'C M', 'C C', 'P 2/M', 'P 21/M', 
            'C 2/M', 'P 2/C', 'P 21/C', 'C 2/C', 'P 2 2 2', 'P 2 2 21', 'P 21 21 2', 'P 21 21 21', 'C 2 2 21', 'C 2 2 2', 'F 2 2 2', 
            'I 2 2 2', 'I 21 21 21', 'P M M 2', 'P M C 21', 'P C C 2', 'P M A 2', 'P C A 21', 'P N C 2', 'P M N 21', 'P B A 2', 
            'P N A 21', 'P N N 2', 'C M M 2', 'C M C 21', 'C C C 2', 'A M M 2', 'A B M 2', 'A M A 2', 'A B A 2', 'F M M 2', 
            'F D D 2', 'I M M 2', 'I B A 2', 'I M A 2', 'P M M M', 'P N N N', 'P C C M', 'P B A N', 'P M M A', 'P N N A', 'P M N A', 
            'P C C A', 'P B A M', 'P C C N', 'P B C M', 'P N N M', 'P M M N', 'P B C N', 'P B C A', 'P N M A', 'C M C M', 'C M C A', 
            'C M M M', 'C C C M', 'C M M A', 'C C C A', 'F M M M', 'F D D D', 'I M M M', 'I B A M', 'I B C A', 'I M M A', 'P 4', 
            'P 41', 'P 42', 'P 43', 'I 4', 'I 41', 'P -4', 'I -4', 'P 4/M', 'P 42/M', 'P 4/N', 'P 42/N', 'I 4/M', 'I 41/A', 
            'P 4 2 2', 'P 4 21 2', 'P 41 2 2', 'P 41 21 2', 'P 42 2 2', 'P 42 21 2', 'P 43 2 2', 'P 43 21 2', 'I 4 2 2', 'I 41 2 2', 
            'P 4 M M', 'P 4 B M', 'P 42 C M', 'P 42 N M', 'P 4 C C', 'P 4 N C', 'P 42 M C', 'P 42 B C', 'I 4 M M', 'I 4 C M', 
            'I 41 M D', 'I 41 C D', 'P -4 2 M', 'P -4 2 C', 'P -4 21 M', 'P -4 21 C', 'P -4 M 2', 'P -4 C 2', 'P -4 B 2', 
            'P -4 N 2', 'I -4 M 2', 'I -4 C 2', 'I -4 2 M', 'I -4 2 D', 'P 4/M M M', 'P 4/M C C', 'P 4/N B M', 'P 4/N N C', 
            'P 4/M B M', 'P 4/M N C', 'P 4/N M M', 'P 4/N C C', 'P 42/M M C', 'P 42/M C M', 'P 42/N B C', 'P 42/N N M', 
            'P 42/M B C', 'P 42/M N M', 'P 42/N M C', 'P 42/N C M', 'I 4/M M M', 'I 4/M C M', 'I 41/A M D', 'I 41/A C D', 'P 3', 
            'P 31', 'P 32', 'R 3', 'P -3', 'R -3', 'P 3 1 2', 'P 3 2 1', 'P 31 1 2', 'P 31 2 1', 'P 32 1 2', 'P 32 2 1', 'R 3 2', 
            'P 3 M 1', 'P 3 1 M', 'P 3 C 1', 'P 3 1 C', 'R 3 M', 'R 3 C', 'P -3 1 M', 'P -3 1 C', 'P -3 M 1', 'P -3 C 1', 'R -3 M', 
            'R -3 C', 'P 6', 'P 61', 'P 65', 'P 62', 'P 64', 'P 63', 'P -6', 'P 6/M', 'P 63/M', 'P 6 2 2', 'P 61 2 2', 'P 65 2 2', 
            'P 62 2 2', 'P 64 2 2', 'P 63 2 2', 'P 6 M M', 'P 6 C C', 'P 63 C M', 'P 63 M C', 'P -6 M 2', 'P -6 C 2', 'P -6 2 M', 
            'P -6 2 C', 'P 6/M M M', 'P 6/M C C', 'P 63/M C M', 'P 63/M M C', 'P 2 3', 'F 2 3', 'I 2 3', 'P 21 3', 'I 21 3', 
            'P M 3', 'P N 3', 'F M 3', 'F D 3', 'I M 3', 'P A 3', 'I A 3', 'P 4 3 2', 'P 42 3 2', 'F 4 3 2', 'F 41 3 2', 'I 4 3 2', 
            'P 43 3 2', 'P 41 3 2', 'I 41 3 2', 'P -4 3 M', 'F -4 3 M', 'I -4 3 M', 'P -4 3 N', 'F -4 3 C', 'I -4 3 D', 'P M 3 M', 
            'P N 3 N', 'P M 3 N', 'P N 3 M', 'F M 3 M', 'F M 3 C', 'F D 3 M', 'F D 3 C', 'I M 3 M', 'I A 3 D']

        # Define the output parsing tree for this version
        self.root_matcher = SM("^.*$",
            sections=['section_run'],
            subMatchers=[
                SM( r"^date\s+.+$",
                    sections=['x_crystal_section_filenames'],
                    subMatchers=[
                        SM( r"^output data in (?P<x_crystal_output_filename>.+)$"),
                        SM( r"^input data in (?P<x_crystal_input_filename>.+)$")
                    ]
                ),
                SM( r"^ [\*]{22,}$",
                    sections=['x_crystal_section_programinformation'],
                    subMatchers=[
                        SM( r"^ \*[ ]{10,}CRYSTAL(?P<program_version>\d+)[\ ]{10,}\*$"),
                        SM( r"^ \*[ ]{10,}public \: (?P<x_crystal_version_minor>[\d\.]+) \- [A-Z]{1}[a-z]{2} \d+[a-z]{2}, \d{4}[\ ]{10,}\*$"),
                    ]
                ),
                SM( r"^\s+\w+\s+STARTING\s+DATE\s+\d{2} \d{2} \d{4} TIME \d{2}\:\d{2}\:\d{2}\.\d{1}$",
                    forwardMatch=True,
                    sections=['x_crystal_section_startinformation'],
                    subMatchers=[
                        SM( r"^\s+\w+\s+STARTING\s+DATE\s+(?P<x_crystal_run_start_date>\d{2} \d{2} \d{4}) TIME (?P<x_crystal_run_start_time>\d{2}\:\d{2}\:\d{2})\.\d{1}$")
                    ]
                ),
                SM( "^\s*SPACE GROUP \(CENTROSYMMETRIC\)\s*\:\s*[A-Z0-9\-\/\ ]+\s*$",
                    forwardMatch=True,
                    sections=['section_system'],
                    subMatchers=[
                        SM( "^\s*SPACE GROUP \(CENTROSYMMETRIC\)\s*\:\s*[A-Z0-9\-\/\ ]+\s*$",
                            forwardMatch=True,
                            adHoc=self.adHoc_spacegroup()
                        ),
                        SM( "^\s*GEOMETRY FOR WAVE FUNCTION \- DIMENSIONALITY OF THE SYSTEM\s+\d+\s*$",
                            forwardMatch=True,
                            subMatchers=[
                                SM( "^\s*GEOMETRY FOR WAVE FUNCTION \- DIMENSIONALITY OF THE SYSTEM\s+(?P<x_crystal_dimensionality>\d+)\s*$"),
                                SM( "^\s*LATTICE PARAMETERS \(ANGSTROMS AND DEGREES\) \- BOHR \=\s*(?P<x_crystal_bohr_angstrom>{0})\s* ANGSTROM\s*$".format(self.regex_f),
                                    forwardMatch=True,
                                    adHoc=self.adHoc_bohr_angstrom()
                                ),
                                SM( "^\s*PRIMITIVE CELL \- CENTRING CODE\s*\d+/\d+\s*VOLUME\s*\=\s*(?P<x_crystal_volume>{0})\s*\-\s*DENSITY\s*(?P<x_crystal_density>{0})\s*g/cm\^3\s*$".format(self.regex_f)),
                                SM( "^\s*A\s+B\s+C\s+ALPHA\s+BETA\s+GAMMA\s*$",
                                    adHoc=self.adHoc_lattice_parameters(),
                                    otherMetaInfo=['x_crystal_lattice_parameters', 'configuration_periodic_dimensions']
                                )
                            ]
                        ),
                        SM( "^\s*DIRECT LATTICE VECTORS CARTESIAN COMPONENTS \(ANGSTROM\)\s*$",
                            adHoc=self.adHoc_simulation_cell(),
                            otherMetaInfo=['simulation_cell']
                        ),
                        SM( "^\s*CARTESIAN COORDINATES \- PRIMITIVE CELL\s*$",
                            adHoc=self.adHoc_atom_positions(),
                            otherMetaInfo=['number_of_atoms', 'atom_labels', 'atom_positions']
                        ),
                        SM( "^\s*ATOMIC WAVEFUNCTION\(S\)\s*$",
                            sections=["section_method", "section_single_configuration_calculation"],
                            subMatchers=[
                                SM( r"^\s*CHARGE NORMALIZATION FACTOR\s*[\+\-]{0,1}\d*\.\d+\s*$",
                                    sections=["section_scf_iteration"],
                                    repeats=True,
                                    subMatchers=[
                                        SM( r"\s+CYC\s+\d+\s+ETOT\(AU\)\s+(?P<energy_total_scf_iteration__hartree>{0})\s+DETOT\s+(?P<energy_change_scf_iteration__hartree>{0})\s+".format(self.regex_f)),
                                    ]
                                ),
                                SM( r"^\s+[\:]+\s+KINETIC\s+ENERGY\s+(?P<electronic_kinetic_energy__hartree>{0})\s+".format(self.regex_f)),
                                SM( r"^\s+[\:]+\s+TOTAL\s+ENERGY\s+(?P<energy_total__hartree>{0})\s+".format(self.regex_f)),
                                SM( r"^\s+\=\=\s+SCF\s+ENDED\s+\-\s+CONVERGENCE\s+ON\s+ENERGY\s+E\(AU\)\s+{0}\s+CYCLES\s+\d+$".format(self.regex_f),
                                    adHoc=self.adHoc_single_point_converged()
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        #=======================================================================
        # The cache settings
        self.caching_level_for_metaname = {
           'x_crystal_run_start_date': CachingLevel.Cache
        }

    #===========================================================================
    # The functions that trigger when sections are closed

    def onClose_x_crystal_section_startinformation(self, backend, gIndex, section):
        """Format date properly
        """
        datestr = section["x_crystal_run_start_date"];
        if datestr is not None:
            datestr = datestr[0]
            if datestr is not None:
                datestr = self.regex_date.match(datestr);
                if datestr is not None:
                    datestr = datestr.group(3) + '-' + datestr.group(2) + '-' + datestr.group(1)
                    backend.superBackend.addValue("x_crystal_run_start_date", datestr)
        pass

    def onClose_section_method(self, backend, gIndex, section):
        pass

    #===========================================================================
    # adHoc functions that are used to do custom parsing. Primarily these
    # functions are used for data that is formatted as a table or a list.

    def adHoc_spacegroup(self):
        def wrapper(parser):
            name = re.compile("^\s*SPACE GROUP \(CENTROSYMMETRIC\)\s*\:\s*([A-Z0-9\-\/\ ]+)\s*$").match(parser.fIn.readline())
            if name is None:
                return
            name = str(name.group(1))
            while(name.endswith(" ")):
                name = name[:-1]
            while(name.startswith(" ")):
                name = name[1:]
            for i in range(230):
                if name == self.spacegroups[i]:
                    parser.backend.addValue("spacegroup_3D_number", i+1)
                    break
        return wrapper

    def adHoc_single_point_converged(self):
        """Called when the SCF cycle of a single point calculation has converged.
        """
        def wrapper(parser):
            parser.backend.addValue("single_configuration_calculation_converged", True)
        return wrapper
        

    def adHoc_simulation_cell(self):
        def wrapper(parser):
            clabels_match = re.compile("^\s*([XYZ]{1})\s+([XYZ]{1})\s+([XYZ]{1})\s*$")
            cvector_match = re.compile('^\s*' + self.float_match + '\s+' + self.float_match + '\s+' + self.float_match + '\s*$')
            clabels = re.compile("^\s*X\s+Y\s+Z\s*$").match(parser.fIn.readline());
            if not clabels:
                return False
            n = 0
            vectors = []
            for i in range(1,4):
                cvector = cvector_match.match(parser.fIn.readline());
                if not cvector:
                    break;
                vector = []
                for j in range(1,4):
                    v = float(cvector.group(j))
                    if v is None:
                        break
                    vector.append(v)
                    n = n + 1
                vectors.append(vector)
            if n == 9:
                parser.backend.addArrayValues("simulation_cell", vectors, unit="angstrom")
        return wrapper

    def adHoc_bohr_angstrom(self):
        def wrapper(parser):
            v = re.compile("^\s*LATTICE PARAMETERS \(ANGSTROMS AND DEGREES\) \- BOHR \=\s*" + self.float_match + "\s* ANGSTROM\s*$").match(parser.fIn.readline())
            if v is None:
                return
            v = float(v.group(1))
            if v is None:
                return
            self.bohr_angstrom = v
            return
        return wrapper

    def adHoc_lattice_parameters(self):
        def wrapper(parser):
            cvector_match = re.compile('^\s*' + self.float_match + '\s+' + self.float_match + '\s+' + self.float_match + '\s+' + self.float_match + '\s+' + self.float_match + '\s+' + self.float_match + '\s*$')
            line1 = cvector_match.match(parser.fIn.readline())
            factor = parser.backend.superBackend
            if not line1:
                return
            periodic = []
            params = []
            for i in xrange(6):
                v = float(line1.group(i+1))
                if i < 3:
                    params.append(v * self.bohr_angstrom)
                    p = 1
                    if v == 500:
                        p = 0
                    periodic.append(p)
                else:
                    params.append(v)
            params = np.array(params)
            periodic = np.array(periodic)
            if self.bohr_angstrom > 0:
                parser.backend.addArrayValues("x_crystal_lattice_parameters", params)
            parser.backend.addArrayValues("configuration_periodic_dimensions", periodic)
        return wrapper

    def adHoc_atom_positions(self):
        def wrapper(parser):
            cvector_match = re.compile('^\s*(\d+)\s+(\d+)\s+([A-Za-z0-9]+)\s+' + self.float_match + '\s+' + self.float_match + '\s+' + self.float_match + '\s*$')
            line1 = re.compile('^\s*[\*]{20,}\s*$').match(parser.fIn.readline())
            line2 = re.compile('^\s*\*\s+ATOM\s+X\(ANGSTROM\)\s+Y\(ANGSTROM\)\s+Z\(ANGSTROM\)\s*$').match(parser.fIn.readline())
            line3 = re.compile('^\s*[\*]{20,}\s*$').match(parser.fIn.readline())
            if (not line1) or (not line2) or (not line3):
                return False
            labels = []
            coordinates = []
            while True:
                cvector = cvector_match.match(parser.fIn.readline())
                if cvector is None:
                    break;
                vector = []
                for j in range(4,7):
                    v = float(cvector.group(j))
                    if v is None:
                        break;
                    vector.append(v)
                if len(vector) != 3:
                    break;
                label = str(cvector.group(3))
                if(len(label) == 2):
                    label = label[0].capitalize() + label[1].lower()
                label = label + '.' + cvector.group(2) + '.' + cvector.group(1)
                coordinates.append(vector)
                labels.append(label)
            coordinates = np.array(coordinates)
            labels = np.array(labels)
            parser.backend.addArrayValues("atom_labels", labels)
            parser.backend.addArrayValues("atom_positions", coordinates, unit="angstrom")
            parser.backend.addValue("number_of_atoms", len(coordinates))
        return wrapper
