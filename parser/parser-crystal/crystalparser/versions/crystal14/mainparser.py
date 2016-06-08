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

        class SubFlags:
            Sequenced = 0    # the subMatchers should be executed in sequence
            Unordered = 1    # the subMatchers can be in any order

        # Define the output parsing tree for this version
        self.regex_f = "-?(?:\d+\.?\d*|\d*\.?\d+)(?:E[\+-]?\d+)?"  # Regex for a floating point value
        self.regex_i = "-?\d+" # Regex for an integer
        self.float_match = '(' + self.regex_f + ')'
        self.input = {} #hash for storing input related information
        self.input_geometries = {
            'CRYSTAL'  : 1,
            'SLAB'     : 1,
            'POLYMER'  : 1,
            'HELIX'    : 1,
            'MOLECULE' : 1,
            'EXTERNAL' : 1,
            'DLVINPUT' : 1
        }
        self.input_geometry_adhoc = {
            'FREQCALC' : 'adhoc_input_freqcalc'
        }
        self.input_basis_adhoc = {
        }
        self.input_param_adhoc = {
            'SHRINK'   : 'adhoc_input_shrink',
            'PPAN'     : 'adhoc_input_ppan'
        }
        self.input_state = 0
        self.input_substate = 0
        self.input_adhoc = None
        self.bohr_angstrom = 0
        self.regex_csectionname = re.compile("^x_crystal_section_(\w+)$")
        self.regex_cend = re.compile("^END(\S*)$")
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

        self.caching_level_for_metaname = {
            'x_crystal_input_title': CachingLevel.ForwardAndCache,
            'x_crystal_input_keyword': CachingLevel.Cache,
        }

        # Define the output parsing tree for this version

        matcher_process = SM("^.*$",
            sections=['x_crystal_section_process'],
            forwardMatch=True,
            subFlags = SubFlags.Unordered,
            subMatchers=[
                SM( "^\s*date\s+(?P<x_crystal_process_datetime>.*?)\s*$",
                    adHoc=self.adHoc_x_crystal_process_datetime()),
                SM( "^\s*hostname\s+(?P<x_crystal_process_hn>.*?)\s*$"),
                SM( "^\s*system\s+(?P<x_crystal_process_os>.*?)\s*$"),
                SM( "^\s*user\s+(?P<x_crystal_process_user>.*?)\s*$"),
                SM( "^\s*input\s+data\s+in\s+(?P<x_crystal_process_input>.*)$"),
                SM( "^\s*output\s+data\s+in\s+(?P<x_crystal_process_output>.*)$"),
                SM( "^\s*crystal\s+executable\s+in\s+(?P<x_crystal_process_exe>.*)$"),
                SM( "^\s*temporary\s+directory\s+(?P<x_crystal_process_tmpdir>.*)$")
        ])
        matcher_input = SM("^\s*(?P<x_crystal_input_title>\S+.*\S+)\s*$",
            sections=['x_crystal_section_input'],
            forwardMatch=True,
            subFlags = SubFlags.Unordered,
            adHoc=self.adHoc_x_crystal_input_title(),
            subMatchers = self.appendNumberMatchers([
                SM( "^\s*(?P<x_crystal_input_keyword>[A-Za-z]+)\s*$",
                    repeats=True,
                    adHoc=self.adHoc_x_crystal_input(0))
                ], 5, 'x_crystal_input', 'value')
        )
        matcher_header = SM("^\s*[\*]{10,}\s*$",
            sections=['x_crystal_section_header'],
            subMatchers=[
                SM( "^\s*\*\s*CRYSTAL(?P<x_crystal_header_version>.*?)\s*\*\s*$"),
                SM( "^\s*\*\s*(?P<x_crystal_header_distribution>.*?)\s*\:\s*(?P<x_crystal_header_minor>.*?)\s*-\s*(?P<x_crystal_header_date>.*?)\s*\*\s*$"),
                SM( "^\s*\*\s*(?P<x_crystal_header_url>.*?://.*?)\s*\*\s*$")
                
        ])
        matcher_start = SM( r"^\s+\w+\s+STARTING\s+DATE\s+\d{2} \d{2} \d{4} TIME \d{2}\:\d{2}\:\d{2}\.\d{1}$",
            forwardMatch=True,
            sections=['x_crystal_section_startinformation'],
            subMatchers=[
                SM( r"^\s+\w+\s+STARTING\s+DATE\s+(?P<x_crystal_run_start_date>\d{2} \d{2} \d{4}) TIME (?P<x_crystal_run_start_time>\d{2}\:\d{2}\:\d{2})\.\d{1}$")
        ])
        matcher_system = SM( "^\s*SPACE GROUP \(CENTROSYMMETRIC\)\s*\:\s*[A-Z0-9\-\/\ ]+\s*$",
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
        ])
        
        self.root_matcher = SM("^.*$",
            forwardMatch=True,
            subMatchers=[
                matcher_process,
                matcher_input,
                matcher_header,
                matcher_start,
                matcher_system
        ])

    def appendNumberMatchers(self, subMatchers, n, sname, key):
        regexes = []
        for i in range(1,n+1):
            keyword = sname + '_' + key + str(i)
            self.caching_level_for_metaname[keyword] = CachingLevel.Cache
            regexes.append("(?P<" + keyword + ">{0})")
            regex_str = ("^\s*" + "\s+".join(regexes) + "\s*$").format(self.regex_f)
            attrname = "adHoc_" + sname
            attrobject = getattr(self, attrname)
            if attrobject is None:
                raise Exception("No such function" + attname)
            subMatchers.append(SM(regex_str, repeats=True, adHoc=attrobject(i)))
        return subMatchers
            
    def getSection(self, parser):
        i = 0
        n = len(parser.context) - 1
        while n >= 0:
            ctx = parser.context[n]
            items = ctx.sections.items()
            if len(items) > 0:
                name, gIndex = items[len(items)-1]
                os = parser.backend.sectionManagers[name].openSections;
                return [os[gIndex], name]
            n = n-1
        return [None, None]

    def getKey(self, sectionname, key):
        sectionname = self.regex_csectionname.match(sectionname)
        if sectionname is None:
            return key
        sectionname = str(sectionname.group(1))
        return 'x_crystal_' + sectionname + '_' + key;

    def getAdHocValues(self, parser, key, n):
        section,sectionname = self.getSection(parser)
        if section is None:
            return None
        key = self.getKey(sectionname, key)
        ret = []
        for i in range(1, n+1):
            data = section[key+str(i)]
            if data is not None:
                data = data[len(data)-1]
            ret.append(data)
        return ret

    def getAdHocValue(self, parser, key):
        section,sectionname = self.getSection(parser)
        if section is None:
            return None
        key = self.getKey(sectionname, key)
        data = section[key]
        if data is not None:
            data = data[len(data)-1]
        return data

    def inputFails(self, comment = ""):
        raise Exception("inputFails state=" + str(self.input_state) + " substate=" + str(self.input_substate) + " comment=" + str(comment))
        self.input_state = -1
        return

    #===========================================================================
    # The functions that trigger when sections are closed

    def onClose_x_crystal_section_input(self, backend, gIndex, section):
        pass

    def onClose_section_method(self, backend, gIndex, section):
        pass

    #===========================================================================
    # adHoc functions that are used to do custom parsing. Primarily these
    # functions are used for data that is formatted as a table or a list.

    def adHoc_x_crystal_process_datetime(self):
        def wrapper(parser):
            section = self.getSection(parser)
        return wrapper

    def adHoc_x_crystal_input_title(self):
        def wrapper(parser):
            self.input['title'] = self.getAdHocValue(parser, 'title')
            self.input_state = 0
        return wrapper

    def adHoc_x_crystal_input(self, n=0):
        def wrapper(parser):
            keyword = None
            endpattern = None
            values = []
            if n == 0:
                keyword = self.getAdHocValue(parser, 'keyword')
                if self.input_state == 0 and self.input['title'] is not None and keyword == self.input['title']:
                    return
                keyword = keyword.upper()
                endpattern = self.regex_cend.match(keyword)
                if endpattern is not None:
                    endpattern = str(endpattern.group(1))
            else:
                values = self.getAdHocValues(parser, 'value', n)
            if self.input_adhoc is not None:
                attr = getattr(self, self.input_adhoc)
                return attr(parser, n, values, keyword, endpattern)
            if self.input_state == 0:
                if keyword is None or self.input_geometries[keyword] is None:
                    return self.inputFails()
                self.input['geometry'] = keyword
                parser.backend.addValue("x_crystal_input_geometry", keyword)
                if keyword == "CRYSTAL":
                    self.input_state += 1
                else:
                    self.input_state += 2
                return
            if self.input_state == 1:
                if n != 3:
                    return self.inputFails()
                self.input['iflag'] = int(values[0])
                parser.backend.addValue('x_crystal_input_iflag', int(values[0]));
                self.input['ifhr']  = int(values[1])
                parser.backend.addValue('x_crystal_input_ifhr',  int(values[1]));
                self.input['ifso']  = int(values[2])
                parser.backend.addValue('x_crystal_input_ifso',  int(values[2]));
                self.input_state += 1
                return
            if self.input_state == 2:
                if self.input['iflag'] == 0:
                    if n != 1:
                        return self.inputFails()
                    parser.backend.addValue('x_crystal_input_spacegroup', int(values[0]))
                else:
                    if n != 0:
                        return self.inputFails()
                    parser.backend.addValue('x_crystal_input_spacegroup_hm', keyword)
                if self.input['ifso'] <= 1:
                    self.input_state += 2
                else:
                    self.input_state += 1
                return
            if self.input_state == 3:
                if n != 3:
                    return self.inputFails()
                parser.backend.addArrayValues('x_crystal_input_shift_of_origin', np.array(values))
                self.input_state += 1
                return
            if self.input_state == 4:
                if n < 1:
                    return self.inputFails()
                parser.backend.addArrayValues('x_crystal_input_lattice_parameters', np.array(values))
                self.input_state += 1
                return
            if self.input_state == 5:
                if n != 1:
                    return self.inputFails()
                num = int(values[0])
                self.input['atoms_left'] = num;
                parser.backend.addValue('x_crystal_input_number_of_atoms', num)
                self.input_state += 1                
                return
            if self.input_state == 6:
                if n != 4:
                    return self.inputFails()
                gIndex = parser.backend.openSection('x_crystal_section_input_atom')
                parser.backend.addValue('x_crystal_input_atom_z', int(values.pop(0)))
                parser.backend.addArrayValues('x_crystal_input_atom_position', np.array(values));
                parser.backend.closeSection('x_crystal_section_input_atom', gIndex)
                self.input['atoms_left'] -= 1
                if self.input['atoms_left'] == 0:
                    self.input_state += 1
                return
            if self.input_state == 7:
                if endpattern is not None:
                    self.input_state += 1
                    return
                if n != 0:
                    return self.inputFails("n = " + str(n))
                self.input_substate = 0
                self.input_adhoc = self.input_geometry_adhoc[keyword]
                if self.input_adhoc is None:
                    return self.inputFails("input_adhoc is None")
                attr = getattr(self, self.input_adhoc)
                return attr(parser, n, values, keyword, endpattern)
            if self.input_state == 8:
                if n != 2:
                    return self.inputFails()
                atom_z = int(values[0])
                self.input['shells_left'] = int(values[1])
                if atom_z == 99 and self.input['shells_left'] == 0:
                    self.input_state += 3
                    return
                self.input['basis_gIndex'] = parser.backend.openSection('x_crystal_section_input_basis')
                parser.backend.addValue('x_crystal_input_basis_z', atom_z)
                parser.backend.addValue('x_crystal_input_basis_number_of_shells', self.input['shells_left']);
                self.input_state += 1
                return
            if self.input_state == 9:
                if n != 5:
                    return self.inputFails('shell does not contain 5 values')
                self.input['shell_gIndex'] = parser.backend.openSection('x_crystal_section_input_basis_shell')
                shell_type                    = int(values[0])
                self.input['shell_l']         = int(values[1])
                self.input['primitives_left'] = int(values[2])
                parser.backend.addValue('x_crystal_input_basis_shell_type', shell_type)
                parser.backend.addValue('x_crystal_input_basis_shell_l', self.input['shell_l'])
                parser.backend.addValue('x_crystal_input_basis_shell_number_of_primitives', self.input['primitives_left']);
                parser.backend.addValue('x_crystal_input_basis_shell_charge', values[3]);
                parser.backend.addValue('x_crystal_input_basis_shell_scale', values[4]);
                if shell_type != 0 or self.input['primitives_left'] <= 0:
                    self.input['primitives_left'] = 0
                    self.input['shells_left'] -= 1
                    parser.backend.closeSection('x_crystal_section_input_basis_shell', self.input['shell_gIndex'])
                    if self.input['shells_left'] <= 0:
                        self.input_state -= 1
                        parser.backend.closeSection('x_crystal_section_input_basis', self.input['basis_gIndex']);
                else:
                    self.input_state += 1
                return             
            if self.input_state == 10:
                if self.input['shell_l'] == 1:
                    if n != 3: return self.inputFail("primitive should contain 3 values")
                else:
                    if n != 2: return self.inputFail("primitive should contain 2 values")
                primitive_gIndex = parser.backend.openSection('x_crystal_section_input_basis_shell_primitive')
                parser.backend.addValue('x_crystal_input_basis_shell_primitive_exp', values[0])
                if n == 3:
                    parser.backend.addValue('x_crystal_input_basis_shell_primitive_coefficient_s', values[1])
                    parser.backend.addValue('x_crystal_input_basis_shell_primitive_coefficient_p', values[2])
                else:
                    parser.backend.addValue('x_crystal_input_basis_shell_primitive_coefficient', values[1])
                parser.backend.closeSection('x_crystal_section_input_basis_shell_primitive', primitive_gIndex)
                self.input['primitives_left'] -= 1
                if self.input['primitives_left'] <= 0:
                    self.input['shells_left'] -= 1
                    self.input_state -= 1
                    parser.backend.closeSection('x_crystal_section_input_basis_shell', self.input['shell_gIndex'])
                    if self.input['shells_left'] <= 0:
                        self.input_state -= 1
                        parser.backend.closeSection('x_crystal_section_input_basis', self.input['basis_gIndex']);
                return
            if self.input_state == 11:
                if endpattern is not None:
                    self.input_state += 1
                    return
                if n != 0:
                    return self.inputFails("n = " + str(n))
                self.input_substate = 0
                self.input_adhoc = self.input_basis_adhoc[keyword]
                if self.input_adhoc is None:
                    return self.inputFails("input_adhoc is None")
                return
            if self.input_state == 12:
                if endpattern is not None:
                    self.input_state += 1 #finished parsing the input file
                    return
                if n != 0:
                    return self.inputFails("n = " + str(n))
                self.input_substate = 0
                self.input_adhoc = self.input_param_adhoc[keyword]
                if self.input_adhoc is None:
                    return self.inputFails("input_adhoc is None")
                attr = getattr(self, self.input_adhoc)
                return attr(parser, n, values, keyword, endpattern)
            if self.input_state == 13:
                print "EXTRA LINES"
                return
        return wrapper
    
    def adhoc_input_freqcalc(self, parser, n, values, keyword, endpattern):
        if self.input_substate == 0:
            self.input_substate += 1
            return
        if self.input_substate == 1:
            if endpattern is not None:
                self.input_adhoc = None;
                del self.input['dieltens']
                return
            if keyword == 'INTENS':
                parser.backend.addValue('x_crystal_input_intens', 1)
                return
            if keyword == 'DIELTENS':
                self.input_substate += 1
                self.input['dieltens'] = []
                return
            return self.inputFails()
        if self.input_substate == 2:
            if n != 3:
                return self.inputFails()
            self.input['dieltens'].append(values)
            if len(self.input['dieltens']) == 3:
                parser.backend.addArrayValues('x_crystal_input_dielectric_tensor', np.array(self.input['dieltens']))
                self.input_substate = 1

    def adhoc_input_shrink(self, parser, n, values, keyword, endpattern):
        if self.input_substate == 0:
            print "DEBUG: adhoc_input_shrink 1"
            self.input_substate += 1
            return
        if n != 2:
            return self.inputFails("shrink should contain 2 values")
        print "DEBUG: adhoc_input_shrink 2"
        parser.backend.addArrayValues('x_crystal_input_shrink', np.array(values))
        self.input_adhoc = None
        return
        
    def adhoc_input_ppan(self, parser, n, values, keyword, endpattern):
        print "DEBUG: adhoc_input_ppan 1"
        parser.backend.addValue('x_crystal_input_ppan', 1)
        self.input_adhoc = None
        return

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

