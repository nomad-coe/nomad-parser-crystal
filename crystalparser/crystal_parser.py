import logging
import datetime
import re
import numpy as np
import ase

from nomad.units import ureg
from nomad import atomutils
from nomad.parsing.parser import FairdiParser
from nomad.parsing.file_parser import UnstructuredTextFileParser, Quantity
from nomad.datamodel.metainfo.public import section_run, section_method, section_system,\
    section_XC_functionals, section_scf_iteration, section_single_configuration_calculation,\
    section_sampling_method, section_frame_sequence, section_eigenvalues, section_dos,\
    section_atom_projected_dos, section_species_projected_dos, section_k_band,\
    section_k_band_segment, section_energy_van_der_Waals, section_calculation_to_calculation_refs,\
    section_method_to_method_refs, section_basis_set_atom_centered
from crystalparser.metainfo.crystal import x_crystal_section_shell


def capture(regex):
    return r'(' + regex + r')'

flt = r'-?(?:\d+\.?\d*|\d*\.?\d+)(?:E[\+-]?\d+)?' # Floating point number
flt_c = capture(flt)                              # Captures a floating point number
flt_crystal_c = r'(-?\d+(?:.\d+)?\*\*-?.*\d+)'    # Crystal specific floating point syntax
ws = r'\s+'                                       # Series of white-space characters
integer = r'-?\d+'                                # Integer number
integer_c = capture(integer)                      # Captures integer number
word = r'[a-zA-Z]+'                               # A single alphanumeric word
word_c = capture(word)                            # Captures a single alphanumeric word

