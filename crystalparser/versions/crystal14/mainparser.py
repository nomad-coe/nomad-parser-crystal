# Copyright 2016-2018 Sami Kivistö, Lauri Himanen, Fawzi Mohamed, Ankit Kariryaa
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import re
from nomadcore.simple_parser import SimpleMatcher as SM
from nomadcore.baseclasses import MainHierarchicalParser
from nomadcore.caching_backend import CachingLevel
from nomadcore.elements import get_atom_number
from .inputparser import CrystalInputParser
import logging
import numpy as np
logger = logging.getLogger("nomad")


class CrystalMainParser(MainHierarchicalParser):
    """The main parser class for crystal. This main parser will parse the
    output file.
    """
    def __init__(self, parser_context):
        """Initialize an output parser.
        """
        super(CrystalMainParser, self).__init__(parser_context)

        # Define the output parsing tree for this version
        self.regex_f = "-?(?:\d+\.?\d*|\d*\.?\d+)(?:E[\+-]?\d+)?"  # Regex for a floating point value
        self.regex_i = "-?\d+"  # Regex for an integer
        self.regex_s = "\S+.*?\S+"  # Regex for a string
        self.regex_crystal_float = "-?\d+(?:.\d+)?\*\*-?.*\d+"  # Regex for a crystal specific float
        self.float_match = '(' + self.regex_f + ')'
        self.regex_fs = re.compile(self.float_match)
        self.regex_kpoint = re.compile("(\d+)-([A-Z]+)\(\s*(\d+)\s*(\d+)\s*(\d+)\s*\)")
        self.regex_filterspace = re.compile('(\s+)')
        self.system = {}
        self.method = {}
        self.element_numbers = {}
        self.method['x_crystal_scf_kinetic_energy'] = None
        self.method['x_crystal_restart_dos_scale_t'] = 0
        self.bohr_angstrom = 0
        self.regex_csectionname = re.compile("^x_crystal_section_(\w+)$")
        self.regex_cend = re.compile("^END(\S*)$")
        self.cache_service.add('x_crystal_info_type_of_calculation2', single=False, update=False)
        self.gtf_nl = {}  # hash storing radial functions for each quantum number pair (n,l)
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

        #=======================================================================
        # Cache levels
        self.caching_levels.update({
            'x_crystal_input_title': CachingLevel.ForwardAndCache,
            'x_crystal_input_keyword': CachingLevel.Cache,
            'x_crystal_primitive_cell_atom_value1': CachingLevel.Cache,
            'x_crystal_primitive_cell_atom_value2': CachingLevel.Cache,
            'x_crystal_primitive_cell_atom_value3': CachingLevel.Cache,
            'x_crystal_prim_atom_tag': CachingLevel.Cache,
            'x_crystal_prim_atom_value1': CachingLevel.Cache,
            'x_crystal_prim_atom_value2': CachingLevel.Cache,
            'x_crystal_prim_atom_value3': CachingLevel.Cache,
            'x_crystal_cell_atom_tag': CachingLevel.Cache,
            'x_crystal_cell_atom_value1': CachingLevel.Cache,
            'x_crystal_cell_atom_value2': CachingLevel.Cache,
            'x_crystal_cell_atom_value3': CachingLevel.Cache,
            'x_crystal_basis_set_atom_value1': CachingLevel.Cache,
            'x_crystal_basis_set_atom_value2': CachingLevel.Cache,
            'x_crystal_basis_set_atom_value3': CachingLevel.Cache,
            'x_crystal_basis_set_atom_shell_omin': CachingLevel.ForwardAndCache,
            'x_crystal_basis_set_atom_shell_omax': CachingLevel.ForwardAndCache,
            'x_crystal_frequency_gradients_op_text': CachingLevel.Cache,
            'x_crystal_vibrational_symmetry_text': CachingLevel.Cache,
            'x_crystal_vibrational_text1': CachingLevel.Cache,
            'x_crystal_vibrational_text2': CachingLevel.Cache,
            'x_crystal_vibrational_text3': CachingLevel.Cache,
            'x_crystal_vibrational_minus': CachingLevel.Cache,
            'x_crystal_vibrational_integer1': CachingLevel.Cache,
            'x_crystal_vibrational_integer2': CachingLevel.Cache,
            'x_crystal_restart_dos_scale_t': CachingLevel.ForwardAndCache,
            'x_crystal_restart_dos_energy_text':  CachingLevel.Cache,
            'x_crystal_info_type_of_calculation2': CachingLevel.ForwardAndCache,
            'x_crystal_info_text': CachingLevel.Cache,
        })

        # Define the output parsing tree for this version
        matcher_process = SM("^.*$",
            sections=['x_crystal_section_process'],
            forwardMatch=True,
            subFlags=SM.SubFlags.Unordered,
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
            ]
        )
        self.input_parser = CrystalInputParser(self)
        matcher_input = SM("^\s*(?P<x_crystal_input_title>\S+.*\S+)\s*$",
            sections=['x_crystal_section_input'],
            subMatchers=[
                self.input_parser.root_matcher,
            ]
        )
        matcher_header = SM("^\s*[\*]{10,}\s*$",
            sections=['x_crystal_section_header'],
            subMatchers=[
                SM( "^\s*\*\s*CRYSTAL(?P<program_version>.*?)\s*\*\s*$"),
                SM( "^\s*\*\s*(?P<x_crystal_header_distribution>.*?)\s*\:\s*(?P<x_crystal_header_minor>.*?)\s*-\s*(?P<x_crystal_header_date>.*?)\s*\*\s*$"),
                SM( "^\s*\*\s*(?P<x_crystal_header_url>.*?://.*?)\s*\*\s*$")

            ]
        )
        matcher_start = SM( r"^\s*E+\s+STARTING\s+DATE\s+\d{2} \d{2} \d{4} TIME \d{2}\:\d{2}\:\d{2}\.\d{1}$",
            forwardMatch=True,
            sections=['x_crystal_section_startinformation'],
            subMatchers=[
                SM( "^\s+\w+\s+STARTING\s+DATE\s+(?P<x_crystal_run_start_date>\d{2} \d{2} \d{4}) TIME (?P<x_crystal_run_start_time>\d{2}:\d{2}:\d{2}(\.\d+)?)\s*$"),
                SM( "^\s*(?P<x_crystal_run_title>.*?)\s*$"),
            ])
        matcher_end = SM( "^\s*T+\s+END\s+TELAPSE\s+" + self.fk('x_crystal_endinformation_telapse') + "\s+TCPU\s+" + self.fk('x_crystal_endinformation_tcpu') + "\s*$",
            sections=['x_crystal_section_endinformation'], subMatchers=[
                SM( "^\s*E+\s+TERMINATION\s+DATE\s+(?P<x_crystal_run_end_date>\d{2} \d{2} \d{4}) TIME (?P<x_crystal_run_end_time>\d{2}:\d{2}:\d{2}(\.\d+)?)\s*$")
        ])
        regex_gaussian_primitive = ("^\s*(?P<x_crystal_basis_set_atom_shell_primitive_exp>{0})" +
            "\s+(?P<x_crystal_basis_set_atom_shell_primitive_coeff_s>{0})" +
            "\s+(?P<x_crystal_basis_set_atom_shell_primitive_coeff_p>{0})" +
            "\s+(?P<x_crystal_basis_set_atom_shell_primitive_coeff_dfg>{0})\s*$").format(self.regex_f)

        matcher_info = SM( " INFORMATION",
            forwardMatch=True,
            sections=['x_crystal_section_info'],
            subMatchers=[

                SM( "^\s*INFORMATION\s*\*+.*?\*+.*?\:\s*FOCK/KS MATRIX MIXING SET TO\s*(?P<x_crystal_info_fock_ks_matrix_mixing>{0})\s+\%\s*$".format(self.regex_f)),
                SM( "^\s*INFORMATION\s*\*+.*?\*+.*?\:\s*COULOMB BIPOLAR BUFFER SET TO\s*(?P<x_crystal_info_coulomb_bipolar_buffer>{0})\s+Mb\s*$".format(self.regex_f)),
                SM( "^\s*INFORMATION\s*\*+.*?\*+.*?\:\s*EXCHANGE BIPOLAR BUFFER SET TO\s*(?P<x_crystal_info_exchange_bipolar_buffer>{0})\s+Mb\s*$".format(self.regex_f)),
                SM( "^\s*INFORMATION\s*\*+\s*TOLDEE\s*\*+\s*\*+\s*SCF TOL ON TOTAL ENERGY SET TO\s*" + self.fk('x_crystal_info_toldee') + "\s*$"),
                SM( "^\s*INFORMATION\s*\*+\s*(?P<x_crystal_info_item_key>.*?)\s*\*+\s*(?P<x_crystal_info_item_value>.*?)\s*$", sections=['x_crystal_section_info_item']),

                SM( re.escape(" *******************************************************************************")),
                SM( "^\s*N\. OF ATOMS PER CELL\s+(?P<x_crystal_info_number_of_atoms>\d+)\s+.*$", forwardMatch=True),
                SM( "^\s*NUMBER OF SHELLS\s+(?P<x_crystal_info_number_of_shells>\d+)\s+.*$", forwardMatch=True),
                SM( "^\s*NUMBER OF AO\s+(?P<x_crystal_info_number_of_orbitals>\d+)\s+.*$", forwardMatch=True),
                SM( "^\s*N\. OF ELECTRONS PER CELL\s+(?P<x_crystal_info_number_of_electrons>\d+)\s+.*$", forwardMatch=True),
                SM( "^\s*CORE ELECTRONS PER CELL\s+(?P<x_crystal_info_number_of_core_electrons>\d+)\s+.*$", forwardMatch=True),
                SM( "^\sN\. OF SYMMETRY OPERATORS\s+(?P<x_crystal_info_number_of_symmops>\d+)\s+.*$", forwardMatch=True),
                SM( "^.*COULOMB OVERLAP TOL\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_info_tol_coulomb_overlap>{})\s*$".format(self.regex_f)),
                SM( "^.*COULOMB PENETRATION TOL\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_info_tol_coulomb_penetration>{})\s*$".format(self.regex_f)),
                SM( "^.*EXCHANGE OVERLAP TOL\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_info_tol_exchange_overlap>{})\s*$".format(self.regex_f)),
                SM( "^.*EXCHANGE PSEUDO OVP \(F\(G\)\)\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_info_tol_pseudo_overlap_f>{})\s*$".format(self.regex_f)),
                SM( "^.*EXCHANGE PSEUDO OVP \(P\(G\)\)\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_info_tol_pseudo_overlap_p>{})\s*$".format(self.regex_f)),
                SM( "^.*POLE ORDER IN MONO ZONE\s*(?P<x_crystal_info_pole_order>\d+)\s*$"),
                SM( "^\s*[A-Z\. ]+\s+\d+\s+[A-Z\. ]+.*?\d+\s*$"),

                SM( re.escape(" *******************************************************************************")),
                SM( " TYPE OF CALCULATION",
                    forwardMatch=True,
                    adHoc=self.adHoc_type_of_calculation
                ),
                SM( " \(EXCHANGE\)\[CORRELATION\] FUNCTIONAL:\((.+)\)\[(.+)\]".format(self.regexs.eol),
                ),
                SM( "^.*CAPPA\s*:\s*IS1\s+(?P<x_crystal_info_is1>\d+)\s*;\s*IS2\s+(?P<x_crystal_info_is2>\d+)\s*;\s*IS3\s+(?P<x_crystal_info_is3>\d+)\s*;\s*K PTS MONK NET\s+(?P<x_crystal_info_k_pts_monk_net>\d+)\s*;\s*SYMMOPS\s*:\s*K SPACE\s+(?P<x_crystal_info_symmops_k>\d+)\s*;\s*G SPACE\s+(?P<x_crystal_info_symmops_g>\d+)\s*$"),

                SM( " MAX NUMBER OF SCF CYCLES\s+(?P<scf_max_iteration>{})".format(self.regexs.int)),
                SM( " WEIGHT OF F\(I\) IN F\(I\+1\)\s+(?P<x_crystal_info_weight_previous>{})\%\s+CONVERGENCE ON ENERGY\s+({})".format(self.regexs.int, self.regex_crystal_float),
                    startReAction=self.transform_scf_convergence
                ),
                SM( " SHRINK\. FACT\.\(MONKH\.\)\s+" + self.fsk('x_crystal_info_shrink_value', 3) + "\s+.*$"),
                SM( " SHRINKING FACTOR\(GILAT NET\)\s+(?P<x_crystal_info_shrink_gilat>{})\s+.*$".format(self.regex_f)),

                # SM( "^.*CONVERGENCE ON DELTAP\s+10\*\*\s*(-? *\d+)\s*$", startReTransform=self.transform_convergence_on_deltap),
                # SM( "^.*CONVERGENCE ON ENERGY\s+10\*\*\s*(-? *\d+)\s*$", startReTransform=self.transform_convergence_on_energy),
                # SM( "^.*NUMBER OF K POINTS IN THE IBZ\s*(?P<x_crystal_info_k_points_ibz>\d+)\s*$"),
                # SM( "^.*NUMBER OF K POINTS\(GILAT NET\)\s*(?P<x_crystal_info_k_points_gilat>\d+)\s*$"),
                # SM( "^\s*[A-Z\.\(\) ]+\s+\d+\%?\s+[A-Z\(\)]+.*?\d+\s*$"),
                # SM( "^\s*\*+\s*$")
            ])
        matcher_lattice = SM( "^\s*DIRECT LATTICE VECTORS COMPON\. \(A\.U\.\)\s*RECIP\. LATTICE VECTORS COMPON\. \(A\.U\.\)\s*$", subMatchers=[
                SM( "^\s*X\s+Y\s+Z\s+X\s+Y\s+Z\s*$", sections=['x_crystal_section_lattice'], adHoc=self.adHoc_x_crystal_lattice())
        ])
        matcher_infoeigen = SM( "^\s*DISK SPACE FOR EIGENVECTORS\s*\(FTN\s*(?P<x_crystal_info_eigenvectors_disk_space_ftn>\d+)\s*\)\s+(?P<x_crystal_info_eigenvectors_disk_space_reals>\d+)\s+REALS\s*$",
            sections=['x_crystal_section_info'], subMatchers=[
                SM( "^\s*SYMMETRY ADAPTION OF THE BLOCH FUNCTIONS (ENABLED|DISABLED)\s*$", startReAction=self.transform_symmetry_adaption),
                SM( "^\s*MATRIX SIZE:\s*P\(G\)\s*(?P<x_crystal_info_matrix_size_p>\d+),\s*F\(G\)\s*(?P<x_crystal_info_matrix_size_f>\d+),\s*P\(G\)\s*IRR\s*(?P<x_crystal_info_irr_p>\d+),\s*F\(G\)\s*IRR\s*(?P<x_crystal_info_irr_f>\d+)\s*$"),
                SM( "^\s*MAX G-VECTOR INDEX FOR 1- AND 2-ELECTRON INTEGRALS\s+(?P<x_crystal_info_max_g_vector_index>\d+)\s*$"),
                SM( "^\s*T+\s+INPUT\s+TELAPSE\s+(?P<x_crystal_info_input_telapse>{0})\s+TCPU\s+(?P<x_crystal_info_input_tcpu>{0})\s*$".format(self.regex_f))
            ])
        matcher_kpoints = SM( "^\s*\*+\s*K POINTS COORDINATES \(OBLIQUE COORDINATES IN UNITS OF IS\s*=\s*(?P<x_crystal_kpoints_is_units>\d+)\s*\)\s*$",
            sections=['x_crystal_section_kpoints'], adHoc=self.adHoc_x_crystal_kpoints('kpoint')
        )
        matcher_neighbors = SM( "^\s*NEIGHBORS OF THE NON-EQUIVALENT ATOMS\s*$", subMatchers=[
                SM( "^\s*N\s*=\s*NUMBER OF NEIGHBORS AT DISTANCE R\s*$", subMatchers=[
                        SM( "^\s*ATOM\s+N\s+R\s*/\s*ANG\s+R\s*/\s*AU\s+NEIGHBORS\s*\(ATOM LABELS AND CELL INDICES\)\s*$", sections=['x_crystal_section_neighbors'], subMatchers=[
                                SM( "^\s*(?P<x_crystal_neighbors_atom_label>\d+)\s+(?P<x_crystal_neighbors_atom_element>[A-Z]+)\s+\d+\s+" + self.fs(2) + ".*?$",
                                    sections=['x_crystal_section_neighbors_atom'], repeats=True, forwardMatch=True, adHoc=self.adHoc_x_crystal_neighbors(3))
                        ]),
                        SM( " THERE ARE NO SYMMETRY ALLOWED DIRECTIONS",
                            sections=['x_crystal_section_symmetry'],
                            forwardMatch=True,
                            subMatchers=[
                                SM( " THERE ARE NO SYMMETRY ALLOWED DIRECTIONS",
                                    fixedStartValues={"x_crystal_symmetry_allowed_directions": 0}
                                ),
                                SM( "^\s*T+\s+SYMM\s+TELAPSE\s+(?P<x_crystal_symmetry_telapse>{0})\s+TCPU\s+(?P<x_crystal_symmetry_tcpu>{0})\s*$".format(self.regex_f),
                                    subMatchers=[
                                        SM( "^\s*T+\s+INT\_SCREEN\s+TELAPSE\s+(?P<x_crystal_symmetry_intscreen_telapse>{0})\s+TCPU\s+(?P<x_crystal_symmetry_intscreen_tcpu>{0})\s*$".format(self.regex_f))
                                    ]
                                )
                            ]
                        )
                        # SM( "^\s*SYMMETRY ALLOWED ELASTIC DISTORTION\s*" + self.dk('x_crystal_symmetry_distortion_number') + "\s*$", sections=['x_crystal_subMatchers=[
                                # SM("^\s*" + self.fsk('x_crystal_symmetry_distortion_value', 3) "\s*$", adHoc=self.
                ])
        ])
        matcher_frequency2 = SM( "^\s*ATOMS ISOTOPIC MASS \(AMU\) FOR FREQUENCY CALCULATION\s*$", subMatchers=[
                SM( "^(\s+\d+\s+[A-Z]+\s+" + self.regex_f + ")+\s*$", forwardMatch=True, adHoc=self.adHoc_x_crystal_frequency_atom()),
                SM( "^\s*N\s+LABEL\s+SYMBOL\s+DISPLACEMENT\s+SYM\.\s*$", subMatchers=[
                        SM( "^\s*1\s+EQUILIBRIUM GEOMETRY\s+(?P<x_crystal_frequency_gradients_equilibrium_symmops>\d+)\s*$", sections=['x_crystal_section_frequency_gradients'], subMatchers=[
                                SM( "^\s+(?P<x_crystal_frequency_gradients_op_num>\d+)\s+(?P<x_crystal_frequency_gradients_op_label>\d+)\s+(?P<x_crystal_frequency_gradients_op_element>[A-Z]+)\s+(?P<x_crystal_frequency_gradients_op_displacement>[A-Z]+)\s+(?P<x_crystal_frequency_gradients_op_text>.+?)\s*$",
                                    sections=['x_crystal_section_frequency_gradients_op'], repeats=True, adHoc=self.adHoc_x_crystal_section_frequency_gradients_op()),
                                SM( "^\s*NUMERICAL GRADIENT COMPUTED WITH A SINGLE DISPLACEMENT \(\+DX\) FOR EACH\s*$", subMatchers=[
                                        SM( "^\s*CARTESIAN COORDINATE WITH RESPECT TO THE EQUILIBRIUM CONFIGURATION\s*$", subMatchers=[
                                                SM( "^\s*DX\s*=\s*" + self.fk('x_crystal_frequency_gradients_dx') + "\s+ANGSTROM\s*$"),
                                                SM( "^\s*NUMBER OF IRREDUCIBLE ATOMS\s+(?P<x_crystal_frequency_gradients_number_of_atoms>\d+)\s*$"),
                                                SM( "^\s*NUMBER OF SCF\+GRADIENT CALCULATIONS\s+(?P<x_crystal_frequency_gradients_number_of_ops>\d+)\s*$"),
                                                SM( "^\s*ATOM\s+SYMOP\s+ORDER\s*$", subMatchers=[
                                                        SM( "^\s*(?P<x_crystal_frequency_gradients_atom_label>\d+)\s+(?P<x_crystal_frequency_gradients_atom_number_of_symmops>\d+)\s+(?P<x_crystal_frequency_gradients_atom_order>\d+)\s*$",
                                                            repeats=True, sections=['x_crystal_section_frequency_gradients_atom'])
                                                ])
                                        ])
                                ]),
                        ])
                ])
        ])
        matcher_frequency = SM( "^\s*\*\s*CALCULATION OF PHONON FREQUENCIES AT THE GAMMA POINT\.\s*\*\s*$", subMatchers=[
                SM( "^\s*\*\s*SYMMETRY IS EXPLOITED TO BUILD THE TOTAL HESSIAN MATRIX\.\s*\*\s*$", sections=['x_crystal_section_frequency'], subMatchers=[
                        matcher_frequency2
                ])
        ])
        matcher_wavefunctions = SM( "^\s*NUCLEAR CHARGE\s+" + self.fs(1) + "\s+SYMMETRY SPECIES\s+S\s+P\s*$",
            forwardMatch=True, repeats=True, sections=['x_crystal_section_wavefunctions'], subMatchers=[
                SM( "^\s*NUCLEAR CHARGE\s+" + self.fk('x_crystal_wavefunctions_atom_nuclear_charge') + "\s+SYMMETRY SPECIES\s+S\s+P\s*$",
                    sections=['x_crystal_section_wavefunctions_atom'], repeats=True, subMatchers=[
                        SM( "^\s*N\. ELECTRONS\s+" + self.fk('x_crystal_wavefunctions_atom_number_of_electrons') + "\s+NUMBER OF PRIMITIVE GTOS\s+(?P<x_crystal_wavefunctions_atom_number_of_primitive_s>\d+)\s+(?P<x_crystal_wavefunctions_atom_number_of_primitive_p>\d+)\s*$"),
                        SM( "^\s*NUMBER OF CONTRACTED GTOS\s+(?P<x_crystal_wavefunctions_atom_number_of_contracted_s>\d+)\s+(?P<x_crystal_wavefunctions_atom_number_of_contracted_p>\d+)\s*$"),
                        SM( "^\s*NUMBER OF CLOSED SHELLS\s+(?P<x_crystal_wavefunctions_atom_number_of_closed_shells_s>\d+)\s+(?P<x_crystal_wavefunctions_atom_number_of_closed_shells_p>\d+)\s*$"),
                        SM( "^\s*OPEN SHELL OCCUPATION\s+(?P<x_crystal_wavefunctions_atom_open_shell_occupation_s>\d+)\s+(?P<x_crystal_wavefunctions_atom_open_shell_occupation_p>\d+)\s*$"),
                        SM( "^\s*ZNUC\s+SCFIT\s+TOTAL HF ENERGY\s+KINETIC ENERGY\s+VIRIAL THEOREM ACCURACY\s*$", subMatchers=[
                                SM( "^\s*" + self.fk('x_crystal_wavefunctions_atom_znuc') + "\s+(?P<x_crystal_wavefunctions_atom_scfit>\d+)\s+" + self.fk('x_crystal_wavefunctions_atom_total_hf_energy')
                                    +"\s+" + self.fk('x_crystal_wavefunctions_atom_kinetic_energy') + "\s+" + self.fk('x_crystal_wavefunctions_atom_virial_theorem')
                                    +"\s+" + self.fk('x_crystal_wavefunctions_atom_accuracy') + "\s*$")
                        ])
                ])
        ])

        matcher_scf_dft = SM(" CHARGE NORMALIZATION FACTOR",
            forwardMatch=True,
            subMatchers=[
                SM(" CHARGE NORMALIZATION FACTOR\s+{}".format(self.regexs.float),
                    repeats=True,
                    sections=["section_scf_iteration"],
                    subMatchers=[
                        SM( "^\s*TOTAL ATOMIC CHARGES:\s+",
                            # adHoc=self.adHoc_x_crystal_total_atomic_charges('initial')
                        ),
                        SM(" TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT QGAM        TELAPSE\s+{0} TCPU\s+{0}".format(self.regexs.float)),
                        SM(" TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT BIEL2       TELAPSE\s+{0} TCPU\s+{0}".format(self.regexs.float)),
                        SM(re.escape(" +++ ENERGIES IN A.U. +++")),
                        SM(re.escape(" ::: EXT EL-POLE : L =\s+{0}\s+{0}".format(self.regexs.int, self.regexs.float))),
                        SM(" TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT TOTENY      TELAPSE\s+{0} TCPU\s+{0}".format(self.regexs.float)),
                        SM(" NUMERICALLY INTEGRATED DENSITY\s+{0}".format(self.regexs.float)),
                        SM(" TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT NUMDFT      TELAPSE\s+{0} TCPU\s+{0}".format(self.regexs.float)),
                        SM(" CYC\s+{0} ETOT\(AU\)\s+(?P<energy_total_scf_iteration__hartree>{1}) DETOT\s+(?P<energy_change_scf_iteration__hartree>{1}) tst\s+{1} PX\s+{1}".format(self.regexs.int, self.regexs.float)),
                        SM(" TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT FDIK        TELAPSE\s+{0} TCPU\s+{0}".format(self.regexs.float)),
                        SM(" INSULATING STATE"),
                        SM(" TOP OF VALENCE BANDS -    BAND\s+{0}; K\s+{0}; EIG\s+{1} AU".format(self.regexs.int, self.regexs.float)),
                        SM(" BOTTOM OF VIRTUAL BANDS - BAND\s+{0}; K\s+{0}; EIG\s+{1} AU".format(self.regexs.int, self.regexs.float)),
                        SM(" TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT PDIG        TELAPSE\s+{0} TCPU\s+{0}".format(self.regexs.float)),
                    ]
                ),
                SM(" == SCF ENDED - CONVERGENCE ON ENERGY      E\(AU\)\s+{1} CYCLES\s+(?P<number_of_scf_iterations>{0})".format(self.regexs.int, self.regexs.float),
                    fixedStartValues={"single_configuration_calculation_converged": True}
                ),
                SM(" TOTAL ENERGY\(DFT\)\(AU\)\(\s+{0}\)\s+(?P<energy_total__hartree>{1}) DE{1} tester\s+{1}".format(self.regexs.int, self.regexs.float)),
                SM(" TOTAL ENERGY\(HF\)\(AU\)\(\s+{0}\)\s+(?P<energy_total__hartree>{1}) DE {1} tst {1} PX {1}".format(self.regexs.int, self.regexs.float)),
            ],
        )

        matcher_forcematrix2 = SM( "^\s*CENTRAL POINT\s+" + self.fk('x_crystal_forces_central_point_energy') + "\s+(?P<x_crystal_forces_central_point_cycles>\d+)\s+"
            +self.fk('x_crystal_forces_central_point_de') + "\s+(?P<x_crystal_forces_central_point_sym>\d+)\s*$", subMatchers=[
                SM( "^\s*(?P<x_crystal_forces_matrix_atom_label>\d+)\s+(?P<x_crystal_forces_matrix_atom_element>[A-Z]+)\s+(?P<x_crystal_forces_matrix_atom_dir>[A-Z]+)\s+"
                    +self.fk('x_crystal_forces_matrix_atom_grad') + "\s+" + self.fk('x_crystal_forces_matrix_atom_energy') + "\s+(?P<x_crystal_forces_matrix_atom_cycles>\d+)\s+"
                    +self.fk('x_crystal_forces_matrix_atom_de') + "\s+(?P<x_crystal_forces_matrix_atom_sym>\d+)\s*$",
                    sections=['x_crystal_section_forces_matrix_atom'],
                    subMatchers=[
                        SM( "^\s*(?P<x_crystal_forces_matrix_atom_gen_label>\d+)\s+(?P<x_crystal_forces_matrix_atom_gen_element>[A-Z]+)\s+(?P<x_crystal_forces_matrix_atom_gen_dir>[A-Z]+)\s+"
                            +"GENERATED FROM A PREVIOUS LINE\s*$",
                            sections=['x_crystal_section_forces_matrix_atom_gen'],
                            repeats=True
                        )
                ])
        ])
        matcher_forcematrix = SM( "^\s*H+\s*$", subMatchers=[
                SM( "^\s*FORCE CONSTANT MATRIX - NUMERICAL ESTIMATE\s*$", subMatchers=[
                        SM( "^\s*H+\s*$", subMatchers=[
                                SM( "^\s*MAX ABS\(DGRAD\): MAXIMUM ABSOLUTE GRADIENT DIFFERENCE WITH RESPECT TO\s*$", subMatchers=[
                                        SM( "^\s*THE CENTRAL POINT\s*$", subMatchers=[
                                                SM( "^\s*DE:\s*ENERGY DIFFERENCE WITH RESPECT TO THE CENTRAL POINT\s*$", subMatchers=[
                                                        SM( "^\s*\(DE IS EXPECTED TO BE POSITIVE FOR ALL DISPLACEMENTS\)\s*$", subMatchers=[
                                                                SM( "^\s*ATOM\s+MAX\s+ABS\(DGRAD\)\s+TOTAL ENERGY \(AU\)\s+N\.CYC\s+DE\s+SYM\s*$", subMatchers=[matcher_forcematrix2])])])])])])])])

        matcher_bornchargetensor = SM( "^\s*ATOMIC BORN CHARGE TENSOR \(UNITS OF e\, ELECTRON CHARGE\)\.\s*$", subMatchers=[
                SM( "^\s*DYNAMIC CHARGE\s*=\s+1\/3\s*\*\s*TRACE\s*\.\s*$", subMatchers=[
                        SM( "^\s*ATOM\s+(?P<x_crystal_forces_born_atom_label>\d+)\s+(?P<x_crystal_forces_born_atom_element>[A-Z]+)\s+DYNAMIC CHARGE\s+" + self.fk('x_crystal_forces_born_atom_charge') + "\s*$",
                            sections=['x_crystal_section_forces_born_atom'], repeats=True, subMatchers=[
                                SM( "^\s*1\s+2\s+3\s*$", adHoc=self.adHoc_x_crystal_forces_born_atom_tensor(3))
                        ])
                ])
        ])

        matcher_vibrational2 = SM( "^\s*(?P<x_crystal_vibrational_symmetry_class>\S+)\s+\|\s*(?P<x_crystal_vibrational_symmetry_text>[0-9\; ]+?)\s*$",
            sections=['x_crystal_section_vibrational_symmetry'], repeats=True)
        matcher_vibrational3 = SM( "^\s*IRREP/CLA\s+(?P<x_crystal_vibrational_text1>.*?)\s*$", subMatchers=[
                SM( "^\s*-+\s*$", subMatchers=[
                        SM( "^\s*MULTIP\s*\|\s*(?P<x_crystal_vibrational_text2>.*?)\s*$", subMatchers=[
                                SM( "^\s*-+\s*$", subMatchers=[
                                        SM( "^\s*Fu\s*\|\s*(?P<x_crystal_vibrational_text3>.*?)\s*$", adHoc=self.adHoc_x_crystal_vibrational_multip(), subMatchers=[
                                                SM( "^\s*Fu\s*(?P<x_crystal_vibrational_minus>-?)\((?P<x_crystal_vibrational_integer1>\d+)\s*,\s*(?P<x_crystal_vibrational_integer2>\d+)\s*\)\;\s*$",
                                                    adHoc=self.adHoc_x_crystal_vibrational_fu())
        ])])])])])

        matcher_vibrational4 = SM( "^\s*SYMMETRY ADAPTED DIRECTIONS FOR LONGITUDINAL OPTICAL MODES\s*$", subMatchers=[
                SM( "^\s*IRREP\s+X\s+Y\s+Z\s*$", subMatchers=[
                        SM( "^\s*Fu\s+" + self.fsk('x_crystal_vibrational_value', 3) + "\s*$", adHoc=self.adHoc_x_crystal_vibrational_optical(3))
        ])])

        matcher_vibrational5 = SM( "^\s*BORN CHARGE VECTOR IN THE BASIS OF NORMAL MODES\s*\(UNITS OF e\*M\_E\*\*\(-1/2\)\s*\)\.\s*$", subMatchers=[
                SM( "^\s*e AND M_E ARE UNITS OF ELECTRON CHARGE AND MASS, RESPECTIVELY\.\s*$", subMatchers=[
                        SM( "^\s*MODE\s+X\s+Y\s+Z\s*$", subMatchers=[
                                SM( "^\s*(?P<x_crystal_vibrational_mode_number>\d+)\s+" + self.fsk('x_crystal_vibrational_mode_value', 3) + "\s*$",
                                    sections=['x_crystal_section_vibrational_mode'], repeats=True, adHoc=self.adHoc_x_crystal_vibrational_mode(3))
        ])])])

        matcher_vibrational6 = SM( "^\s*H+\s*$", subMatchers=[
                SM( "^\s*VIBRATIONAL CONTRIBUTIONS TO THE STATIC DIELECTRIC TENSOR \(OSCILLATOR\s*$", subMatchers=[
                        SM( "^\s*STRENGTHS\) ARE PURE NUMBERS\. THEY ARE COMPUTED FOR EACH nth MODE AS:\s*$", subMatchers=[
                                SM( "^\s*f_\(n,ij\) = 1 / \(4 \* pi \* eps0\) \* 4 \* pi / V \* Z_\(n,i\) \* Z_\(n,j\) / nu_n\*\*2\s*$", subMatchers=[
                                        SM( "^\s*H+\s*$", subMatchers=[
                                                SM( "^\s*MODE\s+CARTESIAN AXES SYSTEM\s*$", subMatchers=[
                                                        SM( "^\s*(?P<x_crystal_vibrational_mode_number>\d+)\s+" + self.fsk('x_crystal_vibrational_mode_value', 3) + "\s*",
                                                            sections=['x_crystal_section_vibrational_mode'], repeats=True, adHoc=self.adHoc_x_crystal_vibrational_modetensor(3))
        ])])])])])])

        matcher_vibrational7 = SM( "^\s*SUM TENSOR OF THE VIBRATIONAL CONTRIBUTIONS TO THE STATIC DIELECTRIC\s+TENSOR\s*$", subMatchers=[
                SM( "^\s*" + self.fsk('x_crystal_vibrational_value', 3) + "\s*", adHoc=self.adHoc_x_crystal_vibrational_tensor(3, 'contrib'))
        ])
        matcher_vibrational8 = SM( "^\s*HIGH FREQUENCY DIELECTRIC\s+TENSOR \(FROM INPUT\)\s*$", subMatchers=[
                SM( "^\s*" + self.fsk('x_crystal_vibrational_value', 3) + "\s*", adHoc=self.adHoc_x_crystal_vibrational_tensor(3, 'hf'))
        ])
        matcher_vibrational9 = SM( "^\s*STATIC DIELECTRIC\s+TENSOR\s*$", subMatchers=[
                SM( "^\s*" + self.fsk('x_crystal_vibrational_value', 3) + "\s*", adHoc=self.adHoc_x_crystal_vibrational_tensor(3, 'static'))
        ])

        matcher_vibrational_irto2 = SM( "^\s*CONVERSION FACTORS FOR FREQUENCIES:\s*$", sections=['x_crystal_section_irto'], subMatchers=[
                SM( "^\s*1 CM\*\*\(-1\)\s*=\s*" + self.fk('x_crystal_irto_conversion_hartree') + "\s*HARTREE\s*$"),
                SM( "^\s*1 THZ\s*=\s*" + self.fk('x_crystal_irto_conversion_thz') + "\s*CM\*\*\(-1\)\s*$"),
                SM( "^\s*H+\s*$", subMatchers=[
                        SM( "^\s*MODES\s+EIGV\s+FREQUENCIES\s+IRREP\s+IR\s+INTENS\s+RAMAN\s*$", subMatchers=[
                                SM( "^\s*\(HARTREE\*\*2\)\s*\(CM\*\*-1\)\s*\(THZ\)\s*\(KM/MOL\)\s*$", subMatchers=[
                                        SM( "^\s*(?P<x_crystal_irto_mode_min>\d+)\s*-\s*(?P<x_crystal_irto_mode_max>\d+)\s+" + self.fk('x_crystal_irto_mode_eigv') + "\s+" +
                                            self.fk('x_crystal_irto_mode_frequency_cmp') + "\s+" + self.fk('x_crystal_irto_mode_frequency_thz') + "\s*\(\s*(?P<x_crystal_irto_mode_irrep>\S+)\s*\)\s*"
                                            +"(?P<x_crystal_irto_mode_ir>\S+)\s*\(\s*" + self.fk('x_crystal_irto_mode_intens') + "\s*\)\s*(?P<x_crystal_irto_mode_raman>\S+)\s*$",
                                            sections=['x_crystal_section_irto_mode'], repeats=True),
                                SM( "^\s*NORMAL MODES NORMALIZED TO CLASSICAL AMPLITUDES\s*$", sections=['x_crystal_section_irto_modes'], subMatchers=[
                                        SM( "^\s*FREQ\(CM\*\*-1\)\s+.*$", forwardMatch=True, repeats=True, subMatchers=[
                                                SM( "^\s*FREQ\(CM\*\*-1\)\s+" + self.fsk('x_crystal_irto_modes_value', 6) + "\s*$", adHoc=self.adHoc_x_crystal_irX_modes('to', 3, 2)),
                                                SM( "^\s*FREQ\(CM\*\*-1\)\s+" + self.fsk('x_crystal_irto_modes_value', 3) + "\s*$", adHoc=self.adHoc_x_crystal_irX_modes('to', 3, 1))
                                        ])
                                ])

        ])])])])
        matcher_vibrational_irto = SM( "^\s*H+\s*$", subMatchers=[
                SM( "^\s*EIGENVALUES \(EIGV\) OF THE MASS WEIGHTED HESSIAN MATRIX AND HARMONIC TRANSVERSE\s*$", subMatchers=[
                        SM( "^\s*OPTICAL \(TO\) FREQUENCIES\. IRREP LABELS REFER TO SYMMETRY REPRESENTATION\s*$", subMatchers=[
                                matcher_vibrational_irto2
        ])])])

        matcher_vibrational_irlo2 = SM( "^\s*MODES\s+EIGV\s+FREQUENCIES\s+IRREP\s+IR\s+INTENS\s+SHIFTS\s*$", subMatchers=[
                SM( "^\s*\(HARTREE\*\*2\)\s+\(CM\*\*-1\)\s+\(THZ\)\s+\(KM/MOL\)\s+\(CM\*\*-1\)\s+\(THZ\)\s*$", sections=['x_crystal_section_irlo'], subMatchers=[
                        SM( "^\s*(?P<x_crystal_irlo_mode_min>\d+)\s*-\s*(?P<x_crystal_irlo_mode_max>\d+)\s+" + self.fk('x_crystal_irlo_mode_eigv') + "\s+" +
                            self.fk('x_crystal_irlo_mode_frequency_cmp') + "\s+" + self.fk('x_crystal_irlo_mode_frequency_thz') + "\s*\(\s*(?P<x_crystal_irlo_mode_irrep>\S+)\s*\)\s*"
                            + self.fk('x_crystal_irlo_mode_intens') + "\s+" + self.fk('x_crystal_irlo_mode_shift_cmp') + "\s+" + self.fk('x_crystal_irlo_mode_shift_thz') + "\s*$",
                            sections=['x_crystal_section_irlo_mode'], repeats=True),
                        SM( "^\s*OVERLAP BETWEEN THE EIGENVECTORS OF LO AND TO MODES\.\s*$", subMatchers=[
                                SM( "^\s*ENTRIES ARE FRQS IN CM\*\*-1\s*$", subMatchers=[
                                        SM( "^\s*IRREP\s+Fu\s*$", subMatchers=[
                                                SM( "^\s*LO/TO(\s+" + self.regex_f + ")+\s*$", forwardMatch=True, adHoc=self.adHoc_x_crystal_irlo_overlap())
                                        ]),
                                        SM( "^\s*LO MODES FOR IRREP Fu\s*$", sections=['x_crystal_section_irlo_modes'], subMatchers=[
                                                SM( "^\s*FREQ\(CM\*\*-1\)\s+.*$", forwardMatch=True, repeats=True, subMatchers=[
                                                SM( "^\s*FREQ\(CM\*\*-1\)\s+" + self.fsk('x_crystal_irlo_modes_value', 6) + "\s*$", adHoc=self.adHoc_x_crystal_irX_modes('lo', 3, 2)),
                                                SM( "^\s*FREQ\(CM\*\*-1\)\s+" + self.fsk('x_crystal_irlo_modes_value', 3) + "\s*$", adHoc=self.adHoc_x_crystal_irX_modes('lo', 3, 1))
                                        ])

        ])])])])])

        matcher_vibrational_irlo = SM( "^\s*H+\s*$", subMatchers=[
                SM( "^\s*LONGITUDINAL OPTICAL \(LO\) PHONON CALCULATION REQUESTED\. IN THOSE CASES\s*$", subMatchers=[
                        SM( "^\s*WHERE LO-TO SPLITTING OCCURS, LO FREQUENCIES AND IR INTENSITIES ARE LISTED\.\s*$", subMatchers=[
                                matcher_vibrational_irlo2
        ])])])

        matcher_temperatures = SM( "^\s*VIBRATIONAL TEMPERATURES \(K\) \[MODE NUMBER;IRREP\]\s*$", sections=['x_crystal_section_vibrational_modes'], subMatchers=[
                SM( "^\s*TO MODES\s*$", adHoc=self.adHoc_x_crystal_vibrational_modes('to')),
                SM( "^\s*LO MODES\s*$", adHoc=self.adHoc_x_crystal_vibrational_modes('lo'))
        ])

        matcher_thermodynamic = SM( "^\s*HARMONIC VIBRATIONAL CONTRIBUTIONS TO THERMODYNAMIC FUNCTIONS AT GIVEN\s*$", subMatchers=[
                SM( "^\s*TEMPERATURE AND PRESSURE:\s*$", sections=['x_crystal_section_thermodynamic'], subMatchers=[
                        SM( "^\s*AU/CELL\s+EV/CELL\s+KJ/MOL\s*$", sections=['x_crystal_section_thermodynamic_contrib'], subFlags=SM.SubFlags.Unordered, subMatchers=[
                                SM( "^\s*EL\s*:\s*" + self.fk('x_crystal_thermodynamic_contrib_el_aucell') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_el_ev') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_el_kjmol') + "\s*$"),
                                SM( "^\s*E0\s*:\s*" + self.fk('x_crystal_thermodynamic_contrib_e0_aucell') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_e0_ev') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_e0_kjmol') + "\s*$"),
                                SM( "^\s*ET\s*:\s*" + self.fk('x_crystal_thermodynamic_contrib_et_aucell') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_et_ev') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_et_kjmol') + "\s*$"),
                                SM( "^\s*PV\s*:\s*" + self.fk('x_crystal_thermodynamic_contrib_pv_aucell') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_pv_ev') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_pv_kjmol') + "\s*$"),
                                SM( "^\s*TS\s*:\s*" + self.fk('x_crystal_thermodynamic_contrib_ts_aucell') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_ts_ev') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_ts_kjmol') + "\s*$"),
                                SM( "^\s*ET\+PV-TS\s*:\s*" + self.fk('x_crystal_thermodynamic_contrib_c1_aucell') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_c1_ev') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_c1_kjmol') + "\s*$"),
                                SM( "^\s*EL\+E0\+ET\+PV-TS\s*:\s*" + self.fk('x_crystal_thermodynamic_contrib_c2_aucell') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_c2_ev') + "\s+" + self.fk('x_crystal_thermodynamic_contrib_c2_kjmol') + "\s*$"),
                                SM( "^\s*AT\s*\(\s*T\s*=\s*" + self.fk('x_crystal_thermodynamic_contrib_temperature') + "\s*K\s*,\s*P\s*=\s*" + self.fk('x_crystal_thermodynamic_contrib_pressure') + "\s*MPA\s*\)\s*:\s*$")
                        ]),
                        SM( "^\s*OTHER THERMODYNAMIC FUNCTIONS:\s*$", subMatchers=[
                                SM( "^\s*mHARTREE/\(CELL\*K\)\s+mEV/\(CELL\*K\)\s+J/\(MOL\*K\)\s*", subMatchers=[
                                        SM( "^\s*ENTROPY\s*:\s*" + self.fk('x_crystal_thermodynamic_entropy_mhartree') + "\s+" + self.fk('x_crystal_thermodynamic_entropy_mev') + "\s+" + self.fk('x_crystal_thermodynamic_entropy_jmolk') + "\s*$"),
                                        SM( "^\s*HEAT CAPACITY\s*:\s*" + self.fk('x_crystal_thermodynamic_heatcapacity_mhartree') + "\s+" + self.fk('x_crystal_thermodynamic_heatcapacity_mev') + "\s+" + self.fk('x_crystal_thermodynamic_heatcapacity_jmolk') + "\s*$")
                        ])])
        ])])

        matcher_vibrational = SM( "^\s*\++\s*SYMMETRY ADAPTION OF VIBRATIONAL MODES\s*\++\s*$", subMatchers=[
                SM( "^\s*SYMMETRY INFORMATION:\s*$", subMatchers=[
                        SM( "^\s*K-LITTLE GROUP: CLASS TABLE, CHARACTER TABLE\.\s*$", subMatchers=[
                                SM( "^\s*IRREP-\(DIMENSION, NO\. IRREDUCIBLE SETS\)\s*$", subMatchers=[
                                        SM( "^\s*\(P, D, RP, RD, STAND FOR PAIRING, DOUBLING, REAL PAIRING AND REAL DOUBLING\s*$", subMatchers=[
                                                SM( "^\s*OF THE IRREPS \(SEE MANUAL\)\)\s*$", subMatchers=[
                                                        SM( "^\s*CLASS\s*\|\s*GROUP OPERATORS \(SEE SYMMOPS KEYWORD\)\s*$", subMatchers=[
                                                                SM( "^\s*-+\s*$", sections=['x_crystal_section_vibrational'], subMatchers=[
                                                                        matcher_vibrational2,
                                                                        matcher_vibrational3,
                                                                        matcher_vibrational4,
                                                                        matcher_vibrational5,
                                                                        matcher_vibrational6,
                                                                        matcher_vibrational7,
                                                                        matcher_vibrational8,
                                                                        matcher_vibrational9,
                                                                        matcher_vibrational_irto,
                                                                        matcher_vibrational_irlo,
                                                                        matcher_temperatures,
                                                                        matcher_thermodynamic
        ])])])])])])])])

        matcher_forces2 = SM( "^\s*ATOM\s+X\s+Y\s+Z\s*$", sections=['x_crystal_section_forces'], subMatchers=[
                SM( "^\s*(?P<x_crystal_forces_atom_label>\d+)\s+(?P<x_crystal_forces_atom_z>\d+)\s+" + self.fsk('x_crystal_forces_atom_value', 3) + "\s*$",
                    sections=['x_crystal_section_forces_atom'], adHoc=self.adHoc_x_crystal_forces_atom()),
                SM( "^\s*RESULTANT FORCE\s+" + self.fsk('x_crystal_forces_value', 3) + "\s*$", adHoc=self.adHoc_x_crystal_forces()),
                SM( "^\s*THERE ARE NO SYMMETRY ALLOWED DIRECTIONS\s*$", adHoc=self.adHoc_x_crystal_forces_symmetry_allowed_directions(0)),
                matcher_forcematrix,
                matcher_bornchargetensor,
                matcher_vibrational
        ])
        matcher_forces = SM( "^\s*\*\s*FORCE\s+CALCULATION\s*\*\s*$", subMatchers=[
                SM( "^\s*CARTESIAN FORCES IN HARTREE\/BOHR \(ANALYTICAL\)\s*$", subMatchers=[matcher_forces2])
        ])

        matcher_crystal = SM( "^\s*CRYSTAL\s+CALCULATION\s*$",
            subMatchers=[
                SM( "^\s*CRYSTAL\s+FAMILY\s*:\s*(?P<x_crystal_family>.*?\S.*?)\s*$"),
                SM( "^\s*CRYSTAL\s+CLASS\s+\(?\s*(?P<x_crystal_class_ref>.*?\S.*?)\s*\)?\s*:\s*(?P<x_crystal_class>.*?\S.*?)\s*$"),
                SM( "^\s*SPACE\s+GROUP\s+\(\s*(?P<x_crystal_spacegroup_class>\S.*?\S)\s*\)\s*:\s*(?P<x_crystal_spacegroup>.*?\S.*?)\s*$", adHoc=self.adHoc_x_crystal_spacegroup()),
                SM( "^\s*LATTICE\s+PARAMETERS\s+\(?\s*(?P<x_crystal_conventional_cell_units>.*?\S.*?)\s*\)?\s*\-\s*CONVENTIONAL\s+CELL\s*$",
                    subMatchers=[
                        SM( "^\s*A\s+B\s+C\s+ALPHA\s+BETA\s+GAMMA\s*$",
                            subFlags=SM.SubFlags.Unordered,
                            subMatchers=self.appendNumberMatchers([], 'x_crystal_conventional_cell', 'value', 6, 6)
                        ),
                    ]
                )
            ]
        )

        matcher_molecular = SM("^\s*MOLECULAR\s+CALCULATION\s*$", subMatchers=[
                SM( "\s*POINT\s+GROUP\s+N\.\s+" + self.dk('x_crystal_pointgroup_number') + "\s*:\s*" + self.dk('x_crystal_pointgroup_number2') + "\s*OR\s*(?P<x_crystal_pointgroup>[A-Z0-9][A-Z0-9 ]*[A-Z0-9])\s*$"),
                SM( "\s*CORRESPONDING SPACE GROUP\s*:\s*(?P<x_crystal_pointgroup_corresponding_spacegroup>[A-Z0-9][A-Z0-9 ]*[A-Z0-9])\s*$"),
        ])

        matcher_system = SM( "^\s*(?:(?:CRYSTAL|MOLECULAR|SLAB|POLYMER|HELIX|EXTERNAL|DLVINPUT)\s+CALCULATION)|(?: GEOMETRY INPUT FROM EXTERNAL FILE)",
            forwardMatch=True,
            sections=['section_system', 'x_crystal_section_conventional_cell'],
            subMatchers=[
                matcher_crystal,
                matcher_molecular,
                SM(" GEOMETRY INPUT FROM EXTERNAL FILE",
                    subMatchers=[
                        SM(" 1D - POLYMER", startReAction=self.action_push1D),
                    ]
                ),
                SM( "^\s*NUMBER\s+OF\s+IRREDUCIBLE\s+ATOMS\s+IN\s+THE\s+CONVENTIONAL\s+CELL\s*:\s*(?P<x_crystal_conventional_cell_number_of_atoms>\d+)\s*$",
                    subMatchers=[
                        SM( "^\s*INPUT COORDINATES\s*$",
                            subMatchers=[
                                SM( "^\s*ATOM\s+AT\.\s+N\.\s+COORDINATES\s*$",
                                    subFlags=SM.SubFlags.Unordered,
                                    subMatchers=self.appendNumberMatchers([],
                                    'x_crystal_conventional_cell', 'value', 3, 5)
                                )
                            ]
                        )
                    ]
                ),
                SM( "^\s*LATTICE\s+PARAMETERS\s+\(?\s*(?P<x_crystal_primitive_cell_units>.*?\S.*?)\s*\)?\s*\-\s*PRIMITIVE\s+CELL\s*$",
                    sections=['x_crystal_section_primitive_cell'],
                    subMatchers=[
                        SM( "^\s*A\s+B\s+C\s+ALPHA\s+BETA\s+GAMMA\s+VOLUME\s*$",
                            subFlags=SM.SubFlags.Unordered,
                            subMatchers=self.appendNumberMatchers([], 'x_crystal_primitive_cell', 'value', 7, 7)
                        )
                    ]
                ),
                SM( "^\s*COORDINATES\s+OF\s+THE\s+EQUIVALENT\s+ATOMS\s+\(\s*(?P<x_crystal_primitive_cell_units_atom>.*?\S.*?)\s*\)\s*$",
                    sections=['x_crystal_section_primitive_cell'],
                    subMatchers=[
                        SM( "^\s*N\.\s+ATOM\s+EQUIV\s+AT\.\s+N\.\s+X\s+Y\s+Z\s*$",
                            subFlags=SM.SubFlags.Unordered,
                            subMatchers=[
                                SM( ("^\s*(?P<x_crystal_primitive_cell_atom_number>\d+)\s+(?P<x_crystal_primitive_cell_atom_label>\d+)\s+(?P<x_crystal_primitive_cell_atom_number_of_equivalents>\d+)\s+" +
                                    "(?P<x_crystal_primitive_cell_atom_z>\d+)\s+(?P<x_crystal_primitive_cell_atom_element>\S+)\s+" +
                                    "(?P<x_crystal_primitive_cell_atom_value1>{0})\s+(?P<x_crystal_primitive_cell_atom_value2>{0})\s+(?P<x_crystal_primitive_cell_atom_value3>{0})\s*$").format(self.regex_f),
                                    sections=['x_crystal_section_primitive_cell_atom'],
                                    repeats=True,
                                    adHoc=self.adHoc_x_crystal_primitive_cell_atom(3))
                            ]
                        )
                    ]
                ),
                SM( " NUMBER OF SYMMETRY OPERATORS\s+:\s+(?P<x_crystal_number_of_symmops>\d+)",
                    subMatchers=[
                        SM( " GEOMETRY NOW FULLY CONSISTENT WITH THE GROUP",
                            fixedStartValues={"x_crystal_geometry_consistent": True}
                        )
                    ]
                ),
                # SM( "^\s*INFORMATION\s+\*+\s+INPFREQ\s+\*+\s+DIELECTRIC\s+TENSOR\s+INPUT\s*$",
                    # adHoc=self.adHoc_x_crystal_dielectric_tensor()
                # ),
                SM(re.escape("  * CELL ROTATION "),
                    subMatchers=[
                        SM(" DIRECT-LATTICE FUNDAMENTAL VECTORS"),
                        SM(" NEW FUNDAMENTAL DIRECT-LATTICE VECTORS B1,B2,B3"),
                        SM(" LATTICE PARAMETERS  \(ANGSTROM  AND DEGREES\)",
                            subMatchers=[
                                SM("        A           B           C        ALPHA        BETA       GAMMA")
                            ]
                        ),
                        SM(" NUMBER OF PRIMITIVE CELLS CONTAINED IN THE NEW FUNDAMENTAL CELL"),
                        SM(" NEW FUNDAMENTAL DIRECT-LATTICE VECTORS B1,B2,B3"),
                        SM(" VOLUME OF THE 3D CELL"),
                        SM(" AREA OF THE 2D CELL"),
                        SM(" B3 MODULUS"),
                        SM(" B3 Z PROJECTION"),
                        SM(" B3 X-Y PROJECTION"),
                        SM(" UNIT CELL ATOM COORDINATES :"),
                        SM(" ATOMS CLASSIFIED ACCORDING TO THE Z COORDINATE :"),
                        SM(" ATOMS CLASSIFIED ACCORDING TO THE Z COORDINATE :"),
                        SM(re.escape(" *************************** CELL ROTATION COMPLETE ***************************"))
                    ],
                ),
                SM(re.escape(" * TWO DIMENSIONAL SLAB PARALLEL TO THE SELECTED PLANE"),
                ),
                SM(re.escape(" ******************************* SLAB GENERATED *******************************"),
                    subMatchers=[
                        SM(" LATTICE PARAMETERS \(ANGSTROMS AND DEGREES\) - BOHR"),
                        SM(" PRIMITIVE CELL"),
                        SM("         A              B              C           ALPHA      BETA       GAMMA")
                    ]
                ),
                SM(" (?:COMBINED CELL\/ATOM OPTIMIZATION CONTROL)|(?:ATOMIC POSITIONS OPTIMIZATION CONTROL)",
                    subMatchers=[
                        SM( "INITIAL TRUST RADIUS\s+{0} MAXIMUM TRUST RADIUS\s+{0}".format(self.regexs.float)),
                        SM( "MAXIMUM GRADIENT COMPONENT\s+{0} MAXIMUM DISPLACEMENT COMPONENT\s+{0}".format(self.regexs.float)),
                        SM( "R.M.S. OF GRADIENT COMPONENT\s+{0} R.M.S. OF DISPLACEMENT COMPONENTS\s+{0}".format(self.regexs.float)),
                        SM( "THRESHOLD ON ENERGY CHANGE\s+{0} EXTRAPOLATING POLYNOMIAL ORDER\s+{1}".format(self.regexs.float, self.regexs.int)),
                        SM( "MAXIMUM ALLOWED NUMBER OF STEPS\s+{0} SORTING OF ENERGY POINTS:\s+{1}".format(self.regexs.float, self.regexs.word)),
                        SM( "ANALYTICAL  GRADIENT                 HESSIAN UPDATING\s+{}".format(self.regexs.float)),
                        SM( "STEP SIZE NUMERICAL GRADIENT\s+{}".format(self.regexs.float)),
                        SM( "INITIAL HESSIAN MATRIX:\s+{}".format(self.regexs.eol)),
                    ]
                ),
                SM( " ATOMS IN THE ASYMMETRIC UNIT\s+{0} - ATOMS IN THE UNIT CELL:\s+{0}".format(self.regexs.int)),
                SM( " GEOMETRY FOR WAVE FUNCTION - DIMENSIONALITY OF THE SYSTEM\s+(?P<x_crystal_dimensionality>\d)",
                    startReAction=self.transform_periodicity,
                    adHoc=self.adHoc_x_crystal_dimensionality,
                    subMatchers=[
                        SM( "\s*\(\s*NON PERIODIC DIRECTION: LATTICE PARAMETER FORMALLY SET TO\s*({})\s*\)".format(self.regexs.float),
                            startReAction=self.transform_nonperiodic_tag
                        ),
                    ]
                ),
                SM( "^\s*LATTICE PARAMETERS \(ANGSTROMS AND DEGREES\) \- BOHR \=\s*(?P<x_crystal_bohr_angstrom>{0})\s* ANGSTROM\s*$".format(self.regex_f),
                    forwardMatch=True,
                    adHoc=self.adHoc_bohr_angstrom(),
                ),
                SM( "^\s*PRIMITIVE\s+CELL\s*\-\s*CENTRING\s+CODE\s+(?P<x_crystal_centring_code_n>\d+)\s*/\s*(?P<x_crystal_centring_code_d>\d+)\s*VOLUME\s*\=\s*(?P<x_crystal_volume>{0})\s*\-\s*DENSITY\s*(?P<x_crystal_density>{0})\s*g/cm\^3\s*$".format(self.regex_f)),
                SM( "^\s*A\s+B\s+C\s+ALPHA\s+BETA\s+GAMMA\s*$",
                    adHoc=self.adHoc_lattice_parameters(),
                ),
                SM( " ATOMS IN THE ASYMMETRIC UNIT\s+{0} - ATOMS IN THE UNIT CELL:\s+{0}".format(self.regexs.int),
                    subMatchers=[
                        SM(re.escape("     ATOM          X(ANGSTROM)         Y(ANGSTROM)         Z(ANGSTROM)"),
                            subMatchers=[
                                SM(re.escape(" *******************************************************************************"),
                                    adHoc=self.adHoc_atom_positions2
                                )
                            ]
                        )
                    ]
                ),
                SM( "^\s*TRANSFORMATION MATRIX PRIMITIVE-CRYSTALLOGRAPHIC CELL\s*$", sections=['x_crystal_section_cell'], adHoc=self.adHoc_x_crystal_cell_transformation_matrix(),
                    subMatchers=[
                        SM( "^\s*CRYSTALLOGRAPHIC CELL\s*\(VOLUME\=\s*(?P<x_crystal_cell_volume>{0})\s*\)\s*$".format(self.regex_f)),
                        SM( "^\s*A\s+B\s+C\s+ALPHA\s+BETA\s+GAMMA\s*$", adHoc=self.adHoc_x_crystal_cell_parameters()),
                        SM( "^\s*COORDINATES IN THE CRYSTALLOGRAPHIC CELL\s*$", subMatchers=[
                            SM( ("^\s*(?P<x_crystal_cell_atom_label>\d+)\s+(?P<x_crystal_cell_atom_tag>\S+)\s+(?P<x_crystal_cell_atom_z>\d+)\s+(?P<x_crystal_cell_atom_element>\S+)\s+" +
                                "(?P<x_crystal_cell_atom_value1>{0})\s+(?P<x_crystal_cell_atom_value2>{0})\s+(?P<x_crystal_cell_atom_value3>{0})\s*$").format(self.regex_f),
                                sections=['x_crystal_section_cell_atom'], repeats=True)
                        ])
                ]),
                SM( "^\s*\*+\s*(?P<x_crystal_cell_number_of_symmops>\d+)\s*SYMMOPS\s*-\s*TRANSLATORS IN FRACTIONAL UNITS\s*$",
                    sections=['x_crystal_section_cell'],
                    subMatchers=[
                        SM( "^\s*\*+\s*MATRICES AND TRANSLATORS IN THE CRYSTALLOGRAPHIC REFERENCE FRAME\s*$",
                            subMatchers=[
                                SM( "^\s*V\s+INV\s+ROTATION MATRICES\s+TRANSLATORS$",
                                    subMatchers=[
                                        SM( "^\s*(?P<x_crystal_cell_symmop_id>\d+)\s+(?P<x_crystal_cell_symmop_inv>\d+)\s+" + self.fsk('x_crystal_cell_symmop_value', 12) + "\s*$",
                                            sections=['x_crystal_section_cell_symmop'],
                                            repeats=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                SM( "^\s*DIRECT LATTICE VECTORS CARTESIAN COMPONENTS \(ANGSTROM\)\s*$",
                    adHoc=self.adHoc_simulation_cell,
                ),
                SM( "^\s*CARTESIAN COORDINATES \- PRIMITIVE CELL\s*$",
                    subMatchers=[
                        SM(re.escape(" *******************************************************************************")),
                        SM(re.escape(" *      ATOM          X(ANGSTROM)         Y(ANGSTROM)         Z(ANGSTROM)")),
                        SM(re.escape(" *******************************************************************************"),
                            adHoc=self.adHoc_atom_positions,
                        )
                    ]
                ),
                SM( " LOCAL ATOMIC FUNCTIONS BASIS SET", subMatchers=[
                        SM( re.escape("   ATOM   X(AU)   Y(AU)   Z(AU)  N. TYPE  EXPONENT  S COEF   P COEF   D/F/G COEF"),
                            sections=['x_crystal_section_basis_set'],
                            subMatchers=[
                                SM( "^\s*(?P<x_crystal_basis_set_atom_label>\d+)\s+(?P<x_crystal_basis_set_atom_element>\S+)\s*" + self.fsk('x_crystal_basis_set_atom_value', 3) + "\s*$",
                                    sections=['x_crystal_section_basis_set_atom'], repeats=True,
                                    subMatchers=[
                                        SM( "^\s*(?P<x_crystal_basis_set_atom_shell_omin>\d+)\s*(?P<x_crystal_basis_set_atom_shell_type>\S+)\s*$",
                                            sections=['x_crystal_section_basis_set_atom_shell'],
                                            repeats=False,
                                            startReAction=self.transform_basis_set_shell,
                                            subMatchers=[
                                                SM( regex_gaussian_primitive,
                                                    repeats=True,
                                                    sections=['x_crystal_section_basis_set_atom_shell_primitive'])
                                            ]
                                        ),
                                        SM( "^\s*(?P<x_crystal_basis_set_atom_shell_omin>\d+)\s*-\s*(?P<x_crystal_basis_set_atom_shell_omax>\d+)\s*(?P<x_crystal_basis_set_atom_shell_type>\S+)\s*$",
                                            sections=['x_crystal_section_basis_set_atom_shell'],
                                            startReAction=self.transform_basis_set_shell,
                                            repeats=True,
                                            subMatchers=[
                                                SM( regex_gaussian_primitive,
                                                    repeats=True,
                                                    sections=['x_crystal_section_basis_set_atom_shell_primitive'])
                                            ]
                                        )
                                ])
                        ]),
                        matcher_info
                ]),
                matcher_kpoints,
                matcher_lattice,
                matcher_infoeigen,
                matcher_neighbors,
                matcher_frequency,
                SM( "^\s*ATOMIC WAVEFUNCTION\(S\)\s*$",
                    sections=["section_single_configuration_calculation"],
                    subMatchers=[
                        matcher_wavefunctions,
                        matcher_scf_dft,
                        matcher_forces
                ])
        ])

        matcher_bands_line = SM( "^\s*" + self.dk('x_crystal_bands_line_point_number') + "\s*" + self.dkspecial('x_crystal_bands_line_point_integer', 3, 3) + "\s*$",
            repeats=True, sections=['x_crystal_section_bands_line_point'], adHoc=self.adHoc_x_crystal_bands_line_point(3))

        matcher_bands = SM( "^\s*\*+\s*$", subMatchers=[
                SM( "^\s*\*\s+BAND STRUCTURE\s+\*\s*$", sections=['x_crystal_section_bands'], subMatchers=[
                        SM( "^\s*\*\s*" + self.wk('x_crystal_bands_title') + "\s*\*\s*$", subMatchers=[
                                SM( "^\s*\*\s+FROM BAND\s*" + self.dk('x_crystal_bands_min') + "\s+TO BAND\s*" + self.dk('x_crystal_bands_max') + "\s+\*\s*$"),
                                SM( "^\s*\*\s+TOTAL OF\s*" + self.dk('x_crystal_bands_number_of_points') + "\s+K-POINTS ALONG THE PATH\s+\*\s*$"),
                                SM( "^\s*LINE\s*" + self.dk('x_crystal_bands_line_number') + "\s*\(\s*" + self.fsk('x_crystal_bands_line_value1', 3) + "\s*:\s*" + self.fsk('x_crystal_bands_line_value2', 3)
                                    + "\s*\)\s*IN TERMS OF PRIMITIVE LATTICE VECTORS\s*$",
                                    repeats=True, sections=['x_crystal_section_bands_line'], adHoc=self.adHoc_x_crystal_bands_line_coordinates('primitive', 3), subMatchers=[
                                        SM( "^\s*" + self.dk('x_crystal_bands_line_number_of_points') + "\s+POINTS - SHRINKING_FACTOR\s*" + self.dk('x_crystal_bands_line_shrink') + "\s*$"),
                                        SM( "^\s*CARTESIAN COORD\.\s*\(\s*" + self.fsk('x_crystal_bands_line_value1', 3) + "\s*\)\s*:\s*\(\s*" + self.fsk('x_crystal_bands_line_value2', 3)
                                            + "\s*\)\s*STEP\s*" + self.fk('x_crystal_bands_line_step') + "\s*$", adHoc=self.adHoc_x_crystal_bands_line_coordinates('cartesian', 3), subMatchers=[matcher_bands_line])
                        ])]),
                        SM( "^\s*ENERGY RANGE \(A\.U\.\)\s*" + self.fk('x_crystal_bands_energy_min') + "\s+-\s+" + self.fk('x_crystal_bands_energy_max') + "\s+EFERMI\s+" + self.fk('x_crystal_bands_energy_fermi') + "\s*$"),
                        SM( "^\s*CAPPA\s*:\s*IS1\s+" + self.dk('x_crystal_bands_is1') + "\s*;\s*IS2\s+" + self.dk('x_crystal_bands_is2') + "\s*;\s*IS3\s+" + self.dk('x_crystal_bands_is3')
                            + "\s*;\s*K PTS MONK NET\s+" + self.dk('x_crystal_bands_k_pts_monk_net') + "\s*;\s*SYMMOPS\s*:\s*K SPACE\s+" + self.dk('x_crystal_bands_symmops_k')
                            + "\s*;\s*G SPACE\s+" + self.dk('x_crystal_bands_symmops_g') + "\s*$"),
                        SM( "^\s*T+\s+BAND\s+TELAPSE\s+" + self.fk('x_crystal_bands_telapse') + "\s+TCPU\s+" + self.fk('x_crystal_bands_tcpu') + "\s*$")
                ]),
        ])

        matcher_properties_info1 = SM( "^\s*[A-Z\. ]+\s+\d+\s+[A-Z\. ]+.*?\d+\s*$", forwardMatch=True, repeats=True, subFlags=SM.SubFlags.Unordered, subMatchers=[
                SM( "^\s*N\. OF ATOMS PER CELL\s+(?P<x_crystal_properties_number_of_atoms>\d+)\s+.*$", forwardMatch=True),
                SM( "^\s*NUMBER OF SHELLS\s+(?P<x_crystal_properties_number_of_shells>\d+)\s+.*$", forwardMatch=True),
                SM( "^\s*NUMBER OF AO\s+(?P<x_crystal_properties_number_of_orbitals>\d+)\s+.*$", forwardMatch=True),
                SM( "^\s*N\. OF ELECTRONS PER CELL\s+(?P<x_crystal_properties_number_of_electrons>\d+)\s+.*$", forwardMatch=True),
                SM( "^\s*CORE ELECTRONS PER CELL\s+(?P<x_crystal_properties_number_of_core_electrons>\d+)\s+.*$", forwardMatch=True),
                SM( "^\sN\. OF SYMMETRY OPERATORS\s+(?P<x_crystal_properties_number_of_symmops>\d+)\s+.*$", forwardMatch=True),
                SM( "^.*COULOMB OVERLAP TOL\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_properties_tol_coulomb_overlap>{})\s*$".format(self.regex_f)),
                SM( "^.*COULOMB PENETRATION TOL\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_properties_tol_coulomb_penetration>{})\s*$".format(self.regex_f)),
                SM( "^.*EXCHANGE OVERLAP TOL\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_properties_tol_exchange_overlap>{})\s*$".format(self.regex_f)),
                SM( "^.*EXCHANGE PSEUDO OVP \(F\(G\)\)\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_properties_tol_pseudo_overlap_f>{})\s*$".format(self.regex_f)),
                SM( "^.*EXCHANGE PSEUDO OVP \(P\(G\)\)\s*\(T\d+\)\s+10\*\*\s*(?P<x_crystal_properties_tol_pseudo_overlap_p>{})\s*$".format(self.regex_f)),
                SM( "^.*POLE ORDER IN MONO ZONE\s*(?P<x_crystal_properties_pole_order>\d+)\s*$"),
                SM( "^\s*[A-Z\. ]+\s+\d+\s+[A-Z\. ]+.*?\d+\s*$")
        ])

        matcher_restart_kpoints = SM( "^\s*\*+\s*K POINTS COORDINATES \(OBLIQUE COORDINATES IN UNITS OF IS\s*=\s*(?P<x_crystal_restart_kpoints_is_units>\d+)\s*\)\s*$",
            sections=['x_crystal_section_restart_kpoints'], adHoc=self.adHoc_x_crystal_kpoints('restart_kpoint')
        )
        matcher_restart_dos = SM( "^\s*\*+\s*INTEGRATED DENSITIES IN THE ENERGY INTERVAL PER PROJECTION AND TOTAL\s*$", sections=['x_crystal_section_restart_dos'], subMatchers=[
                SM( "^\s*T\s*$", subMatchers=[
                        SM( "^\s*" + self.fk('x_crystal_restart_dos_scale_t') + "\s*$", adHoc=self.adHoc_x_crystal_restart_dos_scale(), subMatchers=[
                                SM( "^\s\*+\s+ENERGY\s+TOTAL DENSITY OF STATES\s*-\s*FULL SCALE\s*=\s*" + self.fk('x_crystal_restart_dos_scale_full') + "\s*AU\s*$", subMatchers=[
                                        SM( "^\s*" + self.fk('x_crystal_restart_dos_energy_energy') + "\s*(?P<x_crystal_restart_dos_energy_text>\|? *T)\s*$",
                                            sections=['x_crystal_section_restart_dos_energy'], adHoc=self.adHoc_x_crystal_restart_dos_energy_dos(), repeats=True)
                ])])]),
                SM( "^\s*T+\s+DOSS\s+TELAPSE\s+" + self.fk('x_crystal_restart_dos_telapse') + "\s+TCPU\s+" + self.fk('x_crystal_restart_dos_tcpu') + "\s*$")
        ])
        matcher_restart_end = SM( "^\s*ENDPROP\s*$", subMatchers=[
                SM( "^\s*T+\s+END\s+TELAPSE\s+" + self.fk('x_crystal_restart_end_telapse') + "\s+TCPU\s+" + self.fk('x_crystal_restart_end_tcpu') + "\s*$"),
                SM( "^\s*E+\s+TERMINATION\s+DATE\s+(?P<x_crystal_restart_end_date>\d{2} \d{2} \d{4})\s+TIME\s+(?P<x_crystal_restart_end_time>\d{2}:\d{2}:\d{2}\.\d+)\s*$")
        ])
        matcher_restart = SM( "^\s*RESTART WITH NEW K POINTS NET\s*", sections=['x_crystal_section_restart'], subMatchers=[
                SM( "^\s*\*+\s*$", endReStr="^\s*\*+\s*$", subMatchers=[
                        SM( "^.*?[A-Z]+.*?$", repeats=True, forwardMatch=True, subMatchers=[
                                SM( "^.*?POINTS IN THE IBZ\s+" + self.dk('x_crystal_restart_points_ibz') + ".*?$", forwardMatch=True),
                                SM( "^.*POINTS\(GILAT NET\)\s+" + self.dk('x_crystal_restart_points_gilat') + ".*?$", forwardMatch=True),
                                SM( "^.*SHRINK FACTORS\(MONK\.\)\s+" + self.dsk('x_crystal_restart_integer', 3) + ".*?$", forwardMatch=True, adHoc=self.adHoc_x_crystal_restart_shrink_monkh(3)),
                                SM( "^.*SHRINK FACTOR\(GILAT\)\s+" + self.dk('x_crystal_restart_shrink_gilat') + ".*?$", forwardMatch=True),
                                SM( "^.*?[A-Z]+.*?$")
                        ])
                ]),
                matcher_restart_kpoints,
                SM( "^\s*FERMI ENERGY AND DENSITY MATRIX CALCULATION ON COMPUTED EIGENVECTORS\s*$", subMatchers=[
                        SM( "^\s*DENSITY MATRIX AT SCF CYCLE\s*\(\s*" + self.dk('x_crystal_restart_density_matrix_cycle') + "\s*\+\s*" + self.dk('x_crystal_restart_density_matrix_cycleplus') + "\s*\)\s*$")
                ]),
                SM( "^\s*INSULATING STATE\s*$", adHoc=self.adHoc_x_crystal_restart_insulating(), subMatchers=[
                        SM( "^\s*TOP OF VALENCE BANDS\s*-\s*BAND\s+" + self.dk('x_crystal_restart_top_of_valence_b') + "\s*;\s*K\s+" + self.dk('x_crystal_restart_top_of_valence_k') + "\s*;\s*EIG\s+"
                            + self.fk('x_crystal_restart_top_of_valence_energy') + "\s+AU\s*$"),
                        SM( "^\s*BOTTOM OF VIRTUAL BANDS\s*-\s*BAND\s+" + self.dk('x_crystal_restart_bottom_of_virtual_b') + "\s*;\s*K\s+" + self.dk('x_crystal_restart_bottom_of_virtual_k') + "\s*;\s*EIG\s+"
                            + self.fk('x_crystal_restart_bottom_of_virtual_energy') + "\s+AU\s*$")
                ]),
                SM( "^\s*CORE DENSITY MATRIX CALCULATION\s*$", subMatchers=[
                        SM( "^\s*T+\s+NEWK\s+TELAPSE\s+" + self.fk('x_crystal_restart_telapse') + "\s+TCPU\s+" + self.fk('x_crystal_restart_tcpu') + "\s*$")
                ]),
                SM( "^\s*TOTAL AND PROJECTED DENSITY OF STATES - FOURIER LEGENDRE METHOD\s*$", subMatchers=[
                        SM( "^\s*FROM BAND\s*" + self.dk('x_crystal_restart_fl_band_min') + "\s+TO BAND\s*" + self.dk('x_crystal_restart_fl_band_max') + "\s+ENERGY RANGE\s*"
                            + self.fk('x_crystal_restart_fl_energy_min') + "\s*" + self.fk('x_crystal_restart_fl_energy_max') + "\s*$")
                ]),
                SM( "\s*NUMBER OF LEGENDRE POLYNOMIALS\s*" + self.dk('x_crystal_restart_number_of_lpols') + "\s*$"),
                SM( "\s*NUMBER OF SYMMETRIZED PWS FOR EXPANSION\s*" + self.dk('x_crystal_restart_number_of_sympws') + "\s*"),
                SM( "\s*NUMBER OF K POINTS OF SECONDARY NET\s*" + self.dk('x_crystal_restart_number_of_kpsn') + "\s*$"),
                SM( "\s*NUMBER OF PROJECTIONS\s*" + self.dk('x_crystal_restart_number_of_projections') + "\s*$"),
                SM( "\s*NUMBER OF ENERGY POINTS\s*" + self.dk('x_crystal_restart_number_of_epoints') + "\s*$"),
                SM( "\s*BAND\s+INTEGRATED DOSS PER PROJECTION AND TOTAL\s*$", subMatchers=[
                        SM( "^\s*" + self.dk('x_crystal_restart_band_number') + "\s+" + self.fk('x_crystal_restart_band_doss_per') + "\s*$", sections=['x_crystal_section_restart_band'], repeats=True)
                ]),
                matcher_restart_dos,
                matcher_restart_end
        ])
        matcher_properties_info2 = SM( "^\s*\*+\s*$", subMatchers=[
                SM( "^\s*ATOM\s+N\.\s*AT\.\s+SHELL\s+X\(A\)\s+Y\(A\)\s+Z\(A\)\s+EXAD\s+N\.\s*ELECT\.\s*$", subMatchers=[
                        SM( "^\s*\*+\s*$", subMatchers=[
                                SM( "^\s*" + self.fk('x_crystal_properties_atom_label') + "\s+" + self.fk('x_crystal_properties_atom_z') + "\s+(?P<x_crystal_properties_atom_element>\S+)\s+"
                                    + self.fk('x_crystal_properties_atom_shell') + "\s+" + self.fsk('x_crystal_properties_atom_value', 3) + "\s+" + self.fk('x_crystal_properties_atom_exad')
                                    + "\s+" + self.fk('x_crystal_properties_atom_number_of_electrons') + "\s*$", sections=['x_crystal_section_properties_atom'], repeats=True)
                ])]),
                SM( "^\s*\*+\s*$", endReStr="^\s*\*+\s*$", subMatchers=[
                        SM( "^.*?[A-Z]+.*?$", repeats=True, forwardMatch=True, subMatchers=[
                                SM( "^.*?DE\(K\)\s+" + self.fk('x_crystal_properties_dek') + ".*?$", forwardMatch=True),
                                SM( "^.*?TOTAL ENERGY\s+" + self.fk('x_crystal_properties_total_energy') + ".*?$", forwardMatch=True),
                                SM( "^.*?KIN\. ENERGY\s+" + self.fk('x_crystal_properties_kinetic_energy') + ".*?$", forwardMatch=True),
                                SM( "^.*?N\. OF SCF CYCLES\s+" + self.dk('x_crystal_properties_number_of_scf_cycles') + ".*?$", forwardMatch=True),
                                SM( "^.*?WEIGHT OF F\(I\) IN F\(I\+1\)\s+" + self.fk('x_crystal_properties_weight_f') + ".*?$", forwardMatch=True),
                                SM( "^.*?SHRINK\.\s*FACT\.\s*\(MONKH\.\)\s+" + self.dsk('x_crystal_properties_integer', 3) + ".*?$", forwardMatch=True, adHoc=self.adHoc_x_crystal_properties_shrink_monkh(3)),
                                SM( "^.*?NUMBER OF K POINTS IN THE IBZ\s+" + self.dk('x_crystal_properties_number_of_k_points_ibz') + ".*?$", forwardMatch=True),
                                SM( "^.*?ENERGY LEVEL SHIFTING\s+" + self.fk('x_crystal_properties_energy_level_shifting') + ".*?$", forwardMatch=True),
                                SM( "^.*?CONVERGENCE ON ENER\s+" + self.fk('x_crystal_properties_convergence') + ".*?$", forwardMatch=True),
                                SM( "^.*?VIR\. COEFF\.\s+" + self.fk('x_crystal_properties_virial_coefficient') + ".*?$", forwardMatch=True),
                                SM( "^.*?FERMI ENERGY\s+" + self.fk('x_crystal_properties_fermi_energy') + ".*?$", forwardMatch=True),
                                SM( "^.*?SHRINKING FACTOR\(GILAT NET\)\s+" + self.dk('x_crystal_properties_shrink_gilat') + ".*?$", forwardMatch=True),
                                SM( "^.*?CELL VOLUME \(A\.U\.\)\s+" + self.fk('x_crystal_properties_cell_volume') + ".*?$", forwardMatch=True),
                                SM( "^.*?[A-Z]+.*?$")
                        ])
                ]),
                SM( "^\s*GCALCO - MAX INDICES DIRECT LATTICE VECTOR\s*" + self.dsk('x_crystal_properties_integer', 3) + "\s*$", adHoc=self.adHoc_x_crystal_properties_gcalco(3)),
                SM( "^\s*NO\.OF VECTORS CREATED\s+" + self.dk('x_crystal_properties_number_of_vectors') + "\s+STARS\s+" + self.dk('x_crystal_properties_stars') + "\s+RMAX\s+" + self.fk('x_crystal_properties_rmax_bohr') + "\s+BOHR\s*$"),
                SM( "^\s*MATRIX SIZE: P\(G\)\s*" + self.dk('x_crystal_properties_matrix_size_p') + "\s*,\s*F\(G\)\s*" + self.dk('x_crystal_properties_matrix_size_f')
                    + "\s*,\s*P\(G\) IRR\s+" + self.dk('x_crystal_properties_irr_p') + "\s*,\s*F\(G\) IRR\s+" + self.dk('x_crystal_properties_irr_f') + "\s*$"),
                SM( "^\s*MAX G-VECTOR INDEX FOR 1- AND 2-ELECTRON INTEGRALS\s+" + self.dk('x_crystal_properties_max_gvector_index') + "\s*$"),
                SM( "^\s*CAPPA:IS1\s+" + self.dk('x_crystal_properties_cappa_is1') + "\s*;\s*IS2\s+" + self.dk('x_crystal_properties_cappa_is2') + "\s*;\s*IS3\s+" + self.dk('x_crystal_properties_cappa_is3')
                    + "\s*;\s*K PTS MONK NET\s+" + self.dk('x_crystal_properties_k_pts_monk_net') + "\s*;\s*SYMMOPS\s*:\s*K SPACE\s+" + self.dk('x_crystal_properties_symmops_k') + "\s*;\s*G SPACE\s+"
                    + self.dk('x_crystal_properties_symmops_g') + "\s*$"),
                SM( "\s*WARNING\s*\*+\s*" + self.wk('x_crystal_properties_warning_key') + "\s+\*+\s+" + self.wk('x_crystal_properties_warning_text') + "\s*$", repeats=True, sections=['x_crystal_section_properties_warning']),
                matcher_bands,
                matcher_restart
        ])

        matcher_properties = SM( "^\s*properties input data in\s*(?P<x_crystal_properties_input_file>.*?)\s*$", sections=['x_crystal_section_properties'], subMatchers=[
                SM( "^\s+\w+\s+STARTING\s+DATE\s+(?P<x_crystal_properties_start_date>\d{2} \d{2} \d{4}) TIME (?P<x_crystal_properties_start_time>\d{2}:\d{2}:\d{2}(\.\d+)?)\s*$", subMatchers=[
                        SM( "^\s*\*+\s*$", subMatchers=[
                                SM( "^\s*(?P<x_crystal_properties_title>.*?)\s*$", subMatchers=[
                                        SM( "^\s*CRYSTAL - PROPERTIES - TYPE OF CALCULATION\s*:\s*(?P<x_crystal_properties_type>.*?)\s*$", subMatchers=[
                                                SM( "^\s*\*+\s*$", subMatchers=[
                                                        SM( "^\s*(?P<x_crystal_properties_type2>.*?)\s*$")
                                        ])]),
                                        SM( "^\s*DIRECT LATTICE VECTOR COMPONENTS\s*\(ANGSTROM\)\s*$", sections=['x_crystal_section_properties_lattice'], adHoc=self.adHoc_x_crystal_properties_lattice(), subMatchers=[
                                                SM( "^\s*LATTICE PARAMETERS\s*\(ANGSTROM AND DEGREES\)\s*-\s*PRIMITIVE CELL\s*$", subMatchers=[
                                                        SM( "^\s*A\s+B\s+C\s+ALPHA\s+BETA\s+GAMMA\s+VOLUME\s*$", subMatchers=[
                                                                SM( "^\s*" + self.fsk('x_crystal_properties_lattice_value', 7) + "\s*$", adHoc=self.adHoc_x_crystal_properties_lattice_parameters(7))
                                        ])])]),
                                        SM( "^\s*\*+\s$", subMatchers=[matcher_properties_info1]),
                                        matcher_properties_info2
        ])])])])

        # For some reason the fixedStartValues of the root_matcher are not
        # handled, so we create a dummy root.
        self.root_matcher = SM("",
            forwardMatch=True,
            subMatchers=[
                SM("",
                    name="root",
                    sections=[
                        "section_run",
                        "section_method"
                    ],
                    fixedStartValues={
                        "program_name": "Crystal",
                        "electronic_structure_method": "DFT",
                        "program_basis_set_type": "gaussians",
                    },
                    forwardMatch=True,
                    subMatchers=[
                        matcher_process,
                        matcher_input,
                        matcher_header,
                        matcher_start,
                        matcher_system,
                        matcher_end,
                        matcher_properties
                    ]
                )
            ]
        )

    def fs(self, n):
        arr = []
        for i in range(0, n):
            arr.append("(" + self.regex_f + ")")
        return "\s+".join(arr)

    def fk(self, keyword):
        return "(?P<" + keyword + ">" + self.regex_f + ")"

    def fsk(self, key, n):
        arr = []
        for i in range(1, n+1):
            keyword = key + str(i)
            arr.append("(?P<" + keyword + ">" + self.regex_f + ")")
            self.caching_levels.update({keyword: CachingLevel.Cache})
        return "\s+".join(arr)

    def ds(self, n):
        arr = []
        for i in range(0, n):
            arr.append("(" + self.regex_i + ")")
        return "\s+".join(arr)

    def dk(self, keyword):
        return "(?P<" + keyword + ">" + self.regex_i + ")"

    def dsk(self, key, n):
        arr = []
        for i in range(1, n+1):
            keyword = key + str(i)
            arr.append("(?P<" + keyword + ">" + self.regex_i + ")")
            self.caching_levels.update({keyword: CachingLevel.Cache})
        return "\s+".join(arr)

    def ws(self, n):
        arr = []
        for i in range(0, n):
            arr.append("(" + self.regex_s + ")")
        return "\s+".join(arr)

    def wk(self, keyword):
        return "(?P<" + keyword + ">" + self.regex_s + ")"

    def wsk(self, key, n):
        arr = []
        for i in range(1, n+1):
            keyword = key + str(i)
            arr.append("(?P<" + keyword + ">" + self.regex_s + ")")
            self.caching_levels.update({keyword: CachingLevel.Cache})
        return "\s+".join(arr)

    def dkspecial(self, key, digits, n):
        ret = '\('
        for i in range(0, n):
            key1 = key + str(i*2+1)
            key2 = key + str(i*2+2)
            ret += '(?P<' + key1 + '>[0-9 ]{' + str(digits) + '})'
            ret += '/'
            ret += '(?P<' + key2 + '>[0-9 ]{' + str(digits) + '})'
            self.caching_levels.update({key1: CachingLevel.Cache, key2: CachingLevel.Cache})
        ret += '\)'
        return ret

    def storeElementNumber(self, symbol, z):
        self.element_numbers[symbol] = z
        return

    def getElementNumber(self, symbol):
        number = self.element_numbers.get(symbol)
        if number is None:
            return 0
        return number

    def appendNumberMatchers(self, subMatchers, sname, key, n_min, n_max):
        regexes = []
        attrname = "adHoc_" + sname
        attrobject = getattr(self, attrname)
        if attrobject is None:
            raise Exception("No such function" + attname)
        for i in range(1, n_max+1):
            keyword = sname + '_' + key + str(i)
            self.caching_levels.update({keyword: CachingLevel.Cache})
            regexes.append("(?P<" + keyword + ">{0})")
            if i >= n_min:
                regex_str = ("^\s*" + "\s+".join(regexes) + "\s*$").format(self.regex_f)
                subMatchers.append(SM(regex_str, repeats=True, adHoc=attrobject(i)))
        return subMatchers

    def getSection(self, parser):
        i = 0
        n = len(parser.context) - 1
        while n >= 0:
            ctx = parser.context[n]
            items = ctx.sections.items()
            lastitem = None
            for item in items:
                lastitem = item
            if lastitem is not None and len(lastitem) > 0:
                name, gIndex = lastitem
                os = parser.backend.sectionManagers[name].openSections
                return [os[gIndex], name]
            n = n-1
        return [None, None]

    def getKey(self, sectionname, key):
        sectionname = self.regex_csectionname.match(sectionname)
        if sectionname is None:
            return key
        sectionname = str(sectionname.group(1))
        return 'x_crystal_' + sectionname + '_' + key

    def getAdHocValues(self, parser, key, n):
        section, sectionname = self.getSection(parser)
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
        section, sectionname = self.getSection(parser)
        if section is None:
            return None
        key = self.getKey(sectionname, key)
        data = section[key]
        if data is not None:
            data = data[len(data)-1]
        return data

    def getAdHocValueFullName(self, parser, key):
        section, sectionname = self.getSection(parser)
        if section is None:
            return None
        data = section[key]
        if data is not None:
            data = data[len(data)-1]
        return data

    def inputFails(self, comment=""):
        raise Exception("inputFails state=" + str(self.input_state) + " substate=" + str(self.input_substate) + " comment=" + str(comment))
        self.input_state = -1
        return

    def getValues(self, section, key, min, max):
        ret = []
        for i in range(min, max+1):
            v = section[key + str(i)]
            if v is None or len(v) < 1:
                return None
            ret.append(v[len(v)-1])
        return np.array(ret)

    #===========================================================================
    # The functions that trigger when sections are closed
    def onClose_x_crystal_section_prim_atom(self, backend, gIndex, section):
        v1 = section.get_latest_value('x_crystal_prim_atom_value1')
        v2 = section.get_latest_value('x_crystal_prim_atom_value2')
        v3 = section.get_latest_value('x_crystal_prim_atom_value3')
        backend.addArrayValues('x_crystal_prim_atom_coordinates', np.array([v1, v2, v3]))
        tag = section.get_latest_value('x_crystal_prim_atom_tag')
        if tag == 'T':
            backend.addValue('x_crystal_prim_atom_in_asymmetric', True)
        else:
            backend.addValue('x_crystal_prim_atom_in_asymmetric', False)
        return

    def onClose_x_crystal_section_cell_atom(self, backend, gIndex, section):
        v1 = section.get_latest_value('x_crystal_cell_atom_value1')
        v2 = section.get_latest_value('x_crystal_cell_atom_value2')
        v3 = section.get_latest_value('x_crystal_cell_atom_value3')
        backend.addArrayValues('x_crystal_cell_atom_coordinates', np.array([v1, v2, v3]))
        tag = section.get_latest_value('x_crystal_cell_atom_tag')
        if tag == 'T':
            backend.addValue('x_crystal_cell_atom_in_asymmetric', True)
        else:
            backend.addValue('x_crystal_cell_atom_in_asymmetric', False)
        elem = section.get_latest_value('x_crystal_cell_atom_element')
        if elem is not None:
            elem_z = section.get_latest_value('x_crystal_cell_atom_z')
            self.storeElementNumber(elem, elem_z)
        return

    def onClose_x_crystal_section_cell_symmop(self, backend, gIndex, section):
        backend.addArrayValues('x_crystal_cell_symmop_rotation', np.reshape(self.getValues(section, 'x_crystal_cell_symmop_value', 1, 9), [3, 3]))
        backend.addArrayValues('x_crystal_cell_symmop_translation', self.getValues(section, 'x_crystal_cell_symmop_value', 10, 12))
        return

    def onClose_x_crystal_section_basis_set_atom(self, backend, gIndex, section):
        backend.closeSection('section_gaussian_basis_group', self.method['gIndex_gaussian_basis_group'])
        backend.closeSection('section_basis_set_atom_centered', self.method['gIndex_basis_set_atom_centered'])
        gg = []
        for i in range(1, 4):
            gg.append(section.get_latest_value('x_crystal_basis_set_atom_value' + str(i)))
        backend.addArrayValues('x_crystal_basis_set_atom_coordinates', np.array(gg))

        gIndex = backend.openSection('section_method_atom_kind')
        elem = section.get_latest_value('x_crystal_basis_set_atom_element')
        backend.addValue('method_atom_kind_label', asElementSymbol(elem))

        # If the element is not found, it is a ghost atom and should have
        # number 0 as specified in the metainfo
        try:
            number = get_atom_number(elem.capitalize())
        except KeyError:
            number = 0

        backend.addValue('method_atom_kind_atom_number', number)
        backend.closeSection('section_method_atom_kind', gIndex)
        return

    def onClose_x_crystal_section_basis_set_atom_shell(self, backend, gIndex, section):
        omax = section.get_latest_value('x_crystal_basis_set_atom_shell_omax')
        exponents = self.method['gaussian_exponents']
        contractions = self.method['gaussian_contractions']
        shell_type = self.method['gaussian_shell']

        if omax is None:
            omin = section.get_latest_value('x_crystal_basis_set_atom_shell_omin')
            if omin is not None:
                backend.addValue('x_crystal_basis_set_atom_shell_omax', omin)
        gIndex = backend.openSection('section_gaussian_basis_group')

        if shell_type is not None:
            lvalues = None
            if shell_type == 'S':
                lvalues = [0]
            elif shell_type == 'SP':
                lvalues = [0, 1]
            elif shell_type == 'P':
                lvalues = [1]
            elif shell_type == 'D':
                lvalues = [2]
            elif shell_type == 'F':
                lvalues = [3]
            elif shell_type == 'G':
                lvalues = [4]
            if lvalues is not None:
                backend.addArrayValues('gaussian_basis_group_ls', np.array(lvalues))
                backend.addValue('number_of_gaussian_basis_group_contractions', len(lvalues))

        if exponents is not None:
            backend.addValue('number_of_gaussian_basis_group_exponents', len(exponents))
            backend.addArrayValues('gaussian_basis_group_exponents', flt(exponents))

        if contractions is not None and len(contractions) != 0:
            backend.addArrayValues('gaussian_basis_group_contractions', flt2(contractions))

        backend.closeSection('section_gaussian_basis_group', gIndex)
        return

    def onClose_x_crystal_section_basis_set_atom_shell_primitive(self, backend, gIndex, section):
        self.method['gaussian_exponents'].append(section.get_latest_value('x_crystal_basis_set_atom_shell_primitive_exp'))
        type = self.method['gaussian_shell']
        if type == 'S':
            self.method['gaussian_contractions'].append([section.get_latest_value('x_crystal_basis_set_atom_shell_primitive_coeff_s')])
        elif type == 'P':
            self.method['gaussian_contractions'].append([section.get_latest_value('x_crystal_basis_set_atom_shell_primitive_coeff_p')])
        elif type == 'SP':
            self.method['gaussian_contractions'].append([
                    section.get_latest_value('x_crystal_basis_set_atom_shell_primitive_coeff_s'),
                    section.get_latest_value('x_crystal_basis_set_atom_shell_primitive_coeff_p')
            ])
        else:
            self.method['gaussian_contractions'].append([section.get_latest_value('x_crystal_basis_set_atom_shell_primitive_coeff_dfg')])
        return

    def onClose_section_single_configuration_calculation(self, backend, gIndex, section):
        # Method reference
        method_index = self.method.get("single_configuration_to_calculation_method_ref")
        if method_index is not None:
            backend.addValue("single_configuration_to_calculation_method_ref", method_index)

        # Method reference
        system_index = self.method.get("single_configuration_calculation_to_system_ref")
        if method_index is not None:
            backend.addValue("single_configuration_calculation_to_system_ref", method_index)

        gIndex = backend.openSection('section_method_basis_set')
        type2 = self.cache_service['x_crystal_info_type_of_calculation2']
        if type2 == 'HARTREE-FOCK HAMILTONIAN':
            backend.addValue("method_basis_set_kind", "wavefunction")
        backend.closeSection('section_method_basis_set', gIndex)

    def onClose_x_crystal_section_info(self, backend, gIndex, section):
        arr = self.getValues(section, 'x_crystal_info_shrink_value', 1, 3)
        if arr is not None:
            backend.addArrayValues('x_crystal_info_shrink', arr)
        return

    def onClose_x_crystal_section_vibrational_symmetry(self, backend, gIndex, section):
        text = section.get_latest_value('x_crystal_vibrational_symmetry_text')
        if text is None:
            return
        regx = re.compile('(\d+)')
        ops = regx.findall(text)
        if ops is None or len(ops) < 1:
            raise Exception('onClose_x_crystal_section_vibrational_symmetry: invalid group ops')
        backend.addArrayValues('x_crystal_vibrational_symmetry_group_operators', ints(ops))
        return

    def onClose_x_crystal_section_properties_atom(self, backend, gIndex, section):
        backend.addArrayValues('x_crystal_properties_atom_coordinates', self.getValues(section, 'x_crystal_properties_atom_value', 1, 3))
        return

    def onClose_x_crystal_section_forces_atom(self, backend, gIndex, section):
        backend.addArrayValues('atom_forces', np.array(self.method['atom_forces']))
        self.method['atom_forces'] = None
        return

    #===========================================================================
    # The functions that trigger when sections are opened
    def onOpen_section_method(self, backend, gIndex, section):
        self.method["single_configuration_to_calculation_method_ref"] = gIndex

    def onOpen_section_system(self, backend, gIndex, section):
        self.method["single_configuration_calculation_to_system_description_ref"] = gIndex

    def onOpen_x_crystal_section_forces_atom(self, backend, gIndex, section):
        self.method['atom_forces'] = []

    def onOpen_x_crystal_section_basis_set_atom_shell(self, backend, gIndex, section):
        self.method['gaussian_exponents'] = []
        self.method['gaussian_contractions'] = []

    def onOpen_x_crystal_section_basis_set_atom(self, backend, gIndex, section):
        self.method['gIndex_basis_set_atom_centered'] = backend.openSection('section_basis_set_atom_centered')
        self.method['gIndex_gaussian_basis_group'] = backend.openSection('section_gaussian_basis_group')

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

    def adHoc_x_crystal_conventional_cell(self, n):
        def wrapper(parser):
            values = self.getAdHocValues(parser, 'value', n)
            number_of_atoms = self.getAdHocValue(parser, 'number_of_atoms')
            if number_of_atoms is None:
                if n == 6:
                    parser.backend.addArrayValues('x_crystal_conventional_cell_lengths', np.array(values[0:3]))
                    parser.backend.addArrayValues('x_crystal_conventional_cell_angles', np.array(values[3:6]))
                    return
                raise Exception("Do not know how to handle "+str(n)+" cell parameters")
            if n <= 2:
                raise Exception("Not enough parameters for atom")
            gIndex = parser.backend.openSection('x_crystal_section_conventional_cell_atom')
            label = int(values[0])
            z = int(values[1])
            coord = values[2:n]
            parser.backend.addValue('x_crystal_conventional_cell_atom_label', label)
            parser.backend.addValue('x_crystal_conventional_cell_atom_z', z)
            parser.backend.addArrayValues('x_crystal_conventional_cell_atom_coordinates', np.array(coord))
            parser.backend.closeSection('x_crystal_section_conventional_cell_atom', gIndex)
            return
        return wrapper

    def adHoc_x_crystal_primitive_cell(self, n):
        def wrapper(parser):
            values = self.getAdHocValues(parser, 'value', n)
            if n == 7:
                parser.backend.addArrayValues('x_crystal_primitive_cell_lengths', np.array(values[0:3]))
                parser.backend.addArrayValues('x_crystal_primitive_cell_angles', np.array(values[3:6]))
                parser.backend.addValue('x_crystal_primitive_cell_volume', values[6])
                return
            raise Exception("Do not know how to handle "+str(n)+" cell parameters")
            pass
        return wrapper

    def adHoc_x_crystal_primitive_cell_atom(self, n):
        def wrapper(parser):
            values = self.getAdHocValues(parser, 'value', n)
            parser.backend.addArrayValues('x_crystal_primitive_cell_atom_coordinates', np.array(values))
            elem = self.getAdHocValue(parser, 'element')
            elem_z = self.getAdHocValue(parser, 'z')
            self.storeElementNumber(elem, elem_z)
            # self.method['atom_labels'].append(elem.capitalize())
            return
        return wrapper

    # def adHoc_x_crystal_geometry_consistent(self, v):
        # def wrapper(parser):
            # parser.backend.addValue('x_crystal_geometry_consistent', v)
            # return
        # return wrapper

    def adHoc_x_crystal_spacegroup(self):
        def wrapper(parser):
            name = self.getAdHocValueFullName(parser, 'x_crystal_spacegroup')
            for i in range(230):
                if name == self.spacegroups[i]:
                    parser.backend.addValue("space_group_3D_number", i+1)
                    break
        return wrapper

    def adHoc_x_crystal_dielectric_tensor(self):
        regex_string = r"^\s*({0})\s+({0})\s+({0})\s*$".format(self.regex_f)
        regex_compiled = re.compile(regex_string)

        def wrapper(parser):
            # Read the lines containing the cell vectors
            a_line = parser.fIn.readline()
            b_line = parser.fIn.readline()
            c_line = parser.fIn.readline()

            # Define the regex that extracts the components and apply it to the lines
            a_result = regex_compiled.match(a_line)
            b_result = regex_compiled.match(b_line)
            c_result = regex_compiled.match(c_line)

            # Convert the string results into a 3x3 numpy array
            tensor = np.zeros((3, 3))
            tensor[0, :] = [float(x) for x in a_result.groups()]
            tensor[1, :] = [float(x) for x in b_result.groups()]
            tensor[2, :] = [float(x) for x in c_result.groups()]

            parser.backend.addArrayValues('x_crystal_dielectric_tensor', tensor)
        return wrapper

    def adHoc_x_crystal_dimensionality(self, parser):
        self.getAdHocValueFullName(parser, 'x_crystal_dimensionality')

    def adHoc_x_crystal_cell_transformation_matrix(self):
        regx = re.compile("^\s*" + "\s+".join([self.float_match] * 9) + "\s*$")

        def wrapper(parser):
            values = flt(regx.match(parser.fIn.readline()).groups())
            parser.backend.addArrayValues('x_crystal_cell_transformation_matrix', np.reshape(values, [3, 3]))
        return wrapper

    def adHoc_x_crystal_cell_parameters(self):
        regx = re.compile("^\s*" + "\s+".join([self.float_match] * 6) + "\s*$")

        def wrapper(parser):
            parser.backend.addArrayValues('x_crystal_cell_parameters', flt(regx.match(parser.fIn.readline()).groups()))
            return
        return wrapper

    def adHoc_simulation_cell(self, parser):
        cvector_match = re.compile('^\s*' + self.fs(3) + '\s*$')
        regx = re.compile("^\s*X\s+Y\s+Z\s*$")
        clabels = regx.match(parser.fIn.readline())

        if not clabels:
            return False
        n = 0
        vectors = []
        for i in range(1, 4):
            cvector = cvector_match.match(parser.fIn.readline())
            if not cvector:
                break
            vector = []
            for j in range(1, 4):
                v = float(cvector.group(j))
                if v is None:
                    break
                vector.append(v)
                n = n + 1
            vectors.append(vector)
        if n == 9:
            parser.backend.addArrayValues("simulation_cell", vectors, unit="angstrom")

    def adHoc_bohr_angstrom(self):
        regx = re.compile("^\s*LATTICE PARAMETERS \(ANGSTROMS AND DEGREES\) \- BOHR \=\s*" + self.float_match + "\s* ANGSTROM\s*$")

        def wrapper(parser):
            v = regx.match(parser.fIn.readline())
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
            cvector_match = re.compile('^\s*' + self.fs(6) + '\s*$')
            line1 = cvector_match.match(parser.fIn.readline())
            factor = parser.backend.superBackend
            if not line1:
                return
            periodic = []
            params = []
            nonperiodic_tag = 500
            if 'nonperiodic_tag' in self.method:
                nonperiodic_tag = self.method['nonperiodic_tag']
                if nonperiodic_tag is None:
                    nonperiodic_tag = 500
            for i in range(6):
                v = float(line1.group(i+1))
                if i < 3:
                    params.append(v * self.bohr_angstrom)
                    p = True
                    if v == nonperiodic_tag:
                        p = False
                    periodic.append(p)
                else:
                    params.append(v)
            if self.bohr_angstrom > 0:
                parser.backend.addArrayValues("x_crystal_lattice_parameters", np.array(params))
        return wrapper

    def adHoc_atom_positions(self, parser):
        line_regex = re.compile("\s+{0}\s+{0}\s+({1})\s+({2})\s+({2})\s+({2})".format(self.regexs.int, self.regexs.word, self.regexs.float))
        labels = []
        coordinates = []
        while True:
            line = parser.fIn.readline()
            match = line_regex.match(line)
            if match is None:
                break
            groups = match.groups()
            label = groups[0]
            coordinate = np.array([float(x) for x in groups[1:4]])
            coordinates.append(coordinate)
            labels.append(label.capitalize())

        coordinates = np.array(coordinates)
        labels = np.array(labels)

        parser.backend.addArrayValues("atom_labels", labels)
        parser.backend.addArrayValues("atom_positions", coordinates, unit="angstrom")
        parser.backend.addValue("number_of_atoms", len(labels))

    def adHoc_atom_positions2(self, parser):
        line_regex = re.compile("\s+{0}\s+[TF]\s+{0}\s+({1})\s+({2})\s+({2})\s+({2})".format(self.regexs.int, self.regexs.word, self.regexs.float))
        labels = []
        coordinates = []
        while True:
            line = parser.fIn.readline()
            match = line_regex.match(line)
            if match is None:
                break
            groups = match.groups()
            coordinate = np.array([float(x) for x in groups[1:4]])
            label = groups[0]
            coordinates.append(coordinate)
            labels.append(label.capitalize())

        coordinates = np.array(coordinates)
        labels = np.array(labels)

        parser.backend.addArrayValues("atom_labels", labels)
        parser.backend.addArrayValues("atom_positions", coordinates, unit="angstrom")
        parser.backend.addValue("number_of_atoms", len(labels))

    def adHoc_x_crystal_kpoints(self, sname):
        def wrapper(parser):
            while True:
                line = self.regex_kpoint.findall(parser.fIn.readline())
                if line is None or len(line) < 1:
                    break
                for kpoint in line:
                    gIndex = parser.backend.openSection('x_crystal_section_' + sname)
                    parser.backend.addValue('x_crystal_' + sname + '_number', int(kpoint[0]))
                    parser.backend.addValue('x_crystal_' + sname + '_symbol', kpoint[1])
                    parser.backend.addArrayValues('x_crystal_' + sname + '_coordinates', ints(kpoint[2:]))
                    parser.backend.closeSection('x_crystal_section_' + sname, gIndex)
            return
        return wrapper

    def adHoc_x_crystal_lattice(self):
        regx = re.compile("^\s*" + self.fs(6) + "\s*$")

        def wrapper(parser):
            real_lattice = []
            reciprocal_lattice = []
            for i in range(0, 3):
                vs = regx.match(parser.fIn.readline())
                if vs is None:
                    return
                vs = vs.groups()
                if len(vs) != 6:
                    return
                real_lattice.append(vs[0:3])
                reciprocal_lattice.append(vs[3:6])
            parser.backend.addArrayValues('x_crystal_lattice_real', flt2(real_lattice))
            parser.backend.addArrayValues('x_crystal_lattice_reciprocal', flt2(reciprocal_lattice))
            return
        return wrapper

    def adHoc_x_crystal_neighbors(self, dim):
        regx = re.compile("^\s*(\d+)\s+([A-Z]+)\s+(\d+)\s+" + self.fs(2) + "(\s+\d+\s+[A-Z]+\s+" + "[ \-]{1}\d+"*dim + ")+\s*$")
        regx2 = re.compile("\s+(\d+)\s+([A-Z]+)\s+" + "([ \-]{1}\d+)" * dim)

        def wrapper(parser):
            textline = parser.fIn.readline()
            line = regx.match(textline)
            if line is None:
                raise Exception("Strange line: adHoc_x_crystal_neighbors (1)")
            line = line.groups()
            if line is None or len(line) <= 5:
                raise Exception("Strange line: adHoc_x_crystal_neighbors (2)")
            atomlabel = line[0]
            atomelement = line[1]
            n = int(line[2])
            while True:
                gIndex = parser.backend.openSection('x_crystal_section_neighbors_atom_distance')
                parser.backend.addValue('x_crystal_neighbors_atom_distance_number_of_neighbors', n)
                parser.backend.addValue('x_crystal_neighbors_atom_distance_ang', float(line[3]))
                parser.backend.addValue('x_crystal_neighbors_atom_distance_au', float(line[4]))
                while n > 0:
                    ns = regx2.findall(textline)
                    left = len(ns)
                    if left < 1 or left > n:
                        raise Exception("Strange line adHoc_x_crystal_neighbors (3)")
                    for neighbor in ns:
                        gIndex2 = parser.backend.openSection('x_crystal_section_neighbors_atom_distance_neighbor')
                        parser.backend.addValue('x_crystal_neighbors_atom_distance_neighbor_label', int(neighbor[0]))
                        parser.backend.addValue('x_crystal_neighbors_atom_distance_neighbor_element', neighbor[1])
                        parser.backend.addArrayValues('x_crystal_neighbors_atom_distance_neighbor_cell', ints(neighbor[2:2+dim]))
                        parser.backend.closeSection('x_crystal_section_neighbors_atom_distance_neighbor', gIndex2)
                        n -= 1
                    textline = parser.fIn.readline()
                parser.backend.closeSection('x_crystal_section_neighbors_atom_distance', gIndex)
                line = regx.match(textline)
                if line is None:
                    break
                line = line.groups()
                if line is None or len(line) <= 5:
                    raise Exception("Strange line: adHoc_x_crystal_neighbors (4)")
                if line[0] != atomlabel or line[1] != atomelement:
                    raise Exception("Strange line: adHoc_x_crystal_neighbors (5)")
                    break
                n = int(line[2])
            return
        return wrapper

    def adHoc_x_crystal_frequency_atom(self):
        regx = re.compile("\s+(\d+)\s+([A-Z]+)\s+" + self.fs(1))

        def wrapper(parser):
            while True:
                textline = parser.fIn.readline()
                line = regx.findall(textline)
                if line is None or len(line) == 0:
                    break
                for atom in line:
                    gIndex = parser.backend.openSection('x_crystal_section_frequency_atom')
                    parser.backend.addValue('x_crystal_frequency_atom_label', int(atom[0]))
                    parser.backend.addValue('x_crystal_frequency_atom_element', atom[1])
                    parser.backend.addValue('x_crystal_frequency_atom_mass', float(atom[2]))
                    parser.backend.closeSection('x_crystal_section_frequency_atom', gIndex)
            return
        return wrapper

    def adHoc_x_crystal_section_frequency_gradients_op(self):
        regx_num = re.compile("^(\d+)$")
        regx_gen = re.compile("^GENERATED FROM LINE\s*(\S+)\s*WITH OP\s+(\d+)$")

        def wrapper(parser):
            text = self.getAdHocValue(parser, 'text')
            if text is None:
                raise Exception("adHoc_x_crystal_section_frequency_gradients_op: Unable to retrieve text value")
            if text == "GENERATED BY TRANSLATIONAL INVARIANCE":
                parser.backend.addValue('x_crystal_frequency_gradients_op_translational_invariance', True)
                return
            v = regx_num.match(text)
            if v is not None:
                parser.backend.addValue('x_crystal_frequency_gradients_op_symmops', int(v.group(1)))
                return
            v = regx_gen.match(text)
            if v is not None:
                parser.backend.addValue('x_crystal_frequency_gradients_op_generated_from_line', v.group(1))
                parser.backend.addValue('x_crystal_frequency_gradients_op_generated_by_symmop', int(v.group(2)))
                return
            raise Exception("adHoc_x_crystal_section_frequency_gradients_op: Unable to handle text value" + text)
        return wrapper

    def adHoc_x_crystal_total_atomic_charges(self, clas):
        regx = re.compile(self.regex_f)

        def wrapper(parser):
            textline = parser.fIn.readline()
            v = regx.findall(textline)
            if v is not None and len(v) >= 1:
                parser.backend.addArrayValues('x_crystal_' + clas + '_atomic_charges', flt(v))
            return
        return wrapper

    def adHoc_x_crystal_scf_insulating_state(self):
        def wrapper(parser):
            parser.backend.addValue('x_crystal_scf_insulating_state', True)
            return
        return wrapper

    def adHoc_x_crystal_scf_kinetic_energy(self):
        def wrapper(parser):
            self.method['x_crystal_scf_kinetic_energy'] = self.getAdHocValue(parser, 'x_crystal_scf_kinetic_energy')
            return
        return wrapper

    def adHoc_x_crystal_scf_final(self, ok):
        def wrapper(parser):
            """Called when the SCF cycle of a single point calculation has converged.
            """
            parser.backend.addValue('single_configuration_calculation_converged', ok)
            if self.method['x_crystal_scf_kinetic_energy'] is not None:
                v = parser.backend.convert_unit('electronic_kinetic_energy', self.method['x_crystal_scf_kinetic_energy'], "hartree")
                parser.backend.addValue('electronic_kinetic_energy', v)
            return
        return wrapper

    def adHoc_x_crystal_forces_atom(self):
        def wrapper(parser):
            vs = self.getAdHocValues(parser, 'value', 3)
            if vs is not None and len(vs) >= 1:
                parser.backend.addArrayValues('x_crystal_forces_atom_force', np.array(vs))
                self.method['atom_forces'].append(vs)
            return
        return wrapper

    def adHoc_x_crystal_forces(self):
        def wrapper(parser):
            vs = self.getAdHocValues(parser, 'value', 3)
            if vs is not None and len(vs) >= 1:
                parser.backend.addArrayValues('x_crystal_forces_resultant', np.array(vs))
            return
        return wrapper

    def adHoc_x_crystal_forces_symmetry_allowed_directions(self, n):
        def wrapper(parser):
            parser.backend.addValue('x_crystal_forces_symmetry_allowed_directions', n)
            return
        return wrapper

    def adHoc_x_crystal_forces_born_atom_tensor(self, n):
        regx = re.compile("^\s*(\d+)\s+" + self.fs(n) + "\s*$")

        def wrapper(parser):
            vs = []
            for i in range(1,n+1):
                line = regx.match(parser.fIn.readline())
                if line is None:
                    raise Exception("adHoc_x_crystal_forces_born_atom_tensor: strange (1)")
                line = line.groups()
                if line is None or len(line) != n+1:
                    raise Exception("adHoc_x_crystal_forces_born_atom_tensor: strange (2)")
                if int(line[0]) != i:
                    raise Exception("adHoc_x_crystal_forces_born_atom_tensor: strange (3)" + str(line))
                vs.append(line[1:n+1])
            parser.backend.addArrayValues('x_crystal_forces_born_atom_tensor', flt2(vs))
            return
        return wrapper

    def adHoc_x_crystal_vibrational_multip(self):

        def wrapper(parser):
            texts = self.getAdHocValues(parser, 'text', 3)
            if texts is None:
                raise Exception("adHoc_x_crystal_vibrational_multip strange (1)")
            regx = re.compile("(\S+)")
            irrep_cla = regx.findall(texts[0])
            multip    = regx.findall(texts[1])
            fu        = regx.findall(texts[2])
            n = len(irrep_cla)
            if len(multip) != n or len(fu) != n:
                raise Exception("adHoc_x_crystal_vibrational_multip strange (2)")
            for i in range(0, n):
                gIndex = parser.backend.openSection('x_crystal_section_vibrational_multip')
                parser.backend.addValue('x_crystal_vibrational_multip_irrep_cla', irrep_cla[i])
                parser.backend.addValue('x_crystal_vibrational_multip_multip', int(multip[i]))
                parser.backend.addValue('x_crystal_vibrational_multip_fu', float(fu[i]))
                parser.backend.closeSection('x_crystal_section_vibrational_multip', gIndex)
            return
        return wrapper

    def adHoc_x_crystal_vibrational_fu(self):
        def wrapper(parser):
            minus = self.getAdHocValue(parser, 'minus')
            xy = self.getAdHocValues(parser, 'integer', 2)
            if minus is None or xy is None or len(xy) != 2:
                raise Exception("adHoc_x_crystal_vibrational_fu strange (1)")
            if minus == "-":
                xy[0] = -int(xy[0])
                xy[1] = -int(xy[1])
            parser.backend.addArrayValues('x_crystal_vibrational_fu', np.array(xy))
            return
        return wrapper

    def adHoc_x_crystal_vibrational_optical(self, n):
        def wrapper(parser):
            vs = self.getAdHocValues(parser, 'value', n)
            if vs is None or len(vs) != n:
                raise Exception("adHoc_x_crystal_vibrational_optical strange(1)")
            parser.backend.addArrayValues('x_crystal_vibrational_optical_longitudal_mode_direction', np.array(vs))
            return
        return wrapper

    def adHoc_x_crystal_vibrational_mode(self, n):
        def wrapper(parser):
            vs = self.getAdHocValues(parser, 'value', n)
            if vs is None or len(vs) != n:
                raise Exception("adHoc_x_crystal_vibrational_mode strange(1)")
            parser.backend.addArrayValues('x_crystal_vibrational_mode_born_charge_vector', np.array(vs))
            return
        return wrapper

    def adHoc_x_crystal_vibrational_modetensor(self, n):
        regx = re.compile("\s+(" + self.regex_f + ")")

        def wrapper(parser):
            vs = self.getAdHocValues(parser, 'value', n)
            if vs is None or len(vs) != n:
                raise Exception("adHoc_x_crystal_vibrational_modetensor strange(1)")
            vs = [vs]
            for i in range(1,n):
                line = regx.findall(parser.fIn.readline())
                if line is None or len(line) != n:
                    raise Exception("adHoc_x_crystal_vibrational_modetensor strange(2)")
                vs.append(line)
            parser.backend.addArrayValues('x_crystal_vibrational_mode_tensor', flt2(vs))
            return
        return wrapper

    def adHoc_x_crystal_vibrational_tensor(self, n, meaning):
        regx = re.compile("\s+(" + self.regex_f + ")")

        def wrapper(parser):
            vs = self.getAdHocValues(parser, 'value', n)
            if vs is None or len(vs) != n:
                raise Exception("adHoc_x_crystal_vibrational_modetensor strange(1)")
            vs = [vs]
            for i in range(1, n):
                line = regx.findall(parser.fIn.readline())
                if line is None or len(line) != n:
                    raise Exception("adHoc_x_crystal_vibrational_modetensor strange(2)")
                vs.append(line)
            parser.backend.addArrayValues('x_crystal_vibrational_dielectric_tensor_' + meaning, flt2(vs))
            return
        return wrapper

    def reorder(self, array, dim):
        ret = []
        n = int(len(array) / dim)
        if len(array) != n*dim:
            raise Exception("reorder number of items does not match")
        for i in range(0, n):
            for j in range(0, dim):
                ret.append(array[n*j + i])
        return ret

    def adHoc_x_crystal_irX_modes(self, type, dim, n):
        regx1 = re.compile("^\s*AT\.\s+(\d+)\s+([A-Z]+)\s+([XYZ]{1})\s+" + self.fs(n*dim) + "\s*$")
        regx2 = re.compile("^\s*([XYZ]{1})\s+" + self.fs(n*dim) + "\s*$")
        rempty = re.compile("^\s*$")

        def wrapper(parser):
            frequencies = self.getAdHocValues(parser, 'value', dim*n)
            if frequencies is None:
                raise Exception('adHoc_x_crystal_irX_modes (' + type + '): strange(1)')
            if type == 'lo':
                frequencies = self.reorder(frequencies, dim)
            textline = parser.fIn.readline()
            if rempty.match(textline):
                textline = parser.fIn.readline()
            line = regx1.match(textline)
            if line is None:
                raise Exception('adHoc_x_crystal_irX_modes (' + type + '): strange(2)')
            line = line.groups()
            if len is None or len(line) != 3+n*dim:
                raise Exception('adHoc_x_crystal_irX_modes (' + type + '): strange(3)')
            gIndex = parser.backend.openSection('x_crystal_section_ir' + type + '_modes_atom')
            parser.backend.addValue('x_crystal_ir' + type + '_modes_atom_label', int(line[0]))
            parser.backend.addValue('x_crystal_ir' + type + '_modes_atom_element', line[1])
            tensors = []
            axislabels = line[2]
            line = line[3:]
            if type == 'lo':
                line = self.reorder(line, dim)
            for i in range(0, n):
                tensors.append([line[i*dim: (i+1)*dim]])
            for j in range(1, dim):
                textline = parser.fIn.readline()
                line = regx2.match(textline)
                if line is None:
                    raise Exception('adHoc_x_crystal_irX_modes (' + type + '): strange(4)')
                line = line.groups()
                if line is None or len(line) != 1+dim*n:
                    raise Exception('adHoc_x_crystal_irX_modes (' + type + '): strange(5)')
                axislabels += line[0]
                line = line[1:]
                if type == 'lo':
                    line = self.reorder(line, dim)
                for i in range(0, n):
                    tensors[i].append(line[i*dim: (i+1)*dim])
            parser.backend.addValue('x_crystal_ir' + type + '_modes_atom_axislabels', axislabels)
            for i in range(0, n):
                gIndex2 = parser.backend.openSection('x_crystal_section_ir' + type + '_modes_atom_mode')
                parser.backend.addArrayValues('x_crystal_ir' + type + '_modes_atom_mode_frequencies', np.array(frequencies[i*dim: (i+1)*dim]))
                parser.backend.addArrayValues('x_crystal_ir' + type + '_modes_atom_mode_tensor', flt2(tensors[i]))
                parser.backend.closeSection('x_crystal_section_ir' + type + '_modes_atom_mode', gIndex2)
            gIndex = parser.backend.closeSection('x_crystal_section_ir' + type + '_modes_atom', gIndex)
            return
        return wrapper

    def adHoc_x_crystal_irlo_overlap(self):
        rempty = re.compile("^\s*$")

        def wrapper(parser):
            textline = parser.fIn.readline()
            to_frequencies = self.regex_fs.findall(textline)
            if to_frequencies is None:
                raise Exception('adHoc_x_crystal_irlo_overlap strange(1)')
            lo_frequencies = []
            overlap = []
            n = len(to_frequencies)
            if n < 1:
                raise Exception('adHoc_x_crystal_irlo_overlap strange(2)')
            textline = parser.fIn.readline()
            if not rempty.match(textline):
                raise Exception('adHoc_x_crystal_irlo_overlap strange(3)')
            for i in range(0, n):
                line = self.regex_fs.findall(parser.fIn.readline())
                if line is None or len(line) != n+1:
                    raise Exception('adHoc_x_crystal_irlo_overlap strange(4)')
                lo_frequencies.append(line[0])
                overlap.append(line[1:])
            gIndex = parser.backend.openSection('x_crystal_section_irlo_overlap')
            parser.backend.addArrayValues('x_crystal_irlo_overlap_to', flt(to_frequencies))
            parser.backend.addArrayValues('x_crystal_irlo_overlap_lo', flt(lo_frequencies))
            parser.backend.addArrayValues('x_crystal_irlo_overlap_matrix', flt2(overlap))
            parser.backend.closeSection('x_crystal_section_irlo_overlap', gIndex)
        return wrapper

    def adHoc_x_crystal_vibrational_modes(self, type):
        regex = re.compile('\s*' + self.fs(1) + '\s*\[\s*(\d+)\s*;\s*(\S+)\s*\]')

        def wrapper(parser):
            line = regex.findall(parser.fIn.readline())
            if line is None or len(line) < 1:
                return
            for m in line:
                gIndex = parser.backend.openSection('x_crystal_section_vibrational_modes_' + type)
                parser.backend.addValue('x_crystal_vibrational_modes_' + type + '_temperature', float(m[0]))
                parser.backend.addValue('x_crystal_vibrational_modes_' + type + '_number',      int(m[1]))
                parser.backend.addValue('x_crystal_vibrational_modes_' + type + '_irrep',       m[2])
                parser.backend.closeSection('x_crystal_section_vibrational_modes_' + type, gIndex)
        return wrapper

    def adHoc_x_crystal_properties_lattice(self):
        def wrapper(parser):
            line = self.regex_fs.findall(parser.fIn.readline())
            if line is None or len(line) < 1:
                raise Exception("adHoc_x_crystal_properties_lattice: strange(1)")
            n = len(line)
            matrix = [line]
            for i in range(1, n):
                line = self.regex_fs.findall(parser.fIn.readline())
                if line is None or len(line) != n:
                    raise Exception("adHoc_x_crystal_properties_lattice: strange(2)")
                matrix.append(line)
            parser.backend.addArrayValues('x_crystal_properties_lattice_vectors', flt2(matrix))
            return
        return wrapper

    def adHoc_x_crystal_properties_lattice_parameters(self, n):
        def wrapper(parser):
            arr = self.getAdHocValues(parser, 'value', n)
            if n == 7:
                parser.backend.addArrayValues('x_crystal_properties_lattice_lengths', np.array(arr[0:3]))
                parser.backend.addArrayValues('x_crystal_properties_lattice_angles', np.array(arr[3:6]))
                parser.backend.addValue('x_crystal_properties_lattice_volume', arr[6])
            return
        return wrapper

    def adHoc_x_crystal_properties_shrink_monkh(self, n):
        def wrapper(parser):
            arr = self.getAdHocValues(parser, 'integer', n)
            if arr is None or len(arr) != n:
                raise Exception("adHoc_x_crystal_properties_shrink_monkh: strange(1)")
            parser.backend.addArrayValues('x_crystal_properties_shrink_monkh', np.array(arr))
            return
        return wrapper

    def adHoc_x_crystal_restart_shrink_monkh(self, n):
        def wrapper(parser):
            arr = self.getAdHocValues(parser, 'integer', n)
            if arr is None or len(arr) != n:
                raise Exception("adHoc_x_crystal_restart_shrink_monkh: strange(1)")
            parser.backend.addArrayValues('x_crystal_restart_shrink_monkh', np.array(arr))
            return
        return wrapper

    def adHoc_x_crystal_properties_gcalco(self, n):
        def wrapper(parser):
            arr = self.getAdHocValues(parser, 'integer', n)
            if arr is None or len(arr) != n:
                raise Exception("adHoc_x_crystal_properties_gcalco: strange(1)")
            parser.backend.addArrayValues('x_crystal_properties_gcalco_max_indices', np.array(arr))
            return
        return wrapper

    def adHoc_x_crystal_bands_line_coordinates(self, type, n):
        def wrapper(parser):
            arr1 = self.getAdHocValues(parser, 'value1', n)
            arr2 = self.getAdHocValues(parser, 'value2', n)
            if arr1 is None or arr2 is None:
                raise Exception('adHoc_x_crystal_bands_line_coordinates strange(1)')
            parser.backend.addArrayValues('x_crystal_bands_line_coordinates_' + type + '_begin', np.array(arr1))
            parser.backend.addArrayValues('x_crystal_bands_line_coordinates_' + type + '_end', np.array(arr2))
            return
        return wrapper

    def adHoc_x_crystal_bands_line_point(self, n):
        def wrapper(parser):
            values = self.getAdHocValues(parser, 'integer', n*2)
            if values is None or len(values) != 2*n:
                raise Exception('adHoc_x_crystal_bands_line_point')
            coordinates = []
            for i in range(0, n):
                coordinates.append( float(values[2*i]) / float(values[2*i+1]))
            parser.backend.addArrayValues('x_crystal_bands_line_point_coordinates', np.array(coordinates))
            ret = []
            while True:
                arr = self.regex_fs.findall(parser.fIn.readline())
                if arr is None or len(arr) < 1:
                    break
                for v in arr:
                    ret.append(v)
            parser.backend.addArrayValues('x_crystal_bands_line_point_energies', flt(ret))
            return
        return wrapper

    def adHoc_x_crystal_restart_insulating(self):
        def wrapper(parser):
            parser.backend.addValue('x_crystal_restart_insulating_state', True)
            return
        return wrapper

    def adHoc_x_crystal_restart_dos_scale(self):
        def wrapper(parser):
            self.method['x_crystal_restart_dos_scale_t'] = float(self.getAdHocValue(parser, 'scale_t'))
            return
        return wrapper

    def adHoc_x_crystal_restart_dos_energy_dos(self):
        def wrapper(parser):
            text = self.getAdHocValue(parser, 'text')
            c = self.method['x_crystal_restart_dos_scale_t']
            if c <= 0 or text is None or len(text) < 1:
                raise Exception('adHoc_x_crystal_restart_dos_energy_dos strange(1)')
            parser.backend.addValue('x_crystal_restart_dos_energy_dos', c * float(len(text)-1))
            return
        return wrapper

    #===========================================================================
    # startReActions
    def transform_convergence_on_deltap(self, backend, groups):
        limit = int(groups[0].replace(" ", ""))
        limit = pow(10, limit)
        backend.addValue('x_crystal_info_convergence_on_deltap', limit)

    def transform_convergence_on_energy(self, backend, groups):
        limit = int(groups[0].replace(" ", ""))
        limit = pow(10, limit)
        backend.addValue('x_crystal_info_convergence_on_energy', limit)

    def transform_nonperiodic_tag(self, backend, groups):
        self.method['nonperiodic_tag'] = groups[0]

    def transform_periodicity(self, backend, groups):
        dimensionality = groups[0]
        if dimensionality == "0":
            periodicity = [False, False, False]
        if dimensionality == "1":
            periodicity = [True, False, False]
        if dimensionality == "2":
            periodicity = [True, True, False]
        if dimensionality == "3":
            periodicity = [True, True, True]
        backend.addArrayValues("configuration_periodic_dimensions", np.array(periodicity))

    def transform_periodicity_prim(self, backend, groups):
        periodic = []
        for text in groups:
            if text == 'ANGSTROM':
                periodic.append(False)
            else:
                periodic.append(True)
        backend.addArrayValues("configuration_periodic_dimensions", np.array(periodic))

    def transform_symmetry_adaption(self, backend, groups):
        text = groups[0]
        backend.addValue('x_crystal_info_symmetry_adaption', text == "ENABLED")

    def transform_scf_convergence(self, backend, groups):
        convergence = groups[1]
        base, exponent = convergence.split("**")
        base = int(base)
        exponent = int("".join(exponent.split()))
        result = pow(base, exponent)
        backend.addRealValue('scf_threshold_energy_change', result, unit="hartree")

    def transform_basis_set_shell(self, backend, groups):
        shell = groups[-1]
        self.method['gaussian_shell'] = shell

    def action_push1D(self, backend, groups):
        backend.addArrayValues("configuration_periodic_dimensions", np.array([True, False, False]))

    #===========================================================================
    # Misc
    def debug(self, backend, groups):
        print("DEBUG")

    #===========================================================================
    # New AdHocs
    def adHoc_type_of_calculation(self, parser):

        lines = []
        lines.append(parser.fIn.readline().split(":")[-1].strip())

        while True:
            line = parser.fIn.readline()
            if line.isspace():
                break
            lines.append(line.strip())
        calc_type = " ".join(lines)

        self.backend.addValue("x_crystal_info_type_of_calculation", calc_type)


#===============================================================================
# Misc helper functions
def flt(values):
    arr = []
    for v in values:
        arr.append(float(v))
    return np.array(arr)


def ints(values):
    arr = []
    for v in values:
        arr.append(int(v))
    return np.array(arr)


def flt2(values):
    arr = []
    for v in values:
        arr2 = []
        for v2 in v:
            arr2.append(float(v2))
        arr.append(arr2)
    return np.array(arr)


def flt2np(values):
    arr = []
    for v in values:
        arr2 = []
        for v2 in v:
            arr2.append(float(v2))
        arr.append(arr2)
    return arr


def asElementSymbol(label):
    label = str(label)
    if(len(label) == 2):
        label = label[0].capitalize() + label[1].lower()
    return label
