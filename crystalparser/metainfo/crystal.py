#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import numpy as np            # pylint: disable=unused-import
import typing                 # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference
)
from nomad.metainfo.legacy import LegacyDefinition

from nomad.datamodel.metainfo import public

m_package = Package(
    name='crystal_nomadmetainfo_json',
    description='None',
    a_legacy=LegacyDefinition(name='crystal.nomadmetainfo.json'))


class section_system(public.section_system):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_system'))

    x_crystal_family = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal family.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_family'))

    x_crystal_class = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal class.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_class'))

    x_crystal_spacegroup = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal spacegroup string resembling Hermann–Mauguin notation.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_spacegroup'))

    x_crystal_dimensionality = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        System dimensionality.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_dimensionality'))

    x_crystal_n_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of symmetry operators.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_number_of_symmops'))


class section_scf_iteration(public.section_scf_iteration):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_scf_iteration'))

    x_crystal_scf_ee = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL E-E
        4.6595142576204E+01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_total_ee'))

    x_crystal_scf_en_ne = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL E-N + N-E
        -5.2283101954878E+02
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_total_en_ne'))

    x_crystal_scf_nn = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL N-N
        -7.3084276676762E+01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_total_nn'))

    x_crystal_scf_virial_coefficient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: VIRIAL COEFFICIENT
        9.9998501747632E-01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_virial_coefficient'))


