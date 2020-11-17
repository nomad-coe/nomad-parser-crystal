import logging
import re
import numpy as np

from nomad.units import ureg
from nomad.parsing.parser import FairdiParser
from nomad.parsing.file_parser import UnstructuredTextFileParser, Quantity
from nomad.datamodel.metainfo.public import section_run, section_method, section_system,\
    section_XC_functionals, section_scf_iteration, section_single_configuration_calculation,\
    section_sampling_method, section_frame_sequence, section_eigenvalues, section_dos,\
    section_atom_projected_dos, section_species_projected_dos, section_k_band,\
    section_k_band_segment, section_energy_van_der_Waals, section_calculation_to_calculation_refs,\
    section_method_to_method_refs
from .metainfo import m_env


def capture(regex):
    return r'(' + regex + r')'

flt = r'-?(?:\d+\.?\d*|\d*\.?\d+)(?:E[\+-]?\d+)?' # Floating point number
flt_c = capture(flt)                              # Captures a floating point number
flt_crystal_c = r'(-?\d+(?:.\d+)?\*\*-?.*\d+)'     # Crystal specific floating point syntax
ws = r'\s+'                                       # Series of white-space characters
br = r'\n'                                        # Line break
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
                # System
                Quantity("dimensionality",
                    r' GEOMETRY FOR WAVE FUNCTION - DIMENSIONALITY OF THE SYSTEM\s+(\d)',
                    repeats=False
                ),
                Quantity(
                    "lattice_vectors",
                    r'\s*DIRECT LATTICE VECTORS CARTESIAN COMPONENTS \(ANGSTROM\)\s*'
                    r'          X                    Y                    Z' +
                    ws + flt_c + ws + flt_c + ws + flt_c + ws +
                    ws + flt_c + ws + flt_c + ws + flt_c + ws +
                    ws + flt_c + ws + flt_c + ws + flt_c + ws,
                    unit=ureg.angstrom,
                    shape=(3, 3),
                    dtype=np.float64,
                    repeats=False,
                ),
                Quantity(
                    'labels_positions',
                    r'\s*CARTESIAN COORDINATES \- PRIMITIVE CELL\s*' + 
                    re.escape(r' *******************************************************************************') + 
                    r'\s*\*      ATOM          X\(ANGSTROM\)         Y\(ANGSTROM\)         Z\(ANGSTROM\)\s*' +
                    re.escape(r' *******************************************************************************') +
                    r'((?:' + ws + integer + ws + integer + ws + word + ws + flt + ws + flt + ws + flt + r'\n)*)',
                    shape=(-1, 6),
                    dtype=str,
                    repeats=False,
                ),
                # Method
                Quantity(
                    'xc_functional',
                    r' \(EXCHANGE\)\[CORRELATION\] FUNCTIONAL:(\(.+\)\[.+\])\n',
                    str_operation=lambda x: x,
                    repeats=False,
                ),
                Quantity(
                    'scf_max_iteration',
                    r' MAX NUMBER OF SCF CYCLES\s+' + integer_c,
                    repeats=False,
                ),
                Quantity(
                    'scf_threshold_energy_change',
                    r' WEIGHT OF F\(I\) IN F\(I\+1\)\s+\d+\%\s+CONVERGENCE ON ENERGY\s+' + flt_crystal_c,
                    str_operation=to_float,
                    repeats=False,
                    unit=ureg.hartree,
                ),
                # SCF
                Quantity(
                    "scf_block",
                    r' CHARGE NORMALIZATION FACTOR([\s\S]*?) == SCF ENDED',
                    sub_parser=UnstructuredTextFileParser(quantities=[
                        Quantity(
                            'scf_iterations',
                            r'( CHARGE NORMALIZATION FACTOR[\s\S]*? TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT PDIG)',
                            sub_parser=UnstructuredTextFileParser(quantities=[
                                Quantity('charge_normalization_factor', r' CHARGE NORMALIZATION FACTOR' + ws + flt + br, repeats=False),
                                Quantity('total_atomic_charges', r' TOTAL ATOMIC CHARGES:\n(?:' + ws + flt + r')+' + br, repeats=False),
                                Quantity('QGAM', r' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT QGAM        TELAPSE' + ws + flt + ws + r'TCPU' + ws + flt + br, repeats=False),
                                Quantity('BIEL2', r' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT BIEL2        TELAPSE' + ws + flt + ws + r'TCPU' + ws + flt + br, repeats=False),
                                Quantity('TOTENY', r' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT TOTENY        TELAPSE' + ws + flt + ws + r'TCPU' + ws + flt + br, repeats=False),
                                Quantity('integrated_density', r' NUMERICALLY INTEGRATED DENSITY' + ws + flt + br, repeats=False),
                                Quantity('NUMDFT', r' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT NUMDFT        TELAPSE' + ws + flt + ws + r'TCPU' + ws + flt + br, repeats=False),
                                Quantity('energies', r' CYC' + ws + integer + ws + r'ETOT\(AU\)' + ws + flt_c + ws + r'DETOT' + ws + flt_c + ws + r'tst' + ws + flt + ws + r'PX' + ws + flt + br, repeats=False, dtype=np.float64, unit=ureg.hartree),
                                Quantity('FDIK', r' TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT FDIK        TELAPSE' + ws + flt + ws + r'TCPU' + ws + flt + br, repeats=False),
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

        # System
        system = run.m_create(section_system)
        system.lattice_vectors = out.lattice_vectors
        system.atom_positions = out.labels_positions[:, 3:].astype(float) * ureg.angstrom
        system.atom_species = out.labels_positions[:, 1].astype(int)
        dimensionality = out.dimensionality
        pbc = np.array([False, False, False])
        pbc[0:dimensionality] = True
        system.configuration_periodic_dimensions = pbc

        # Method
        method = run.m_create(section_method)
        method.scf_max_iteration = out.scf_max_iteration
        method.scf_threshold_energy_change = out.scf_threshold_energy_change
        dftd3 = out["dftd3"]
        if dftd3:
            if dftd3["version"] == "VERSION 2":
                method.van_der_Waals_method = "G06"
            else:
                method.van_der_Waals_method = "DFT-D3"
        if out["grimme"]:
            method.van_der_Waals_method = "G06"
            
        dft = out["dft"]
        if dft:
            exchange = dft["exchange"]
            correlation = dft["correlation"]
            exchange_correlation = dft["exchange_correlation"]
            functionals = to_libxc(exchange, correlation, exchange_correlation)
            for xc in functionals:
                method.m_add_sub_section(section_method.section_XC_functionals, xc)
            method.XC_functional = "+".join(sorted(["{}*{}".format(x.XC_functional_weight, x.XC_functional_name) for x in functionals]))

        # SCC
        scf_block = out["scf_block"]
        number_of_scf_iterations = out["number_of_scf_iterations"]
        scc = run.m_create(section_single_configuration_calculation)
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


def to_float(value):
    """Transforms the Crystal-specific float notation into a floating point
    number.
    """
    base, exponent = value.split("**")
    base = int(base)
    exponent = int("".join(exponent.split()))
    return pow(base, exponent)

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