class CrystalParser(FairdiParser):
    """NOMAD-lab parser for Crystal.
    """
    def __init__(self):
        super().__init__(
            name='parsers/crystal',
            code_name='Crystal',
            code_homepage='https://www.crystal.unito.it/',
            mainfile_contents_re=(
                r'(CRYSTAL\s*\n\d+ \d+ \d+)|(CRYSTAL will run on \d+ processors)|'
                r'(\s*\*\s*CRYSTAL[\d]+\s*\*\s*\*\s*(public|Release) \: [\d\.]+.*\*)|'
                r'(Executable:\s*[/_\-a-zA-Z0-9]*MPPcrystal)'
            )
        )

    def parse_output(self, filepath):
        """Reads the calculation output.
        """
        outputparser = UnstructuredTextFileParser(
            filepath,
            quantities=[
                # Header
                Quantity("datetime", r'(?:Date\:|date)\s+(.*?)\n', str_operation=lambda x: x, repeats=False),
                Quantity("hostname", r'(?:Running on\:|hostname)\s+(.*?)\n', str_operation=lambda x: x, repeats=False),
                Quantity("os", r'(?:system)\s+(.*?)\n', str_operation=lambda x: x, repeats=False),
                Quantity("user", r'user\s+(.*?)\n', str_operation=lambda x: x, repeats=False),
                Quantity("input_path", r'(?:Input data|input data in)\s+(.*?)\n', str_operation=lambda x: x, repeats=False),
                Quantity("output_path", r'(?:Output\:|output data in)\s+(.*?)\n', str_operation=lambda x: x, repeats=False),
                Quantity("executable_path", r'(?:Executable\:|crystal executable in)\s+(.*?)\n', str_operation=lambda x: x, repeats=False),
                Quantity("tmpdir", r'(?:Temporary directory\:|temporary directory)\s+(.*?)\n', str_operation=lambda x: x, repeats=False),
                Quantity("system_type", r'(CRYSTAL|SLAB|POLYMER|HELIX|MOLECULE|EXTERNAL|DLVINPUT)', repeats=False),
                Quantity("calculation_type", r'(OPTGEOM|FREQCALC|ANHARM)', repeats=False),

                # Input
                Quantity(
                    "dftd3",
                    r'(DFTD3\n[\s\S]*?END\n)',
                    sub_parser=UnstructuredTextFileParser(quantities=[
                        Quantity(
                            "version",
                            r'(VERSION \d)',
                            str_operation=lambda x: x,
                            repeats=False,
                        ),
                    ]),
                    repeats=False,
                ),
                Quantity(
                    "grimme",
                    r'(GRIMME\n[\s\S]*?END\n)',
                    repeats=False,
                ),
                Quantity(
                    "dft",
                    r'(DFT\n[\w\s]*?END\n)',
                    sub_parser=UnstructuredTextFileParser(quantities=[
                        Quantity(
                            "exchange",
                            r'EXCHANGE\n(LDA|VBH|BECKE|PBE|PBESOL|mPW91|PWGGA|SOGGA|WCGGA)',
                            repeats=False,
                        ),
                        Quantity(
                            "correlation",
                            r'CORRELAT\n(PZ|VBH|VWN|LYP|P86|PBE|PBESOL|PWGGA|PWLSD|WL)',
                            repeats=False,
                        ),
                        Quantity(
                            "exchange_correlation",
                            r'(SVWN|BLYP|PBEXC|PBESOLXC|SOGGAXC|B3PW|B3LYP|PBE0|PBESOL0|B1WC|WCILYP|B97H|PBE0-13|HYBRID|NONLOCAL|HSE06|HSESOL|HISS|RSHXLDA|wB97|wB97X|LC-WPBE|LC-WPBESOL|LC-WBLYP|M05-2X|M05|M062X|M06HF|M06L|M06|B2PLYP|B2GPPLYP|mPW2PLYP|DHYBRID)',
                            repeats=False,
                        ),
                    ]),
                    repeats=False,
                ),
                Quantity("program_version", r'\s*\*\s*CRYSTAL(.*?)\s*\*\s*', repeats=False, dtype=str),
                Quantity("distribution", r'\n \*\s*(.*? \: .*? - .*?)\s*\*\n', str_operation=lambda x: x, repeats=False),
                Quantity("start_timestamp", r' EEEEEEEEEE STARTING  DATE\s+(.*? TIME .*?)\n', str_operation=lambda x: x, repeats=False),
                Quantity("title", r' EEEEEEEEEE STARTING  DATE.*?\n\s*(.*?)\n\n', str_operation=lambda x: x, repeats=False),
                Quantity("hamiltonian_type", r' (KOHN-SHAM HAMILTONIAN|HARTREE-FOCK HAMILTONIAN)', str_operation=lambda x: x, repeats=False),
                Quantity("xc_out", r' \(EXCHANGE\)\[CORRELATION\] FUNCTIONAL:(\([\s\S]+?\)\[[\s\S]+?\])', str_operation=lambda x: x, repeats=False),
                Quantity("hybrid_out", fr' HYBRID EXCHANGE - PERCENTAGE OF FOCK EXCHANGE\s+{flt_c}', repeats=False),

                # Geometry optimization settings
                Quantity('initial_trust_radius', fr' INITIAL TRUST RADIUS\s+{flt_c}', repeats=False),
                Quantity('maximum_trust_radius', fr' MAXIMUM TRUST RADIUS\s+{flt_c}', repeats=False),
                Quantity('maximum_gradient_component', fr' MAXIMUM GRADIENT COMPONENT\s+{flt_c}', repeats=False),
                Quantity('rms_gradient_component', fr' R\.M\.S\. OF GRADIENT COMPONENT\s+{flt_c}', repeats=False),
                Quantity('rms_displacement_component', fr' R\.M\.S\. OF DISPLACEMENT COMPONENTS\s+{flt_c}', repeats=False),
                Quantity('geometry_change', fr' MAXIMUM DISPLACEMENT COMPONENT\s+{flt_c}', unit=ureg.bohr, repeats=False),
                Quantity('energy_change', fr' THRESHOLD ON ENERGY CHANGE\s+{flt_c}', unit=ureg.hartree, repeats=False),
                Quantity('extrapolating_polynomial_order', fr' EXTRAPOLATING POLYNOMIAL ORDER{ws}{integer_c}', repeats=False),
                Quantity('max_steps', fr' MAXIMUM ALLOWED NUMBER OF STEPS\s+{integer_c}', repeats=False),
                Quantity('sorting_of_energy_points', fr'SORTING OF ENERGY POINTS\:\s+{word_c}', repeats=False),

                # System
                Quantity("dimensionality",
                    r' GEOMETRY FOR WAVE FUNCTION - DIMENSIONALITY OF THE SYSTEM\s+(\d)',
                    repeats=False
                ),
                Quantity(
                    'lattice_parameters',
                    fr' PRIMITIVE CELL - CENTRING CODE [\s\S]*?VOLUME=\s*{flt} - DENSITY\s*{flt} g/cm\^3\n' +
                    fr'         A              B              C           ALPHA      BETA       GAMMA\s*' +
                    fr'{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\n',
                    shape=(6),
                    dtype=np.float64,
                    repeats=False,
                ),
                Quantity(
                    "labels_positions",
                    fr' ATOMS IN THE ASYMMETRIC UNIT\s+{integer} - ATOMS IN THE UNIT CELL:\s+{integer}\n' +
                    fr'     ATOM              X/A                 Y/B                 Z/C\s*\n' +
                    re.escape(' *******************************************************************************') +
                    fr'((?:\s+{integer}\s+(?:T|F)\s+{integer}\s+[\s\S]*?\s+{flt}\s+{flt}\s+{flt}\n)+)',
                    shape=(-1, 7),
                    dtype=str,
                    repeats=False,
                ),
                Quantity(
                    'lattice_parameters_restart',
                    fr' LATTICE PARAMETERS  \(ANGSTROM AND DEGREES\) - PRIMITIVE CELL\n' +
                    fr'       A          B          C         ALPHA      BETA     GAMMA        VOLUME\n' +
                    fr'\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt}\n',
                    shape=(6),
                    dtype=np.float64,
                    repeats=False,
                ),
                Quantity(
                    "labels_positions_restart",
                    fr'   ATOM N\.AT\.  SHELL    X\(A\)      Y\(A\)      Z\(A\)      EXAD       N\.ELECT\.\n' +
                    re.escape(' *******************************************************************************') +
                    fr'((?:\s+{integer}\s+{integer}\s+{word}\s+{integer}\s+{flt}\s+{flt}\s+{flt}\s+{flt}\s+{flt}\n)+)',
                    shape=(-1, 9),
                    dtype=str,
                    repeats=False,
                ),

                # Method
                Quantity(
                    'basis_set',
                    re.escape(r' *******************************************************************************') + 
                    r'\n LOCAL ATOMIC FUNCTIONS BASIS SET\n' +
                    re.escape(r' *******************************************************************************') +
                    r'\n   ATOM   X\(AU\)   Y\(AU\)   Z\(AU\)  N. TYPE  EXPONENT  S COEF   P COEF   D/F/G COEF\n' + 
                    r'([\s\S]*?)\n INFORMATION',
                    sub_parser=UnstructuredTextFileParser(quantities=[
                        Quantity(
                            "basis_sets",
                            fr'({ws}{integer}{ws}{word}{ws}{flt}{ws}{flt}{ws}{flt}\n(?:(?:\s+(?:\d+-\s+)?\d+\s+(?:S|P|SP|D|F|G)\s*\n[\s\S]*?(?:{ws}{flt}(?:{ws})?{flt}(?:{ws})?{flt}(?:{ws})?{flt}\n)+)+)?)',
                            sub_parser=UnstructuredTextFileParser(quantities=[
                                Quantity(
                                    "species",
                                    fr'({ws}{integer}{ws}{word}{ws}{flt}{ws}{flt}{ws}{flt}\n)',
                                    repeats=False,
                                ),
                                Quantity(
                                    "shells",
                                    fr'(\s+(?:\d+-\s+)?\d+\s+(?:S|P|SP|D|F|G)\s*\n[\s\S]*?(?:{ws}{flt}(?:{ws})?{flt}(?:{ws})?{flt}(?:{ws})?{flt}\n)+)',
                                    sub_parser=UnstructuredTextFileParser(quantities=[
                                        Quantity(
                                            "shell_range",
                                            r'(\s+(?:\d+-\s+)?\d+)',
                                            str_operation=lambda x: "".join(x.split()),
                                            repeats=False,
                                        ),
                                        Quantity(
                                            "shell_type",
                                            r'((?:S|P|SP|D|F|G))\s*\n',
                                            str_operation=lambda x: x.strip(),
                                            repeats=False,
                                        ),
                                        Quantity(
                                            "shell_coefficients",
                                            fr'{ws}({flt})(?:{ws})?({flt})(?:{ws})?({flt})(?:{ws})?({flt})\n',
                                            repeats=True,
                                            dtype=np.float64,
                                            shape=(4)
                                        ),
                                    ]),
                                    repeats=True,
                                ),
                            ]),
                            repeats=True,
                        ),
                    ]),
                    repeats=False,
                ),
                Quantity("fock_ks_matrix_mixing", r' INFORMATION \*+.*?\*+.*?\:\s+FOCK/KS MATRIX MIXING SET TO\s+' + integer_c + r'\s+\%\n*', repeats=False),
                Quantity("coulomb_bipolar_buffer", r' INFORMATION \*+.*?\*+.*?\:\s+COULOMB BIPOLAR BUFFER SET TO\s+' + flt_c + r' Mb\n*', repeats=False),
                Quantity("exchange_bipolar_buffer", r' INFORMATION \*+.*?\*+.*?\:\s+EXCHANGE BIPOLAR BUFFER SET TO\s+' + flt_c + r' Mb\n*', repeats=False),
                Quantity("toldee", r' INFORMATION \*+ TOLDEE \*+\s*\*+ SCF TOL ON TOTAL ENERGY SET TO\s+' + flt_c + r'\n', repeats=False),
                Quantity("n_atoms_per_cell", r' N\. OF ATOMS PER CELL\s+' + integer_c, repeats=False),
                Quantity("n_shells", r' NUMBER OF SHELLS\s+' + integer_c, repeats=False),
                Quantity("n_ao", r' NUMBER OF AO\s+' + integer_c, repeats=False),
                Quantity("n_electrons", r' N\. OF ELECTRONS PER CELL\s+' + integer_c, repeats=False),
                Quantity("n_core_electrons", r' CORE ELECTRONS PER CELL\s+' + integer_c, repeats=False),
                Quantity("n_symmops", r' N\. OF SYMMETRY OPERATORS\s+' + integer_c, repeats=False),
                Quantity("tol_coulomb_overlap", r' COULOMB OVERLAP TOL\s+\(T1\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("tol_coulomb_penetration", r' COULOMB PENETRATION TOL\s+\(T2\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("tol_exchange_overlap", r' EXCHANGE OVERLAP TOL\s+\(T3\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("tol_pseudo_overlap_f", r' EXCHANGE PSEUDO OVP \(F\(G\)\)\s+\(T4\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("tol_pseudo_overlap_p", r' EXCHANGE PSEUDO OVP \(P\(G\)\)\s+\(T5\) ' + flt_crystal_c, str_operation=to_float, repeats=False),
                Quantity("pole_order", r' POLE ORDER IN MONO ZONE\s+' + integer_c, repeats=False),
                Quantity("calculation_type", r' TYPE OF CALCULATION \:\s+(.*?\n\s+.*?)\n', str_operation=lambda x: " ".join(x.split()), repeats=False),
                Quantity('xc_functional', r' \(EXCHANGE\)\[CORRELATION\] FUNCTIONAL:(\(.+\)\[.+\])\n', str_operation=lambda x: x, repeats=False,),
                Quantity("cappa", r'CAPPA:IS1\s+' + integer_c + r';IS2\s+' + integer_c + r';IS3\s+' + integer_c + '; K PTS MONK NET\s+' + integer_c + r'; SYMMOPS:K SPACE\s+' + integer_c + ';G SPACE\s+' + integer_c, repeats=False),
                Quantity('scf_max_iteration', r' MAX NUMBER OF SCF CYCLES\s+' + integer_c, repeats=False),
                Quantity('convergenge_deltap', r'CONVERGENCE ON DELTAP\s+' + flt_crystal_c, str_operation=to_float, repeats=False), Quantity('weight_f', r'WEIGHT OF F\(I\) IN F\(I\+1\)\s+' + integer_c, repeats=False),
                Quantity('scf_threshold_energy_change', r'CONVERGENCE ON ENERGY\s+' + flt_crystal_c, str_operation=to_float, repeats=False, unit=ureg.hartree),
                Quantity('shrink', r'SHRINK\. FACT\.\(MONKH\.\)\s+(' + integer + ws + integer + ws + integer + r')', repeats=False),
                Quantity('n_k_points_ibz', r'NUMBER OF K POINTS IN THE IBZ\s+' + integer_c, repeats=False),
                Quantity('shrink_gilat', r'SHRINKING FACTOR\(GILAT NET\)\s+' + integer_c, repeats=False),
                Quantity('n_k_points_gilat', r'NUMBER OF K POINTS\(GILAT NET\)\s+' + integer_c, repeats=False),

                # SCF
                Quantity(
                    "scf_block",
                    r' CHARGE NORMALIZATION FACTOR([\s\S]*?) == SCF ENDED',
                    sub_parser=UnstructuredTextFileParser(quantities=[
                        Quantity(
                            'scf_iterations',
                            r'( CHARGE NORMALIZATION FACTOR[\s\S]*? TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT PDIG)',
                            sub_parser=UnstructuredTextFileParser(quantities=[
                                Quantity('charge_normalization_factor', fr' CHARGE NORMALIZATION FACTOR{ws}{flt}\n', repeats=False),
                                Quantity('total_atomic_charges', fr' TOTAL ATOMIC CHARGES:\n(?:{ws}{flt})+\n', repeats=False),
                                Quantity('QGAM', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT QGAM        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}\n', repeats=False),
                                Quantity('BIEL2', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT BIEL2        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}\n', repeats=False),
                                Quantity('TOTENY', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT TOTENY        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}\n', repeats=False),
                                Quantity('integrated_density', fr' NUMERICALLY INTEGRATED DENSITY{ws}{flt}\n', repeats=False),
                                Quantity('NUMDFT', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT NUMDFT        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}\n', repeats=False),
                                Quantity('energies', fr' CYC{ws}{integer}{ws}ETOT\(AU\){ws}{flt_c}{ws}DETOT{ws}{flt_c}{ws}tst{ws}{flt}{ws}PX{ws}{flt}\n', repeats=False, dtype=np.float64, unit=ureg.hartree),
                                Quantity('FDIK', fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT FDIK        TELAPSE{ws}{flt}{ws}TCPU{ws}{flt}\n', repeats=False),
                            ]),
                            repeats=True,
                        ),
                    ]),
                    repeats=False,
                ),
                Quantity('number_of_scf_iterations', r' == SCF ENDED - CONVERGENCE ON ENERGY      E\(AU\)' + ws + flt + ws + r'CYCLES' + ws + integer_c, repeats=False),
                Quantity(
                    'energy_total',
                    r' TOTAL ENERGY\(DFT|HF\)\(AU\)\(' + ws + integer + r'\)' + ws + flt_c + ws + 'DE' + flt + ws + 'tester|tst' + ws + flt,
                    unit=ureg.hartree,
                    repeats=False,
                ),

                # Geometry optimization steps
                Quantity(
                    "geo_opt",
                    re.escape(r' *******************************************************************************') + r'\n' +
                    r' \*                             OPTIMIZATION STARTS                             \*\n' +
                    r'([\s\S]*?' + 
                    re.escape(r' ******************************************************************') + r'\n' +
                    fr'\s*\* OPT END - CONVERGED \* E\(AU\)\:\s+{flt}\s+POINTS\s+{integer})\s+\*\n',
                    sub_parser=UnstructuredTextFileParser(quantities=[
                        Quantity(
                            'geo_opt_step',
                            fr' COORDINATE AND CELL OPTIMIZATION - POINT\s+{integer}\n' +
                            fr'([\s\S]*?)' +
                            fr' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT OPTI',
                            sub_parser=UnstructuredTextFileParser(quantities=[
                                Quantity(
                                    'lattice_parameters',
                                    fr' PRIMITIVE CELL - CENTRING CODE [\s\S]*?VOLUME=\s*{flt} - DENSITY\s*{flt} g/cm\^3\n' +
                                    fr'         A              B              C           ALPHA      BETA       GAMMA\s*' +
                                    fr'{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\s+{flt_c}\n',
                                    shape=(6),
                                    dtype=np.float64,
                                    repeats=False,
                                ),
                                Quantity(
                                    "labels_positions",
                                    fr' ATOMS IN THE ASYMMETRIC UNIT\s+{integer} - ATOMS IN THE UNIT CELL:\s+{integer}\n' +
                                    fr'     ATOM              X/A                 Y/B                 Z/C\s*\n' +
                                    re.escape(' *******************************************************************************') +
                                    fr'((?:\s+{integer}\s+(?:T|F)\s+{integer}\s+[\s\S]*?\s+{flt}\s+{flt}\s+{flt}\n)+)',
                                    shape=(-1, 7),
                                    dtype=str,
                                    repeats=False,
                                ),
                                Quantity('energy', fr' TOTAL ENERGY\({word}\)\(AU\)\(\s*{integer}\)\s*{flt_c}', repeats=False),
                            ]),
                            repeats=True,
                        ),
                        Quantity('converged', fr' \* OPT END - ([\s\S]*?) \* E\(AU\)\:\s+{flt}\s+POINTS\s+{integer}\s+\*\n', repeats=False),
                    ]),
                    repeats=False,
                ),

                # Band structure
                Quantity(
                    "band_structure",
                    re.escape(r' *******************************************************************************') + r'\n' +
                    fr' \*                                                                             \*\n' +
                    r' \*  BAND STRUCTURE                                                             \*\n' +
                    r'[\s\S]*?' + 
                    fr' \*  FROM BAND\s+{integer} TO BAND\s+{integer}\s+\*\n' +
                    fr' \*  TOTAL OF\s+{integer} K-POINTS ALONG THE PATH\s+\*\n' +
                    fr' \*                                                                             \*\n' +
                    re.escape(r' *******************************************************************************') + r'\n' +
                    r'([\s\S]*?' + 
                    fr' ENERGY RANGE \(A\.U\.\)\s*{flt} - \s*{flt} EFERMI\s*{flt_c}\n)',
                    sub_parser=UnstructuredTextFileParser(quantities=[
                        Quantity(
                            'segments',
                            fr' (LINE\s+{integer} \( {flt} {flt} {flt}: {flt} {flt} {flt}\) IN TERMS OF PRIMITIVE LATTICE VECTORS\n' +
                            fr'\s+{integer} POINTS - SHRINKING_FACTOR {integer}\n' +
                            fr' CARTESIAN COORD\.\s+\( {flt} {flt} {flt}\):\( {flt} {flt} {flt}\) STEP\s+{flt}\n\n\n' +
                            fr'(?:\s+{integer}\([\d/\s]+?\)\n' +
                            fr'(?:\s*{flt})+\n\n)+)',
                            sub_parser=UnstructuredTextFileParser(quantities=[
                                Quantity(
                                    'start_end',
                                    fr'LINE\s+{integer} \( {flt_c} {flt_c} {flt_c}: {flt_c} {flt_c} {flt_c}\) IN TERMS OF PRIMITIVE LATTICE VECTORS\n',
                                    type=np.float64,
                                    shape=(2, 3),
                                    repeats=False,
                                ),
                                Quantity(
                                    'shrinking_factor',
                                    fr'\s+{integer} POINTS - SHRINKING_FACTOR {integer_c}\n',
                                    repeats=False,
                                ),
                                Quantity(
                                    'intervals',
                                    fr'\s+{integer}\(\s*([\d/\s]+?)\)\n' +
                                    fr'(?:\s*{flt})+\n\n',
                                    str_operation=lambda x: x,
                                    repeats=True,
                                ),
                            ]),
                            repeats=True,
                        ),
                        Quantity("fermi_energy", fr' ENERGY RANGE \(A\.U\.\)\s*{flt} - \s*{flt} EFERMI\s*{flt_c}', unit=ureg.hartree, repeats=False),
                    ]),
                    repeats=False,
                ),

                # Forces
                Quantity(
                    'forces',
                    r' CARTESIAN FORCES IN HARTREE/BOHR \(ANALYTICAL\)\n'
                    r'   ATOM                     X                   Y                   Z\n' + 
                    r'((?:' + ws + integer + ws + integer + ws + flt + ws + flt + ws + flt + r'\n)*)',
                    shape=(-1, 5),
                    dtype=str,
                    repeats=False,
                ),
                Quantity("end_timestamp", r' EEEEEEEEEE TERMINATION  DATE\s+(.*? TIME .*?)\n', str_operation=lambda x: x, repeats=False),
            ]
        )

        return outputparser

    def parse(self, filepath, archive, logger):
        # Read files
        out = self.parse_output(filepath)

        # Run
        run = archive.m_create(section_run)
        run.program_name = 'Crystal'
        run.program_version = out["program_version"]
        run.program_basis_set_type = 'gaussians'
        run.electronic_structure_method = 'DFT'
        run.x_crystal_datetime = out["datetime"]
        run.x_crystal_hostname = out["hostname"]
        run.x_crystal_user = out["user"]
        run.x_crystal_os = out["os"]
        run.x_crystal_input_path = out["input_path"]
        run.x_crystal_output_path = out["output_path"]
        run.x_crystal_tmpdir = out["tmpdir"]
        run.x_crystal_executable_path = out["executable_path"]
        distribution = out["distribution"]
        dist, rest = distribution.split(" : ", 1)
        minor, rest = rest.split(" - ", 1)
        run.x_crystal_distribution = dist
        run.x_crystal_version_minor = minor
        run.x_crystal_version_date = rest
        title = out["title"]
        if title is not None:
            run.x_crystal_run_title = title.strip()
        run.time_run_date_start = to_unix_time(out["start_timestamp"])
        run.time_run_date_end = to_unix_time(out["end_timestamp"])

        # System
        system = run.m_create(section_system)
        lattice_parameters = out["lattice_parameters"]
        if lattice_parameters is None:
            lattice_parameters = out["lattice_parameters_restart"]
        labels_positions = out["labels_positions"]
        if labels_positions is None:
            labels_positions = out["labels_positions_restart"]
            atomic_numbers = labels_positions[:, 1].astype(np.int)
            scaled_pos = labels_positions[:, 4:7].astype(np.float64)
        else:
            atomic_numbers = labels_positions[:, 2].astype(np.int)
            scaled_pos = labels_positions[:, 4:7].astype(np.float64)

        cart_positions, lattice_vectors = to_system(lattice_parameters, scaled_pos)
        system.lattice_vectors = lattice_vectors
        system.atom_positions = cart_positions
        system.atom_species = atomic_numbers
        dimensionality = out["dimensionality"]
        pbc = np.array([False, False, False])
        pbc[0:dimensionality] = True
        system.configuration_periodic_dimensions = pbc

        # Method
        method = run.m_create(section_method)
        method.scf_max_iteration = out["scf_max_iteration"]
        method.scf_threshold_energy_change = out["scf_threshold_energy_change"]
        dftd3 = out["dftd3"]
        if dftd3:
            if dftd3["version"] == "VERSION 2":
                method.van_der_Waals_method = "G06"
            else:
                method.van_der_Waals_method = "DFT-D3"
        if out["grimme"]:
            method.van_der_Waals_method = "G06"
            
        # Try to primarily read the methodology from input
        dft = out["dft"]
        if dft:
            exchange = dft["exchange"]
            correlation = dft["correlation"]
            exchange_correlation = dft["exchange_correlation"]
            functionals = to_libxc(exchange, correlation, exchange_correlation)
            if functionals:
                for xc in functionals:
                    method.m_add_sub_section(section_method.section_XC_functionals, xc)
                method.XC_functional = to_libxc_name(functionals)
        # If methodology not reported in input, try to read from output
        else:
            hamiltonian_type = out["hamiltonian_type"]
            if hamiltonian_type == "HARTREE-FOCK HAMILTONIAN":
                xc = section_XC_functionals()
                xc.XC_functional_name = "HF_X"
                xc.XC_functional_weight = 1.0
                method.m_add_sub_section(section_method.section_XC_functionals, xc)
                method.XC_functional = to_libxc_name([xc])
            elif hamiltonian_type == "KOHN-SHAM HAMILTONIAN":
                xc_output = out["xc_out"]
                hybrid = out["hybrid_out"]
                functionals = to_libxc_out(xc_output, hybrid)
                if functionals:
                    for xc in functionals:
                        method.m_add_sub_section(section_method.section_XC_functionals, xc)
                    method.XC_functional = to_libxc_name(functionals)

        method.x_crystal_fock_ks_matrix_mixing = out["fock_ks_matrix_mixing"]
        method.x_crystal_coulomb_bipolar_buffer = out["coulomb_bipolar_buffer"]
        method.x_crystal_exchange_bipolar_buffer = out["exchange_bipolar_buffer"]
        method.x_crystal_toldee = out["toldee"]
        method.x_crystal_n_atoms = out["n_atoms_per_cell"]
        method.x_crystal_n_shells = out["n_shells"]
        method.x_crystal_n_orbitals = out["n_ao"]
        method.x_crystal_n_electrons = out["n_electrons"]
        method.x_crystal_n_core_electrons = out["n_core_electrons"]
        method.x_crystal_n_symmops = out["n_symmops"]
        method.x_crystal_tol_coulomb_overlap = out["tol_coulomb_overlap"]
        method.x_crystal_tol_coulomb_penetration = out["tol_coulomb_penetration"]
        method.x_crystal_tol_exchange_overlap = out["tol_exchange_overlap"]
        method.x_crystal_tol_pseudo_overlap_f = out["tol_pseudo_overlap_f"]
        method.x_crystal_tol_pseudo_overlap_p = out["tol_pseudo_overlap_p"]
        method.x_crystal_pole_order = out["pole_order"]
        method.x_crystal_type_of_calculation = out["calculation_type"]
        cappa = out["cappa"]
        method.x_crystal_is1 = cappa[0]
        method.x_crystal_is2 = cappa[1]
        method.x_crystal_is3 = cappa[2]
        method.x_crystal_k_pts_monk_net = cappa[3]
        method.x_crystal_symmops_k = cappa[4]
        method.x_crystal_symmops_g = cappa[5]
        method.x_crystal_weight_f = out["weight_f"]
        method.x_crystal_shrink = out["shrink"]
        method.x_crystal_shrink_gilat = out["shrink_gilat"]
        method.x_crystal_convergence_deltap = out["convergenge_deltap"]
        method.x_crystal_n_k_points_ibz = out["n_k_points_ibz"]
        if out["n_k_points_gilat"] is not None: method.x_crystal_n_k_points_gilat = out["n_k_points_gilat"]
        basis_set = out["basis_set"]
        covered_species = set()
        if basis_set is not None:
            for bs in basis_set["basis_sets"]:
                atomic_number = to_atomic_number(bs["species"][1])
                shells = bs["shells"]
                if atomic_number != covered_species and shells is not None:
                    section_basis_set = section_basis_set_atom_centered()
                    section_basis_set.basis_set_atom_number = atomic_number
                    run.m_add_sub_section(section_run.section_basis_set_atom_centered, section_basis_set)
                    covered_species.add(atomic_number)
                    for shell in shells:
                        section_shell = x_crystal_section_shell()
                        section_shell.x_crystal_shell_range = str(shell["shell_range"])
                        section_shell.x_crystal_shell_type = shell["shell_type"]
                        section_shell.x_crystal_shell_coefficients = np.array(shell["shell_coefficients"])
                        section_basis_set.m_add_sub_section(section_basis_set_atom_centered.x_crystal_section_shell, section_shell)

        # SCC
        scc = run.m_create(section_single_configuration_calculation)
        scf_block = out["scf_block"]
        if scf_block is not None:
            number_of_scf_iterations = out["number_of_scf_iterations"]
            scc.single_configuration_calculation_converged = number_of_scf_iterations is not None
            scc.number_of_scf_iterations = number_of_scf_iterations
            for scf in scf_block["scf_iterations"]:
                energies = scf["energies"]
                section_scf = section_scf_iteration()
                section_scf.energy_total_scf_iteration = energies[0]
                section_scf.energy_change_scf_iteration = energies[1]
                scc.m_add_sub_section(section_single_configuration_calculation.section_scf_iteration, section_scf)

        scc.energy_total = out["energy_total"]
        forces = out["forces"]
        if forces is not None:
            scc.atom_forces = forces[:, 2:].astype(float) * ureg.hartree/ureg.bohr
        scc.single_configuration_calculation_to_system_ref = system
        scc.single_configuration_to_calculation_method_ref = method

        # Band structure
        band_structure = out["band_structure"]
        if band_structure is not None:
            section_band = section_k_band()
            section_band.reciprocal_cell = atomutils.reciprocal_cell(system.lattice_vectors.magnitude)*1/ureg.meter
            fermi_energy = band_structure["fermi_energy"]
            if fermi_energy is not None:
                scc.energy_reference_fermi = fermi_energy
            segments = band_structure["segments"]
            for segment in segments:
                section_segment = section_k_band_segment()
                start_end = segment["start_end"]
                shrinking_factor = segment["shrinking_factor"]
                intervals = segment["intervals"]
                k_points = to_k_points(shrinking_factor, intervals)
                section_segment.band_k_points = k_points
                section_segment.band_segm_start_end = start_end
                section_segment.number_of_k_points_per_segment = k_points.shape[0]
                section_band.m_add_sub_section(section_k_band.section_k_band_segment, section_segment)

            # Read energies from the f25-file.
            # TODO

            scc.m_add_sub_section(section_single_configuration_calculation.section_k_band, section_band)

        # Sampling
        geo_opt = out["geo_opt"]
        if geo_opt is not None:
            steps = geo_opt["geo_opt_step"]
            if steps is not None:
                sampling_method = section_sampling_method()
                sampling_method.sampling_method = "geometry_optimization"
                sampling_method.geometry_optimization_energy_change = out["energy_change"]
                sampling_method.geometry_optimization_geometry_change = out["geometry_change"]
                run.m_add_sub_section(section_run.section_sampling_method, sampling_method) 
                fs = section_frame_sequence()
                run.m_add_sub_section(section_run.section_frame_sequence, fs) 

                # First step is special: it refers to the initial system which
                # was printed before entering the geometry optimization loop.
                i_system = system
                i_energy = steps[0]["energy"]
                scc.energy_total = i_energy

                frames = []
                for step in steps[1:]:
                    i_scc = section_single_configuration_calculation()
                    i_system = section_system()
                    i_energy = step["energy"]
                    i_labels_positions = step["labels_positions"]
                    i_lattice_parameters = step["lattice_parameters"]
                    i_atomic_numbers = i_labels_positions[:, 2].astype(np.int)
                    i_scaled_pos = i_labels_positions[:, 4:8].astype(np.float64)
                    i_cart_pos, i_lattice_vectors = to_system(i_lattice_parameters, i_scaled_pos)
                    i_system.atom_species = i_atomic_numbers
                    i_system.atom_positions = i_cart_pos
                    i_system.lattice_vectors = i_lattice_vectors
                    i_system.configuration_periodic_dimensions = pbc
                    i_scc.energy_total = i_energy

                    i_scc.single_configuration_calculation_to_system_ref = i_system
                    i_scc.single_configuration_to_calculation_method_ref = method

                    run.m_add_sub_section(section_run.section_system, i_system)
                    run.m_add_sub_section(section_run.section_single_configuration_calculation, i_scc)
                    frames.append(i_scc)

                fs.frame_sequence_local_frames_ref = frames
                fs.number_of_frames_in_sequence = len(fs.frame_sequence_local_frames_ref)
                fs.frame_sequence_to_sampling_ref = sampling_method
                fs.geometry_optimization_converged = geo_opt["converged"] == "CONVERGED"


def to_k_points(sf, intervals):
    """Converts the k-path intervals reported by Crystal into scaled k-points.
    """
    regex = re.compile(fr'{integer_c}/{sf}\s*{integer_c}/{sf}\s*{integer_c}/{sf}')
    k_points = []
    for interval in intervals:
        match = regex.match(interval)
        groups = match.groups()
        k_point = [int(x)/sf for x in groups]
        k_points.append(k_point)
    return np.array(k_points)


def to_system(lattice_parameters, scaled_pos):
    """Converts the primitive cell reported by Crystal into the corresponding
    species, cartesian positions and lattice vectors.
    """
    lattice_vectors = atomutils.cellpar_to_cell(lattice_parameters, degrees=True)
    wrapped_pos = atomutils.wrap_positions(scaled_pos)
    cart_pos = atomutils.to_cartesian(wrapped_pos, lattice_vectors)

    return cart_pos * ureg.angstrom, lattice_vectors * ureg.angstrom


def to_float(value):
    """Transforms the Crystal-specific float notation into a floating point
    number.
    """
    base, exponent = value.split("**")
    base = int(base)
    exponent = int("".join(exponent.split()))
    return pow(base, exponent)


def to_atomic_number(value):
    """Given a Crystal specific uppercase species name, returns the
    corresponding atomic number.
    """
    symbol = value.lower().capitalize()
    atomic_number = ase.data.atomic_numbers[symbol]
    return atomic_number


def to_unix_time(value):
    """Transforms the Crystal-specific float notation into a floating point
    number.
    """
    if value is None:
        return None

    value = value.strip()
    date_time_obj = datetime.datetime.strptime(value, '%d %m %Y TIME %H:%M:%S.%f')
    return date_time_obj.timestamp()


def to_libxc(exchange, correlation, exchange_correlation):
    """Transforms the Crystal-specific XC naming into a list of
    section_XC_functionals.
    """
    xc_list = []

    # Handle the XC's defined with single shortcut
    if exchange_correlation:
        exchange_correlation = exchange_correlation.upper()
        shortcut_map = {
            "PBE0": "HYB_GGA_XC_PBEH",
            "B3LYP": "HYB_GGA_XC_B3LYP",
            "HSE06": "HYB_GGA_XC_HSE06",
            "M06": "HYB_MGGA_XC_M06",
            "M05-2X": "HYB_MGGA_XC_M05_2X",
            "LC-WPBE": "HYB_GGA_XC_LRC_WPBE",
        }
        norm_xc = shortcut_map.get(exchange_correlation)
        if norm_xc:
            xc_list.append(norm_xc)

    # Handle the exchange part
    if exchange:
        exchange = exchange.upper()
        exchange_map = {
            "PBE": "GGA_X_PBE",
            "PBESOL": "GGA_X_PBE_SOL",
            "BECKE": "GGA_X_B88",
            "LDA": "LDA_X",
            "PWGGA": "GGA_X_PW91",
        }
        norm_x = exchange_map.get(exchange)
        if norm_x:
            xc_list.append(norm_x)

    # Handle the correlation part
    if correlation:
        correlation = correlation.upper()
        correlation_map = {
            "PBE": "GGA_C_PBE",
            "PBESOL": "GGA_C_PBE_SOL",
            "PZ": "LDA_C_PZ",
            "WFN": "LDA_C_VWN",
            "PWGGA": "GGA_C_PW91",
        }
        norm_c = correlation_map.get(correlation)
        if norm_c:
            xc_list.append(norm_c)

    # Go throught the XC list and add the sections and gather a summary
    functionals = []
    for xc in xc_list:
        section = section_XC_functionals()
        weight = 1.0
        section.XC_functional_name = xc
        section.XC_functional_weight = weight
        functionals.append(section)

    return functionals

def to_libxc_out(xc, hybridization):
    """Transforms the Crystal-specific XC naming in the output into a list of
    section_XC_functionals.
    """
    xc_list = []
    exchange, correlation = xc[1:-1].split(")[")

    # Handle the exchange part
    if exchange:
        exchange = exchange.upper()
        exchange_map = {
            "PERDEW-BURKE-ERNZERHOF": "GGA_X_PBE",
        }
        norm_x = exchange_map.get(exchange)
        if norm_x:
            xc_list.append(norm_x)

    # Handle the correlation part
    if correlation:
        correlation = correlation.upper()
        correlation_map = {
            "PERDEW-BURKE-ERNZERHOF": "GGA_C_PBE",
        }
        norm_c = correlation_map.get(correlation)
        if norm_c:
            xc_list.append(norm_c)

    # Shortcuts
    if norm_x == "GGA_X_PBE" and norm_c == "GGA_C_PBE" and hybridization == 25.00:
        xc_list = ["HYB_GGA_XC_PBEH"]

    # Go throught the XC list and add the sections and gather a summary
    functionals = []
    for xc in xc_list:
        section = section_XC_functionals()
        weight = 1.0
        section.XC_functional_name = xc
        section.XC_functional_weight = weight
        functionals.append(section)

    return functionals


def to_libxc_name(functionals):
    """Given a list of section_XC_functionals, returns the single string that
    represents them all.
    """
    return "+".join(sorted(["{}*{}".format(x.XC_functional_weight, x.XC_functional_name) for x in functionals]))