class section_run(public.section_run):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_run'))

    x_crystal_run_title = Quantity(
        type=str,
        shape=[],
        description='''
        Title of the runcry(14) task.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_run_title'))

    x_crystal_datetime = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary type for storing date and time, in locale-dependent format.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_datetime'))

    x_crystal_executable_path = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal executable filepath.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_exe'))

    x_crystal_hostname = Quantity(
        type=str,
        shape=[],
        description='''
        Hostname where Crystal was run.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_hn'))

    x_crystal_input_path = Quantity(
        type=str,
        shape=[],
        description='''
        Input file name.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_input'))

    x_crystal_os = Quantity(
        type=str,
        shape=[],
        description='''
        String describing the operating system where Crystal was run.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_os'))

    x_crystal_output = Quantity(
        type=str,
        shape=[],
        description='''
        Output file name.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_output'))

    x_crystal_tmpdir = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary directory.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_tmpdir'))

    x_crystal_user = Quantity(
        type=str,
        shape=[],
        description='''
        Username: who ran Crystal.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_user'))

    x_crystal_distribution = Quantity(
        type=str,
        shape=[],
        description='''
        Distribution describer.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_header_distribution'))

    x_crystal_version_minor = Quantity(
        type=str,
        shape=[],
        description='''
        Minor version number of Crystal.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_header_minor'))


class section_method(public.section_method):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_method'))

    x_crystal_convergence_deltap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence seettings, on power of 10 (e.g. CONVERGENCE ON DELTAP        10**-16)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_convergence_on_deltap'))

    x_crystal_weight_f = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        WEIGHT OF F(I) IN F(I+1)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_weight_f'))

    x_crystal_coulomb_bipolar_buffer = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        COULOMB BIPOLAR BUFFER SET TO x Mb
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_coulomb_bipolar_buffer'))

    x_crystal_eigenvectors_disk_space_ftn = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        DISK SPACE FOR EIGENVECTORS (FTN 10)      351575 REALS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_eigenvectors_disk_space_ftn'))

    x_crystal_eigenvectors_disk_space_reals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        DISK SPACE FOR EIGENVECTORS (FTN 10)      351575 REALS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_eigenvectors_disk_space_reals'))

    x_crystal_exchange_bipolar_buffer = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE BIPOLAR BUFFER SET TO x Mb
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_exchange_bipolar_buffer'))

    x_crystal_fock_ks_matrix_mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FOCK/KS MATRIX MIXING SET TO x %
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_fock_ks_matrix_mixing'))

    x_crystal_input_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT INPUT       TELAPSE        0.01 TCPU        0.01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_input_tcpu'))

    x_crystal_input_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT INPUT       TELAPSE        0.01 TCPU        0.01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_input_telapse'))

    x_crystal_irr_f = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_irr_f'))

    x_crystal_irr_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_irr_p'))

    x_crystal_is1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_is1'))

    x_crystal_is2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_is2'))

    x_crystal_is3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_is3'))

    x_crystal_n_k_points_gilat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF K POINTS(GILAT NET)    145
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_k_points_gilat'))

    x_crystal_n_k_points_ibz = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF K POINTS IN THE IBZ    145
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_k_points_ibz'))

    x_crystal_k_pts_monk_net = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_k_pts_monk_net'))

    x_crystal_matrix_size_f = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_matrix_size_f'))

    x_crystal_matrix_size_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_matrix_size_p'))

    x_crystal_max_g_vector_index = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAX G-VECTOR INDEX FOR 1- AND 2-ELECTRON INTEGRALS 247
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_max_g_vector_index'))

    x_crystal_max_scf_cycles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAX NUMBER OF SCF CYCLES
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_max_scf_cycles'))

    x_crystal_n_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF ATOMS PER CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_atoms'))

    x_crystal_n_core_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CORE ELECTRONS PER CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_core_electrons'))

    x_crystal_n_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF ELECTRONS PER CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_electrons'))

    x_crystal_n_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF AO (Atomic orbitals)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_orbitals'))

    x_crystal_n_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF SHELLS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_shells'))

    x_crystal_n_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF SYMMETRY OPERATORS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_symmops'))

    x_crystal_pole_order = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        POLE ORDER IN MONO ZONE
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_pole_order'))

    x_crystal_shrink_gilat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        SHRINKING FACTOR(GILAT NET)   16
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink_gilat'))

    x_crystal_shrink_value1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink_value1'))

    x_crystal_shrink_value2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink_value2'))

    x_crystal_shrink_value3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink_value3'))

    x_crystal_shrink = Quantity(
        type=np.dtype(np.int32),
        shape=[3],
        description='''
        SHRINK. FACT.(MONKH.)   16 16 16
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink'))

    x_crystal_symmetry_adaption = Quantity(
        type=bool,
        shape=[],
        description='''
        SYMMETRY ADAPTION OF THE BLOCH FUNCTIONS ENABLED
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_symmetry_adaption'))

    x_crystal_symmops_g = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_symmops_g'))

    x_crystal_symmops_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_symmops_k'))

    x_crystal_tol_coulomb_overlap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        COULOMB OVERLAP TOL         (T1) 10**   -6. (Tolerance T1, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_coulomb_overlap'))

    x_crystal_tol_coulomb_penetration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        COULOMB PENETRATION TOL     (T2) 10**   -6. (Tolerance T2, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_coulomb_penetration'))

    x_crystal_tol_exchange_overlap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE OVERLAP TOL        (T3) 10**   -6. (Tolerance T3, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_exchange_overlap'))

    x_crystal_tol_pseudo_overlap_f = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE PSEUDO OVP (F(G))  (T4) 10**   -6. (Tolerance T4, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_pseudo_overlap_f'))

    x_crystal_tol_pseudo_overlap_p = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE PSEUDO OVP (P(G))  (T5) 10**  -12. (Tolerance T5, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_pseudo_overlap_p'))

    x_crystal_type_of_calculation = Quantity(
        type=str,
        shape=[],
        description='''
        The type of the calculation that was performed.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_type_of_calculation'))

    x_crystal_weight_previous = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        WEIGHT OF F(I) IN F(I+1)      30%
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_weight_previous'))

    x_crystal_toldee = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOLDEE info
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_toldee'))


class section_basis_set_atom_centered(public.section_basis_set_atom_centered):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_basis_set_atom_centered'))

    x_crystal_section_shell = SubSection(
        sub_section=SectionProxy('x_crystal_section_shell'),
        repeats=True
    )


class x_crystal_section_shell(MSection):
    '''
    Shell contains a number of orbitals.
    '''
    m_def = Section(validate=False)

    x_crystal_shell_range = Quantity(
        type=str,
        shape=[],
        description='''
        The range of orbitals
        ''')

    x_crystal_shell_type = Quantity(
        type=str,
        shape=[],
        description='''
        Shell type: S / P / SP / D / F / G.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_shell_type'))

    x_crystal_shell_coefficients = Quantity(
        type=np.dtype(np.float64),
        shape=['n_orbitals', 4],
        description='''
        Contraction coefficients in this order: exponent, S, P, D/F/G.
        '''
    )


m_package.__init_metainfo__()
