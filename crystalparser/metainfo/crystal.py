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


class x_crystal_section_bands_line_point(MSection):
    '''
    A particular point in a line: 1(  0/456  0/456  0/456)
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_bands_line_point'))

    x_crystal_bands_line_point_coordinates = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        fractional coordinates of the point: 1(  0/456  0/456  0/456)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_point_coordinates'))

    x_crystal_bands_line_point_energies = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Energy of each band
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_point_energies'))

    x_crystal_bands_line_point_integer1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_point_integer1'))

    x_crystal_bands_line_point_integer2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_point_integer2'))

    x_crystal_bands_line_point_integer3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_point_integer3'))

    x_crystal_bands_line_point_integer4 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_point_integer4'))

    x_crystal_bands_line_point_integer5 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_point_integer5'))

    x_crystal_bands_line_point_integer6 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_point_integer6'))

    x_crystal_bands_line_point_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of the point: 1(  0/456  0/456  0/456)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_point_number'))


class x_crystal_section_bands_line(MSection):
    '''
    A particular line in band structure calculation
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_bands_line'))

    x_crystal_bands_line_coordinates_cartesian_begin = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        CARTESIAN COORD. ( 0.000 0.000 0.000):( 0.000 0.590 0.000) STEP  0.0310
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_coordinates_cartesian_begin'))

    x_crystal_bands_line_coordinates_cartesian_end = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        CARTESIAN COORD. ( 0.000 0.000 0.000):( 0.000 0.590 0.000) STEP  0.0310
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_coordinates_cartesian_end'))

    x_crystal_bands_line_coordinates_primitive_begin = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        LINE  1 ( 0.00 0.00 0.00: 0.50 0.00 0.50) IN TERMS OF PRIMITIVE LATTICE VECTORS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_coordinates_primitive_begin'))

    x_crystal_bands_line_coordinates_primitive_end = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        LINE  1 ( 0.00 0.00 0.00: 0.50 0.00 0.50) IN TERMS OF PRIMITIVE LATTICE VECTORS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_coordinates_primitive_end'))

    x_crystal_bands_line_number_of_points = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        20 POINTS - SHRINKING_FACTOR 456
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_number_of_points'))

    x_crystal_bands_line_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        LINE  1 ( 0.00 0.00 0.00: 0.50 0.00 0.50) IN TERMS OF PRIMITIVE LATTICE VECTORS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_number'))

    x_crystal_bands_line_shrink = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        20 POINTS - SHRINKING_FACTOR 456
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_shrink'))

    x_crystal_bands_line_step = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CARTESIAN COORD. ( 0.000 0.000 0.000):( 0.000 0.590 0.000) STEP  0.0310
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_step'))

    x_crystal_bands_line_value11 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_value11'))

    x_crystal_bands_line_value12 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_value12'))

    x_crystal_bands_line_value13 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_value13'))

    x_crystal_bands_line_value21 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_value21'))

    x_crystal_bands_line_value22 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_value22'))

    x_crystal_bands_line_value23 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_line_value23'))

    x_crystal_section_bands_line_point = SubSection(
        sub_section=SectionProxy('x_crystal_section_bands_line_point'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_bands_line_point'))


class x_crystal_section_bands(MSection):
    '''
    BAND STRUCTURE
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_bands'))

    x_crystal_bands_energy_fermi = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENERGY RANGE (A.U.) -104.75831 -   0.62475 EFERMI  -0.39686
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_energy_fermi'))

    x_crystal_bands_energy_max = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENERGY RANGE (A.U.) -104.75831 -   0.62475 EFERMI  -0.39686
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_energy_max'))

    x_crystal_bands_energy_min = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENERGY RANGE (A.U.) -104.75831 -   0.62475 EFERMI  -0.39686
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_energy_min'))

    x_crystal_bands_is1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_is1'))

    x_crystal_bands_is2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_is2'))

    x_crystal_bands_is3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_is3'))

    x_crystal_bands_k_pts_monk_net = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_k_pts_monk_net'))

    x_crystal_bands_max = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        FROM BAND   1 TO BAND  18
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_max'))

    x_crystal_bands_min = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        FROM BAND   1 TO BAND  18
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_min'))

    x_crystal_bands_number_of_points = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        TOTAL OF  60 K-POINTS ALONG THE PATH
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_number_of_points'))

    x_crystal_bands_symmops_g = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_symmops_g'))

    x_crystal_bands_symmops_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_symmops_k'))

    x_crystal_bands_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        BAND        TELAPSE        0.11 TCPU        0.11
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_tcpu'))

    x_crystal_bands_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        BAND        TELAPSE        0.11 TCPU        0.11
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_telapse'))

    x_crystal_bands_title = Quantity(
        type=str,
        shape=[],
        description='''
        Title string for the file
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bands_title'))

    x_crystal_section_bands_line = SubSection(
        sub_section=SectionProxy('x_crystal_section_bands_line'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_bands_line'))


class x_crystal_section_basis_set_atom_shell_primitive(MSection):
    '''
    A GTF shell / orbital has a number of gaussian primitives.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_basis_set_atom_shell_primitive'))

    x_crystal_basis_set_atom_shell_primitive_coeff_dfg = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Gaussian primitive: coefficient for d, f or g orbitals.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_shell_primitive_coeff_dfg'))

    x_crystal_basis_set_atom_shell_primitive_coeff_p = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Gaussian primitive: coefficient for p orbitals.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_shell_primitive_coeff_p'))

    x_crystal_basis_set_atom_shell_primitive_coeff_s = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Gaussian primitive: coefficient for s orbitals.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_shell_primitive_coeff_s'))

    x_crystal_basis_set_atom_shell_primitive_exp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Gaussian primitive: exponent.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_shell_primitive_exp'))


class x_crystal_section_basis_set_atom_shell(MSection):
    '''
    Shell contains a number of orbitals.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_basis_set_atom_shell'))

    x_crystal_basis_set_atom_shell_omax = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Orbital number: last orbital.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_shell_omax'))

    x_crystal_basis_set_atom_shell_omin = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Orbital number: first orbital.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_shell_omin'))

    x_crystal_basis_set_atom_shell_type = Quantity(
        type=str,
        shape=[],
        description='''
        Shell type: S / P / SP / D / F / G.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_shell_type'))

    x_crystal_section_basis_set_atom_shell_primitive = SubSection(
        sub_section=SectionProxy('x_crystal_section_basis_set_atom_shell_primitive'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_basis_set_atom_shell_primitive'))


class x_crystal_section_basis_set_atom(MSection):
    '''
    Basis set atom
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_basis_set_atom'))

    x_crystal_basis_set_atom_coordinates = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        Atom element coordinates.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_coordinates'))

    x_crystal_basis_set_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Atom element label.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_element'))

    x_crystal_basis_set_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom id.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_label'))

    x_crystal_basis_set_atom_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_value1'))

    x_crystal_basis_set_atom_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_value2'))

    x_crystal_basis_set_atom_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_basis_set_atom_value3'))

    x_crystal_section_basis_set_atom_shell = SubSection(
        sub_section=SectionProxy('x_crystal_section_basis_set_atom_shell'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_basis_set_atom_shell'))


class x_crystal_section_basis_set(MSection):
    '''
    Basis set with low precision.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_basis_set'))

    x_crystal_section_basis_set_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_basis_set_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_basis_set_atom'))


class x_crystal_section_cell_atom(MSection):
    '''
    Atom in crystallographic cell.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_cell_atom'))

    x_crystal_cell_atom_coordinates = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Atom coordinates.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_atom_coordinates'))

    x_crystal_cell_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Atom in crystallographic cell
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_atom_element'))

    x_crystal_cell_atom_in_asymmetric = Quantity(
        type=bool,
        shape=[],
        description='''
        Atom belongs to the asymmetric unit.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_atom_in_asymmetric'))

    x_crystal_cell_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom in crystallographic cell
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_atom_label'))

    x_crystal_cell_atom_tag = Quantity(
        type=str,
        shape=[],
        description='''
        Atom in crystallographic cell
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_atom_tag'))

    x_crystal_cell_atom_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atom in crystallographic cell: temporary value
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_atom_value1'))

    x_crystal_cell_atom_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atom in crystallographic cell: temporary value
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_atom_value2'))

    x_crystal_cell_atom_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atom in crystallographic cell: temporary value
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_atom_value3'))

    x_crystal_cell_atom_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom in crystallographic cell
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_atom_z'))


class x_crystal_section_cell_symmop(MSection):
    '''
    Symmetry operator.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_cell_symmop'))

    x_crystal_cell_symmop_id = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Symmop id.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_id'))

    x_crystal_cell_symmop_inv = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Id of inversion symmop
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_inv'))

    x_crystal_cell_symmop_rotation = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        Rotation matrix related to the symmop.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_rotation'))

    x_crystal_cell_symmop_translation = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Translation related to the symmop.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_translation'))

    x_crystal_cell_symmop_value10 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value10'))

    x_crystal_cell_symmop_value11 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value11'))

    x_crystal_cell_symmop_value12 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value12'))

    x_crystal_cell_symmop_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value1'))

    x_crystal_cell_symmop_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value2'))

    x_crystal_cell_symmop_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value3'))

    x_crystal_cell_symmop_value4 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value4'))

    x_crystal_cell_symmop_value5 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value5'))

    x_crystal_cell_symmop_value6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value6'))

    x_crystal_cell_symmop_value7 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value7'))

    x_crystal_cell_symmop_value8 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value8'))

    x_crystal_cell_symmop_value9 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Symmop: temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_symmop_value9'))


class x_crystal_section_cell(MSection):
    '''
    Crystallographic lattice
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_cell'))

    x_crystal_cell_number_of_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of symmetry operators
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_number_of_symmops'))

    x_crystal_cell_parameters = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Crystallographic cell: vector lengths and angles.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_parameters'))

    x_crystal_cell_transformation_matrix = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        Crystallographic cell transformation matrix from primitive cell.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_transformation_matrix'))

    x_crystal_cell_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Crystallographic cell volume.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_cell_volume'))

    x_crystal_section_cell_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_cell_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_cell_atom'))

    x_crystal_section_cell_symmop = SubSection(
        sub_section=SectionProxy('x_crystal_section_cell_symmop'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_cell_symmop'))


class x_crystal_section_conventional_cell_atom(MSection):
    '''
    Atom information.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_conventional_cell_atom'))

    x_crystal_conventional_cell_atom_coordinates = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        Atom coordinates.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_atom_coordinates'))

    x_crystal_conventional_cell_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_atom_label'))

    x_crystal_conventional_cell_atom_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Proton number.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_atom_z'))


class x_crystal_section_conventional_cell(MSection):
    '''
    Section for conventional cell parameters
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_conventional_cell'))

    x_crystal_conventional_cell_angles = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Angles between conventional lattice vectors.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_angles'))

    x_crystal_conventional_cell_lengths = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Lengths of conventional lattice vectors.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_lengths'))

    x_crystal_conventional_cell_number_of_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of non-equivalent atoms in the conventional cell.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_number_of_atoms'))

    x_crystal_conventional_cell_units = Quantity(
        type=str,
        shape=[],
        description='''
        Units used for length and angle.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_units'))

    x_crystal_conventional_cell_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_value1'))

    x_crystal_conventional_cell_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_value2'))

    x_crystal_conventional_cell_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_value3'))

    x_crystal_conventional_cell_value4 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_value4'))

    x_crystal_conventional_cell_value5 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_value5'))

    x_crystal_conventional_cell_value6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_conventional_cell_value6'))

    x_crystal_section_conventional_cell_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_conventional_cell_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_conventional_cell_atom'))


class x_crystal_section_endinformation(MSection):
    '''
    runcry14 termination stats (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT END         TELAPSE
    166.54 TCPU      166.18)
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_endinformation'))

    x_crystal_endinformation_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        runcry14 termination stats (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT END
        TELAPSE      166.54 TCPU      166.18)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_endinformation_tcpu'))

    x_crystal_endinformation_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        runcry14 termination stats (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT END
        TELAPSE      166.54 TCPU      166.18)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_endinformation_telapse'))

    x_crystal_run_end_date = Quantity(
        type=str,
        shape=[],
        description='''
        runcry14 termination stats (e.g. EEEEEEEEEE TERMINATION  DATE 26 05 2016 TIME
        13:13:06.4)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_run_end_date'))

    x_crystal_run_end_time = Quantity(
        type=str,
        shape=[],
        description='''
        runcry14 termination stats (e.g. EEEEEEEEEE TERMINATION  DATE 26 05 2016 TIME
        13:13:06.4)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_run_end_time'))


class x_crystal_section_forces_atom(MSection):
    '''
    Atomic forces on a single atom
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_forces_atom'))

    x_crystal_forces_atom_force = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Atomic forces on a single atom
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_atom_force'))

    x_crystal_forces_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label (number), e.g. in 1  11            -2.045495870088E-15
        -2.044980874056E-15 -2.242718650102E-15
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_atom_label'))

    x_crystal_forces_atom_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_atom_value1'))

    x_crystal_forces_atom_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_atom_value2'))

    x_crystal_forces_atom_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_atom_value3'))

    x_crystal_forces_atom_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom proton number, e.g. in 1  11            -2.045495870088E-15
        -2.044980874056E-15 -2.242718650102E-15
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_atom_z'))


class x_crystal_section_forces_born_atom(MSection):
    '''
    ATOMIC BORN CHARGE TENSOR (UNITS OF e, ELECTRON CHARGE).
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_forces_born_atom'))

    x_crystal_forces_born_atom_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atom dynamic charge (e.g. in ATOM   1 NA DYNAMIC CHARGE     0.986361)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_born_atom_charge'))

    x_crystal_forces_born_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Atom element symbol (e.g. in ATOM   1 NA DYNAMIC CHARGE     0.986361)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_born_atom_element'))

    x_crystal_forces_born_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label number (e.g. in ATOM   1 NA DYNAMIC CHARGE     0.986361)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_born_atom_label'))

    x_crystal_forces_born_atom_tensor = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        ATOMIC BORN CHARGE TENSOR
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_born_atom_tensor'))


class x_crystal_section_forces_matrix_atom_gen(MSection):
    '''
    Atom in force matrix: directions that are GENERATED FROM A PREVIOUS LINE
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_forces_matrix_atom_gen'))

    x_crystal_forces_matrix_atom_gen_dir = Quantity(
        type=str,
        shape=[],
        description='''
        Direction in atom list of forces section (e.g. in ATOM      MAX ABS(DGRAD)
        TOTAL ENERGY (AU)  N.CYC      DE       SYM. 2 CL DY                   GENERATED
        FROM A PREVIOUS LINE)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_gen_dir'))

    x_crystal_forces_matrix_atom_gen_element = Quantity(
        type=str,
        shape=[],
        description='''
        Element symbol in atom list of forces section (e.g. in ATOM      MAX ABS(DGRAD)
        TOTAL ENERGY (AU)  N.CYC      DE       SYM. 2 CL DY                   GENERATED
        FROM A PREVIOUS LINE)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_gen_element'))

    x_crystal_forces_matrix_atom_gen_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label in atom list of forces section (e.g. in ATOM      MAX ABS(DGRAD)
        TOTAL ENERGY (AU)  N.CYC      DE       SYM. 2 CL DY                   GENERATED
        FROM A PREVIOUS LINE)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_gen_label'))


class x_crystal_section_forces_matrix_atom(MSection):
    '''
    Atom in force matrix
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_forces_matrix_atom'))

    x_crystal_forces_matrix_atom_cycles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of cycles (N.CYC) in atom list of forces section (e.g. in ATOM      MAX
        ABS(DGRAD)       TOTAL ENERGY (AU)  N.CYC      DE       SYM. X   9.7672E-05
        -6.214953997616E+02     4     2.8014E-07     8)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_cycles'))

    x_crystal_forces_matrix_atom_de = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        delta energy (DE) in atom list of forces section (e.g. in ATOM      MAX ABS(DGRAD)
        TOTAL ENERGY (AU)  N.CYC      DE       SYM. X   9.7672E-05
        -6.214953997616E+02     4     2.8014E-07     8)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_de'))

    x_crystal_forces_matrix_atom_dir = Quantity(
        type=str,
        shape=[],
        description='''
        Direction in atom list of forces section (e.g. in ATOM      MAX ABS(DGRAD)
        TOTAL ENERGY (AU)  N.CYC      DE       SYM. 2 CL DX   9.7672E-05
        -6.214953997616E+02     4     2.8014E-07     8)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_dir'))

    x_crystal_forces_matrix_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Element symbol in atom list of forces section (e.g. in ATOM      MAX ABS(DGRAD)
        TOTAL ENERGY (AU)  N.CYC      DE       SYM. 2 CL DX   9.7672E-05
        -6.214953997616E+02     4     2.8014E-07     8)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_element'))

    x_crystal_forces_matrix_atom_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL ENERGY (AU) in atom list of forces section (e.g. in ATOM      MAX ABS(DGRAD)
        TOTAL ENERGY (AU)  N.CYC      DE       SYM. X   9.7672E-05
        -6.214953997616E+02     4     2.8014E-07     8)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_energy'))

    x_crystal_forces_matrix_atom_grad = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        MAX ABS(DGRAD) in atom list of forces section (e.g. in ATOM      MAX ABS(DGRAD)
        TOTAL ENERGY (AU)  N.CYC      DE       SYM. X   9.7672E-05
        -6.214953997616E+02     4     2.8014E-07     8)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_grad'))

    x_crystal_forces_matrix_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label in atom list of forces section (e.g. in ATOM      MAX ABS(DGRAD)
        TOTAL ENERGY (AU)  N.CYC      DE       SYM. 2 CL DX   9.7672E-05
        -6.214953997616E+02     4     2.8014E-07     8)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_label'))

    x_crystal_forces_matrix_atom_sym = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        number of symmetries (SYM) in atom list of forces section (e.g. in ATOM      MAX
        ABS(DGRAD)       TOTAL ENERGY (AU)  N.CYC      DE       SYM. X   9.7672E-05
        -6.214953997616E+02     4     2.8014E-07     8)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_matrix_atom_sym'))

    x_crystal_section_forces_matrix_atom_gen = SubSection(
        sub_section=SectionProxy('x_crystal_section_forces_matrix_atom_gen'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_forces_matrix_atom_gen'))


class x_crystal_section_forces(MSection):
    '''
    Atomic forces
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_forces'))

    x_crystal_forces_central_point_cycles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ATOM      MAX ABS(DGRAD)       TOTAL ENERGY (AU)  N.CYC      DE       SYM.
        CENTRAL POINT             -6.214954000417E+02    22     0.0000E+00    48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_central_point_cycles'))

    x_crystal_forces_central_point_de = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ATOM      MAX ABS(DGRAD)       TOTAL ENERGY (AU)  N.CYC      DE       SYM.
        CENTRAL POINT             -6.214954000417E+02    22     0.0000E+00    48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_central_point_de'))

    x_crystal_forces_central_point_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Force matrix: central point energy
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_central_point_energy'))

    x_crystal_forces_central_point_sym = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ATOM      MAX ABS(DGRAD)       TOTAL ENERGY (AU)  N.CYC      DE       SYM.
        CENTRAL POINT             -6.214954000417E+02    22     0.0000E+00    48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_central_point_sym'))

    x_crystal_forces_resultant = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Atomic forces: resultant of all
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_resultant'))

    x_crystal_forces_symmetry_allowed_directions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Symmetry allowed directions.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_symmetry_allowed_directions'))

    x_crystal_forces_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_value1'))

    x_crystal_forces_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_value2'))

    x_crystal_forces_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_forces_value3'))

    x_crystal_section_forces_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_forces_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_forces_atom'))

    x_crystal_section_forces_born_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_forces_born_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_forces_born_atom'))

    x_crystal_section_forces_matrix_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_forces_matrix_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_forces_matrix_atom'))

    x_crystal_section_vibrational = SubSection(
        sub_section=SectionProxy('x_crystal_section_vibrational'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_vibrational'))


class x_crystal_section_frequency_atom(MSection):
    '''
    Frequency calculation setup: atom masses.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_frequency_atom'))

    x_crystal_frequency_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Atom label.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_atom_element'))

    x_crystal_frequency_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_atom_label'))

    x_crystal_frequency_atom_mass = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mass in AMU.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_atom_mass'))


class x_crystal_section_frequency_gradients_atom(MSection):
    '''
    Atom listed in the gradients section.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_frequency_gradients_atom'))

    x_crystal_frequency_gradients_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        IRREDUCIBLE ATOM
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_atom_label'))

    x_crystal_frequency_gradients_atom_number_of_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF SYMMETRY OPERATORS THAT DOESN'T MOVE THE IRREDUCIBLE ATOM
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_atom_number_of_symmops'))

    x_crystal_frequency_gradients_atom_order = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAXIMUM ORDER AMONG THE OPERATORS OF THE IRREDUCIBLE ATOM
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_atom_order'))


class x_crystal_section_frequency_gradients_op(MSection):
    '''
    Frequency calculation: scf+gradient calculations required for calculating frequencies:
    a particular gradient.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_frequency_gradients_op'))

    x_crystal_frequency_gradients_op_displacement = Quantity(
        type=str,
        shape=[],
        description='''
        Particular gradient: displacement component
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_op_displacement'))

    x_crystal_frequency_gradients_op_element = Quantity(
        type=str,
        shape=[],
        description='''
        Particular gradient: element symbol
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_op_element'))

    x_crystal_frequency_gradients_op_generated_by_symmop = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        GENERATED FROM LINE ? WITH OP ?
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_op_generated_by_symmop'))

    x_crystal_frequency_gradients_op_generated_from_line = Quantity(
        type=str,
        shape=[],
        description='''
        GENERATED FROM LINE ? WITH OP ?
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_op_generated_from_line'))

    x_crystal_frequency_gradients_op_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Particular gradient: atom label
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_op_label'))

    x_crystal_frequency_gradients_op_num = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Particular gradient: number
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_op_num'))

    x_crystal_frequency_gradients_op_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of symmops
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_op_symmops'))

    x_crystal_frequency_gradients_op_text = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_op_text'))

    x_crystal_frequency_gradients_op_translational_invariance = Quantity(
        type=bool,
        shape=[],
        description='''
        GENERATED BY TRANSLATIONAL INVARIANCE
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_op_translational_invariance'))


class x_crystal_section_frequency_gradients(MSection):
    '''
    Frequency calculation: scf+gradient calculations required for calculating frequencies.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_frequency_gradients'))

    x_crystal_frequency_gradients_dx = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Length (angstrom) of single displacement in gradient calculations.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_dx'))

    x_crystal_frequency_gradients_equilibrium_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of symmops used in equilibrium geometry.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_equilibrium_symmops'))

    x_crystal_frequency_gradients_number_of_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of irreducible atoms.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_number_of_atoms'))

    x_crystal_frequency_gradients_number_of_ops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of scf+gradient calculations needed.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_frequency_gradients_number_of_ops'))

    x_crystal_section_frequency_gradients_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_frequency_gradients_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_frequency_gradients_atom'))

    x_crystal_section_frequency_gradients_op = SubSection(
        sub_section=SectionProxy('x_crystal_section_frequency_gradients_op'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_frequency_gradients_op'))


class x_crystal_section_frequency(MSection):
    '''
    Frequency calculations setup.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_frequency'))

    x_crystal_section_frequency_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_frequency_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_frequency_atom'))

    x_crystal_section_frequency_gradients = SubSection(
        sub_section=SectionProxy('x_crystal_section_frequency_gradients'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_frequency_gradients'))


class x_crystal_section_header(MSection):
    '''
    Contains crystal version information and other information obtained from the first
    asterix header in the Crystal output file.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_header'))

    x_crystal_header_date = Quantity(
        type=str,
        shape=[],
        description='''
        Date of the Crystal version.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_header_date'))

    x_crystal_header_distribution = Quantity(
        type=str,
        shape=[],
        description='''
        Distribution describer.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_header_distribution'))

    x_crystal_header_minor = Quantity(
        type=str,
        shape=[],
        description='''
        Minor version number of Crystal.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_header_minor'))

    x_crystal_header_url = Quantity(
        type=str,
        shape=[],
        description='''
        URL given in the header.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_header_url'))


class x_crystal_section_info_item(MSection):
    '''
    Information line.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_info_item'))

    x_crystal_info_item_key = Quantity(
        type=str,
        shape=[],
        description='''
        Header of unspecified info line.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_item_key'))

    x_crystal_info_item_value = Quantity(
        type=str,
        shape=[],
        description='''
        Contents of unspecified info line.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_item_value'))


class x_crystal_section_info(MSection):
    '''
    Section containing miscellaneous information.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_info'))

    x_crystal_info_convergence_on_deltap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence seettings, on power of 10 (e.g. CONVERGENCE ON DELTAP        10**-16)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_convergence_on_deltap'))

    x_crystal_info_convergence_on_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Convergence seettings, on power of 10 (e.g. CONVERGENCE ON ENERGY        10**-10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_convergence_on_energy'))

    x_crystal_info_coulomb_bipolar_buffer = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        COULOMB BIPOLAR BUFFER SET TO x Mb
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_coulomb_bipolar_buffer'))

    x_crystal_info_eigenvectors_disk_space_ftn = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        DISK SPACE FOR EIGENVECTORS (FTN 10)      351575 REALS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_eigenvectors_disk_space_ftn'))

    x_crystal_info_eigenvectors_disk_space_reals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        DISK SPACE FOR EIGENVECTORS (FTN 10)      351575 REALS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_eigenvectors_disk_space_reals'))

    x_crystal_info_exchange_bipolar_buffer = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE BIPOLAR BUFFER SET TO x Mb
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_exchange_bipolar_buffer'))

    x_crystal_info_fock_ks_matrix_mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FOCK/KS MATRIX MIXING SET TO x %
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_fock_ks_matrix_mixing'))

    x_crystal_info_input_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT INPUT       TELAPSE        0.01 TCPU        0.01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_input_tcpu'))

    x_crystal_info_input_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT INPUT       TELAPSE        0.01 TCPU        0.01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_input_telapse'))

    x_crystal_info_irr_f = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_irr_f'))

    x_crystal_info_irr_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_irr_p'))

    x_crystal_info_is1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_is1'))

    x_crystal_info_is2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_is2'))

    x_crystal_info_is3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_is3'))

    x_crystal_info_k_points_gilat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF K POINTS(GILAT NET)    145
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_k_points_gilat'))

    x_crystal_info_k_points_ibz = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF K POINTS IN THE IBZ    145
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_k_points_ibz'))

    x_crystal_info_k_pts_monk_net = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_k_pts_monk_net'))

    x_crystal_info_matrix_size_f = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_matrix_size_f'))

    x_crystal_info_matrix_size_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_matrix_size_p'))

    x_crystal_info_max_g_vector_index = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAX G-VECTOR INDEX FOR 1- AND 2-ELECTRON INTEGRALS 247
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_max_g_vector_index'))

    x_crystal_info_max_scf_cycles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAX NUMBER OF SCF CYCLES
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_max_scf_cycles'))

    x_crystal_info_number_of_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF ATOMS PER CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_atoms'))

    x_crystal_info_number_of_core_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CORE ELECTRONS PER CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_core_electrons'))

    x_crystal_info_number_of_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF ELECTRONS PER CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_electrons'))

    x_crystal_info_number_of_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF AO (Atomic orbitals)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_orbitals'))

    x_crystal_info_number_of_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF SHELLS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_shells'))

    x_crystal_info_number_of_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF SYMMETRY OPERATORS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_number_of_symmops'))

    x_crystal_info_pole_order = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        POLE ORDER IN MONO ZONE
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_pole_order'))

    x_crystal_info_shrink_gilat = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        SHRINKING FACTOR(GILAT NET)   16
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink_gilat'))

    x_crystal_info_shrink_value1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink_value1'))

    x_crystal_info_shrink_value2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink_value2'))

    x_crystal_info_shrink_value3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink_value3'))

    x_crystal_info_shrink = Quantity(
        type=np.dtype(np.int32),
        shape=['n'],
        description='''
        SHRINK. FACT.(MONKH.)   16 16 16
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_shrink'))

    x_crystal_info_symmetry_adaption = Quantity(
        type=bool,
        shape=[],
        description='''
        SYMMETRY ADAPTION OF THE BLOCH FUNCTIONS ENABLED
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_symmetry_adaption'))

    x_crystal_info_symmops_g = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_symmops_g'))

    x_crystal_info_symmops_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48.
        (mentioned after the basis set)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_symmops_k'))

    x_crystal_info_tol_coulomb_overlap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        COULOMB OVERLAP TOL         (T1) 10**   -6. (Tolerance T1, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_coulomb_overlap'))

    x_crystal_info_tol_coulomb_penetration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        COULOMB PENETRATION TOL     (T2) 10**   -6. (Tolerance T2, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_coulomb_penetration'))

    x_crystal_info_tol_exchange_overlap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE OVERLAP TOL        (T3) 10**   -6. (Tolerance T3, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_exchange_overlap'))

    x_crystal_info_tol_pseudo_overlap_f = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE PSEUDO OVP (F(G))  (T4) 10**   -6. (Tolerance T4, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_pseudo_overlap_f'))

    x_crystal_info_tol_pseudo_overlap_p = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXCHANGE PSEUDO OVP (P(G))  (T5) 10**  -12. (Tolerance T5, power of 10)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_tol_pseudo_overlap_p'))

    x_crystal_info_type_of_calculation = Quantity(
        type=str,
        shape=[],
        description='''
        The type of the calculation that was performed.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_type_of_calculation'))

    x_crystal_info_weight_previous = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        WEIGHT OF F(I) IN F(I+1)      30%
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_weight_previous'))

    x_crystal_info_toldee = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOLDEE info
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_info_toldee'))

    x_crystal_section_info_item = SubSection(
        sub_section=SectionProxy('x_crystal_section_info_item'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_info_item'))


class x_crystal_section_input_atom(MSection):
    '''
    Non-equivalent atom.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_input_atom'))

    x_crystal_input_atom_position = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        Atom coordinates.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_atom_position'))

    x_crystal_input_atom_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom proton number.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_atom_z'))


class x_crystal_section_input_basis_shell_primitive(MSection):
    '''
    Atom shell gaussian primitive.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_input_basis_shell_primitive'))

    x_crystal_input_basis_shell_primitive_coefficient_p = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Gaussian primitive: coefficient for p (in sp shell).
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_shell_primitive_coefficient_p'))

    x_crystal_input_basis_shell_primitive_coefficient_s = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Gaussian primitive: coefficient for s (in sp shell).
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_shell_primitive_coefficient_s'))

    x_crystal_input_basis_shell_primitive_coefficient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Gaussian primitive: coefficient.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_shell_primitive_coefficient'))

    x_crystal_input_basis_shell_primitive_exp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Gaussian primitive: exponent.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_shell_primitive_exp'))


class x_crystal_section_input_basis_shell(MSection):
    '''
    Atom shell in basis set.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_input_basis_shell'))

    x_crystal_input_basis_shell_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atom shell total charge.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_shell_charge'))

    x_crystal_input_basis_shell_l = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom shell l-value.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_shell_l'))

    x_crystal_input_basis_shell_number_of_primitives = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom shell number of primitives.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_shell_number_of_primitives'))

    x_crystal_input_basis_shell_scale = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atom shell scale factor.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_shell_scale'))

    x_crystal_input_basis_shell_type = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom shell type.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_shell_type'))

    x_crystal_section_input_basis_shell_primitive = SubSection(
        sub_section=SectionProxy('x_crystal_section_input_basis_shell_primitive'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_input_basis_shell_primitive'))


class x_crystal_section_input_basis(MSection):
    '''
    Basis set for an atom.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_input_basis'))

    x_crystal_input_basis_number_of_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom number of shells.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_number_of_shells'))

    x_crystal_input_basis_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom proton number.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_basis_z'))

    x_crystal_section_input_basis_shell = SubSection(
        sub_section=SectionProxy('x_crystal_section_input_basis_shell'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_input_basis_shell'))


class x_crystal_section_input(MSection):
    '''
    Contains the input data for Crystal.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_input'))

    x_crystal_input_dielectric_tensor = Quantity(
        type=np.dtype(np.float64),
        shape=[3, 3],
        description='''
        Freqcalc dielectric tensor.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_dielectric_tensor'))

    x_crystal_input_geometry = Quantity(
        type=str,
        shape=[],
        description='''
        Geometry key: CRYSTAL / SLAB / POLYMER / HELIX / MOLECULE / EXTERNAL / DLVINPUT.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_geometry'))

    x_crystal_input_ifhr = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Lattice parameters given in: 0: hexagonal, 1:rhombohedral.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_ifhr'))

    x_crystal_input_iflag = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Spacegroup input format: 0:sequential number, 1:Hermann-Manguin.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_iflag'))

    x_crystal_input_ifso = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Setting of origin: 0: spacegroup, 1: standard, 2: specified in input.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_ifso'))

    x_crystal_input_intens = Quantity(
        type=bool,
        shape=[],
        description='''
        Freqcalc intens.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_intens'))

    x_crystal_input_keyword = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage for parsing a keyword.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_keyword'))

    x_crystal_input_lattice_parameters = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Lattice parameters.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_lattice_parameters'))

    x_crystal_input_number_of_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of non-equivalent atoms.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_number_of_atoms'))

    x_crystal_input_pointgroup = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Point group for molecules.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_pointgroup'))

    x_crystal_input_ppan = Quantity(
        type=bool,
        shape=[],
        description='''
        Flag for Mulliken population analysis.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_ppan'))

    x_crystal_input_rodgroup = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Rod group for polymers.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_rodgroup'))

    x_crystal_input_shift_of_origin = Quantity(
        type=np.dtype(np.float64),
        shape=[3],
        description='''
        A non-standard shift of origin in fractional coordinates.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_shift_of_origin'))

    x_crystal_input_shrink = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        Shrink factors.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_shrink'))

    x_crystal_input_slabgroup = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Slab group for slabs.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_slabgroup'))

    x_crystal_input_spacegroup_hm = Quantity(
        type=str,
        shape=[],
        description='''
        Spacegroup given in Hermann-Manguin notation.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_spacegroup_hm'))

    x_crystal_input_spacegroup = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Spacegroup for crystals.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_spacegroup'))

    x_crystal_input_title = Quantity(
        type=str,
        shape=[],
        description='''
        Input file title.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_title'))

    x_crystal_input_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for parsing a line of numbers.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_value1'))

    x_crystal_input_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for parsing a line of numbers.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_value2'))

    x_crystal_input_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for parsing a line of numbers.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_value3'))

    x_crystal_input_value4 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for parsing a line of numbers.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_value4'))

    x_crystal_input_value5 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage for parsing a line of numbers.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_value5'))

    x_crystal_input_system_type = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal system type name.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_system_type'))

    x_crystal_input_calculation_type = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal calculation type name.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_calculation_type'))

    x_crystal_input_toldee = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Input TOLDEE
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_toldee'))

    x_crystal_section_input_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_input_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_input_atom'))

    x_crystal_section_input_basis = SubSection(
        sub_section=SectionProxy('x_crystal_section_input_basis'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_input_basis'))

    x_crystal_section_input_dft = SubSection(
        sub_section=SectionProxy('x_crystal_section_input_dft'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_input_dft'))


class x_crystal_section_input_dft(MSection):
    '''
    DFT input.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_input_dft'))

    x_crystal_input_dft_xc_shortcut = Quantity(
        type=str,
        shape=[],
        description='''
        DFT exchange-correlation functional shortcut name
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_dft_xc_shortcut'))

    x_crystal_input_dft_exchange = Quantity(
        type=str,
        shape=[],
        description='''
        DFT exchange functional name
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_dft_exchange'))

    x_crystal_input_dft_correlation = Quantity(
        type=str,
        shape=[],
        description='''
        DFT correlation functional name
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_input_dft_correlation'))


class x_crystal_section_irlo_modes_atom_mode(MSection):
    '''
    Mode
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irlo_modes_atom_mode'))

    x_crystal_irlo_modes_atom_mode_frequencies = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Frequencies
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_atom_mode_frequencies'))

    x_crystal_irlo_modes_atom_mode_tensor = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        Mode tensor
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_atom_mode_tensor'))


class x_crystal_section_irlo_modes_atom(MSection):
    '''
    Atom
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irlo_modes_atom'))

    x_crystal_irlo_modes_atom_axislabels = Quantity(
        type=str,
        shape=[],
        description='''
        Labels used for Cartesian axes.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_atom_axislabels'))

    x_crystal_irlo_modes_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Atom element symbol
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_atom_element'))

    x_crystal_irlo_modes_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_atom_label'))

    x_crystal_section_irlo_modes_atom_mode = SubSection(
        sub_section=SectionProxy('x_crystal_section_irlo_modes_atom_mode'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irlo_modes_atom_mode'))


class x_crystal_section_irlo_modes(MSection):
    '''
    LO MODES FOR IRREP Fu
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irlo_modes'))

    x_crystal_irlo_modes_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_value1'))

    x_crystal_irlo_modes_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_value2'))

    x_crystal_irlo_modes_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_value3'))

    x_crystal_irlo_modes_value4 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_value4'))

    x_crystal_irlo_modes_value5 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_value5'))

    x_crystal_irlo_modes_value6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_modes_value6'))

    x_crystal_section_irlo_modes_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_irlo_modes_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irlo_modes_atom'))


class x_crystal_section_irlo_mode(MSection):
    '''
    MODES         EIGV          FREQUENCIES    IRREP IR INTENS       SHIFTS
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irlo_mode'))

    x_crystal_irlo_mode_eigv = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EIGENVALUES (EIGV)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_mode_eigv'))

    x_crystal_irlo_mode_frequency_cmp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FREQUENCIES (CM**-1)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_mode_frequency_cmp'))

    x_crystal_irlo_mode_frequency_thz = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FREQUENCIES (THZ)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_mode_frequency_thz'))

    x_crystal_irlo_mode_intens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        IR INTENS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_mode_intens'))

    x_crystal_irlo_mode_irrep = Quantity(
        type=str,
        shape=[],
        description='''
        IRREP
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_mode_irrep'))

    x_crystal_irlo_mode_max = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MODES
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_mode_max'))

    x_crystal_irlo_mode_min = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MODES
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_mode_min'))

    x_crystal_irlo_mode_shift_cmp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        SHIFTS (CM**-1)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_mode_shift_cmp'))

    x_crystal_irlo_mode_shift_thz = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        SHIFTS (THZ)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_mode_shift_thz'))


class x_crystal_section_irlo_overlap(MSection):
    '''
    OVERLAP BETWEEN THE EIGENVECTORS OF LO AND TO MODES.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irlo_overlap'))

    x_crystal_irlo_overlap_to = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        IRREP Fu TO (ENTRIES ARE FRQS IN CM**-1)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_overlap_to'))


class x_crystal_section_irlo(MSection):
    '''
    LONGITUDINAL OPTICAL (LO) PHONON CALCULATION REQUESTED.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irlo'))

    x_crystal_irlo_overlap_lo = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        IRREP Fu LO (ENTRIES ARE FRQS IN CM**-1)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_overlap_lo'))

    x_crystal_irlo_overlap_matrix = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        IRREP Fu OVERLAP matrix
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irlo_overlap_matrix'))

    x_crystal_section_irlo_modes = SubSection(
        sub_section=SectionProxy('x_crystal_section_irlo_modes'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irlo_modes'))

    x_crystal_section_irlo_mode = SubSection(
        sub_section=SectionProxy('x_crystal_section_irlo_mode'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irlo_mode'))

    x_crystal_section_irlo_overlap = SubSection(
        sub_section=SectionProxy('x_crystal_section_irlo_overlap'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irlo_overlap'))


class x_crystal_section_irto_modes_atom_mode(MSection):
    '''
    Mode
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irto_modes_atom_mode'))

    x_crystal_irto_modes_atom_mode_frequencies = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Frequencies
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_atom_mode_frequencies'))

    x_crystal_irto_modes_atom_mode_tensor = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        Mode tensor
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_atom_mode_tensor'))


class x_crystal_section_irto_modes_atom(MSection):
    '''
    Atom
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irto_modes_atom'))

    x_crystal_irto_modes_atom_axislabels = Quantity(
        type=str,
        shape=[],
        description='''
        Labels used for Cartesian axes.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_atom_axislabels'))

    x_crystal_irto_modes_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Atom element symbol
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_atom_element'))

    x_crystal_irto_modes_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_atom_label'))

    x_crystal_section_irto_modes_atom_mode = SubSection(
        sub_section=SectionProxy('x_crystal_section_irto_modes_atom_mode'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irto_modes_atom_mode'))


class x_crystal_section_irto_modes(MSection):
    '''
    NORMAL MODES NORMALIZED TO CLASSICAL AMPLITUDES.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irto_modes'))

    x_crystal_irto_modes_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_value1'))

    x_crystal_irto_modes_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_value2'))

    x_crystal_irto_modes_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_value3'))

    x_crystal_irto_modes_value4 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_value4'))

    x_crystal_irto_modes_value5 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_value5'))

    x_crystal_irto_modes_value6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_modes_value6'))

    x_crystal_section_irto_modes_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_irto_modes_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irto_modes_atom'))


class x_crystal_section_irto_mode(MSection):
    '''
    MODES         EIGV          FREQUENCIES     IRREP  IR   INTENS    RAMAN
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irto_mode'))

    x_crystal_irto_mode_eigv = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Transverse optical mode eigv value (e.g. in 1-   3    0.0000E+00      0.0000
        0.0000  (Fu )   A (     0.00)   I)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_mode_eigv'))

    x_crystal_irto_mode_frequency_cmp = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Transverse optical mode frequency CM**-1 (e.g. in 1-   3    0.0000E+00      0.0000
        0.0000  (Fu )   A (     0.00)   I)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_mode_frequency_cmp'))

    x_crystal_irto_mode_frequency_thz = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Transverse optical mode frequency THZ (e.g. in 1-   3    0.0000E+00      0.0000
        0.0000  (Fu )   A (     0.00)   I)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_mode_frequency_thz'))

    x_crystal_irto_mode_intens = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Transverse optical mode INTENSity KM/MOL (e.g. in 1-   3    0.0000E+00      0.0000
        0.0000  (Fu )   A (     0.00)   I)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_mode_intens'))

    x_crystal_irto_mode_irrep = Quantity(
        type=str,
        shape=[],
        description='''
        Transverse optical mode IRREP tag (e.g. in 1-   3    0.0000E+00      0.0000
        0.0000  (Fu )   A (     0.00)   I)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_mode_irrep'))

    x_crystal_irto_mode_ir = Quantity(
        type=str,
        shape=[],
        description='''
        Transverse optical mode IR tag (e.g. in 1-   3    0.0000E+00      0.0000    0.0000
        (Fu )   A (     0.00)   I)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_mode_ir'))

    x_crystal_irto_mode_max = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Transverse optical mode number, max (e.g. in 1-   3    0.0000E+00      0.0000
        0.0000  (Fu )   A (     0.00)   I)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_mode_max'))

    x_crystal_irto_mode_min = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Transverse optical mode number, min (e.g. in 1-   3    0.0000E+00      0.0000
        0.0000  (Fu )   A (     0.00)   I)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_mode_min'))

    x_crystal_irto_mode_raman = Quantity(
        type=str,
        shape=[],
        description='''
        Transverse optical mode RAMAN tag (e.g. in 1-   3    0.0000E+00      0.0000
        0.0000  (Fu )   A (     0.00)   I)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_mode_raman'))


class x_crystal_section_irto(MSection):
    '''
    EIGENVALUES (EIGV) OF THE MASS WEIGHTED HESSIAN MATRIX AND HARMONIC TRANSVERSE OPTICAL
    (TO) FREQUENCIES.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_irto'))

    x_crystal_irto_conversion_hartree = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CONVERSION FACTORS FOR FREQUENCIES: 1 CM**(-1) = ? HARTREE
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_conversion_hartree'))

    x_crystal_irto_conversion_thz = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CONVERSION FACTORS FOR FREQUENCIES: 1 THZ = ? CM**(-1)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_irto_conversion_thz'))

    x_crystal_section_irto_modes = SubSection(
        sub_section=SectionProxy('x_crystal_section_irto_modes'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irto_modes'))

    x_crystal_section_irto_mode = SubSection(
        sub_section=SectionProxy('x_crystal_section_irto_mode'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irto_mode'))


class x_crystal_section_kpoints(MSection):
    '''
    K points
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_kpoints'))

    x_crystal_kpoints_is_units = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        K points units (as in e.g. *** K POINTS COORDINATES (OBLIQUE COORDINATES IN UNITS
        OF IS = 16))
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_kpoints_is_units'))

    x_crystal_section_kpoint = SubSection(
        sub_section=SectionProxy('x_crystal_section_kpoint'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_kpoint'))


class x_crystal_section_kpoint(MSection):
    '''
    K point (as in e.g. *** K POINTS COORDINATES (OBLIQUE COORDINATES IN UNITS OF IS =
    16))
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_kpoint'))

    x_crystal_kpoint_coordinates = Quantity(
        type=np.dtype(np.int32),
        shape=['n'],
        description='''
        K point integer coordinates. (as in 21-C( 12  1  0))
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_kpoint_coordinates'))

    x_crystal_kpoint_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        K point number (as in 21-C( 12  1  0))
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_kpoint_number'))

    x_crystal_kpoint_symbol = Quantity(
        type=str,
        shape=[],
        description='''
        K point symbol (as in 21-C( 12  1  0))
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_kpoint_symbol'))


class x_crystal_section_lattice(MSection):
    '''
    Vectors of the real and reciprical lattice.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_lattice'))

    x_crystal_lattice_real = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        Real space primary lattice vectors.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_lattice_real'))

    x_crystal_lattice_reciprocal = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        Reciprocal lattice vectors.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_lattice_reciprocal'))


class x_crystal_section_neighbors_atom_distance_neighbor(MSection):
    '''
    Particular neighbor at a given distance.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_neighbors_atom_distance_neighbor'))

    x_crystal_neighbors_atom_distance_neighbor_cell = Quantity(
        type=np.dtype(np.int32),
        shape=['n'],
        description='''
        Neighbor atom cell.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_neighbors_atom_distance_neighbor_cell'))

    x_crystal_neighbors_atom_distance_neighbor_element = Quantity(
        type=str,
        shape=[],
        description='''
        Neighbor atom element.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_neighbors_atom_distance_neighbor_element'))

    x_crystal_neighbors_atom_distance_neighbor_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Neighbor atom label.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_neighbors_atom_distance_neighbor_label'))


class x_crystal_section_neighbors_atom_distance(MSection):
    '''
    Nearest neighbors at a given distance.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_neighbors_atom_distance'))

    x_crystal_neighbors_atom_distance_ang = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Distance in angstroms.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_neighbors_atom_distance_ang'))

    x_crystal_neighbors_atom_distance_au = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Distance in atomic units.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_neighbors_atom_distance_au'))

    x_crystal_neighbors_atom_distance_number_of_neighbors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of neighbors at at given distance
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_neighbors_atom_distance_number_of_neighbors'))

    x_crystal_section_neighbors_atom_distance_neighbor = SubSection(
        sub_section=SectionProxy('x_crystal_section_neighbors_atom_distance_neighbor'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_neighbors_atom_distance_neighbor'))


class x_crystal_section_neighbors_atom(MSection):
    '''
    Nearest neighbors of a particular (equivalent) atom
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_neighbors_atom'))

    x_crystal_neighbors_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Atom element
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_neighbors_atom_element'))

    x_crystal_neighbors_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_neighbors_atom_label'))

    x_crystal_section_neighbors_atom_distance = SubSection(
        sub_section=SectionProxy('x_crystal_section_neighbors_atom_distance'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_neighbors_atom_distance'))


class x_crystal_section_neighbors(MSection):
    '''
    Nearest neighbors.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_neighbors'))

    x_crystal_section_neighbors_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_neighbors_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_neighbors_atom'))


class x_crystal_section_prim_atom(MSection):
    '''
    Atom mentioned in asymmetric unit listings.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_prim_atom'))

    x_crystal_prim_atom_coordinates = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Atom coordinates.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_prim_atom_coordinates'))

    x_crystal_prim_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Atom mentioned in asymmetric unit listing.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_prim_atom_element'))

    x_crystal_prim_atom_in_asymmetric = Quantity(
        type=bool,
        shape=[],
        description='''
        Atom belongs to the asymmetric unit.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_prim_atom_in_asymmetric'))

    x_crystal_prim_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom mentioned in asymmetric unit listing.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_prim_atom_label'))

    x_crystal_prim_atom_tag = Quantity(
        type=str,
        shape=[],
        description='''
        Atom mentioned in asymmetric unit listing.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_prim_atom_tag'))

    x_crystal_prim_atom_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atom mentioned in asymmetric unit listing: temporary value
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_prim_atom_value1'))

    x_crystal_prim_atom_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atom mentioned in asymmetric unit listing: temporary value
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_prim_atom_value2'))

    x_crystal_prim_atom_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Atom mentioned in asymmetric unit listing: temporary value
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_prim_atom_value3'))

    x_crystal_prim_atom_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom mentioned in asymmetric unit listing.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_prim_atom_z'))


class x_crystal_section_primitive_cell_atom(MSection):
    '''
    Atom information.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_primitive_cell_atom'))

    x_crystal_primitive_cell_atom_coordinates = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Atom coordinates.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_atom_coordinates'))

    x_crystal_primitive_cell_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        Element symbol.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_atom_element'))

    x_crystal_primitive_cell_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom label
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_atom_label'))

    x_crystal_primitive_cell_atom_number_of_equivalents = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of equivalent atoms.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_atom_number_of_equivalents'))

    x_crystal_primitive_cell_atom_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atom number
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_atom_number'))

    x_crystal_primitive_cell_atom_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_atom_value1'))

    x_crystal_primitive_cell_atom_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_atom_value2'))

    x_crystal_primitive_cell_atom_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_atom_value3'))

    x_crystal_primitive_cell_atom_z = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Proton number.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_atom_z'))


class x_crystal_section_primitive_cell(MSection):
    '''
    Section for primitive cell parameters
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_primitive_cell'))

    x_crystal_primitive_cell_angles = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Angles between primitive lattice vectors.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_angles'))

    x_crystal_primitive_cell_lengths = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Lengths of primitive lattice vectors.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_lengths'))

    x_crystal_primitive_cell_units_atom = Quantity(
        type=str,
        shape=[],
        description='''
        Units used for atom coordinates.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_units_atom'))

    x_crystal_primitive_cell_units = Quantity(
        type=str,
        shape=[],
        description='''
        Units used for length and angle.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_units'))

    x_crystal_primitive_cell_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_value1'))

    x_crystal_primitive_cell_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_value2'))

    x_crystal_primitive_cell_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_value3'))

    x_crystal_primitive_cell_value4 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_value4'))

    x_crystal_primitive_cell_value5 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_value5'))

    x_crystal_primitive_cell_value6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_value6'))

    x_crystal_primitive_cell_value7 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_value7'))

    x_crystal_primitive_cell_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Primitive cell volume.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_primitive_cell_volume'))

    x_crystal_section_primitive_cell_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_primitive_cell_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_primitive_cell_atom'))


class x_crystal_section_prim(MSection):
    '''
    Atoms mentioned in asymmetric unit listings.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_prim'))

    x_crystal_section_prim_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_prim_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_prim_atom'))


class x_crystal_section_process(MSection):
    '''
    Stores operating system related information related to the Crystal process.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_process'))

    x_crystal_process_datetime = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary type for storing date and time, in locale-dependent format.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_datetime'))

    x_crystal_process_exe = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal executable file name.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_exe'))

    x_crystal_process_hn = Quantity(
        type=str,
        shape=[],
        description='''
        Hostname where Crystal was run
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_hn'))

    x_crystal_process_input = Quantity(
        type=str,
        shape=[],
        description='''
        Input file name.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_input'))

    x_crystal_process_os = Quantity(
        type=str,
        shape=[],
        description='''
        String describing the operating system where Crystal was run.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_os'))

    x_crystal_process_output = Quantity(
        type=str,
        shape=[],
        description='''
        Output file name.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_output'))

    x_crystal_process_tmpdir = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary directory.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_tmpdir'))

    x_crystal_process_user = Quantity(
        type=str,
        shape=[],
        description='''
        Username: who ran Crystal.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_process_user'))


class x_crystal_section_properties_atom(MSection):
    '''
    ATOM N.AT.  SHELL    X(A)      Y(A)      Z(A)      EXAD       N.ELECT.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_properties_atom'))

    x_crystal_properties_atom_coordinates = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        X(A)      Y(A)      Z(A)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_coordinates'))

    x_crystal_properties_atom_element = Quantity(
        type=str,
        shape=[],
        description='''
        AT.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_element'))

    x_crystal_properties_atom_exad = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EXAD
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_exad'))

    x_crystal_properties_atom_label = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ATOM
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_label'))

    x_crystal_properties_atom_number_of_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        N.ELECT.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_number_of_electrons'))

    x_crystal_properties_atom_shell = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        SHELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_shell'))

    x_crystal_properties_atom_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_value1'))

    x_crystal_properties_atom_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_value2'))

    x_crystal_properties_atom_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_value3'))

    x_crystal_properties_atom_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        N.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_atom_z'))


class x_crystal_section_properties_lattice(MSection):
    '''
    Section containing lattice parameters used by Properties program.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_properties_lattice'))

    x_crystal_properties_lattice_angles = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Angles between primitive lattice vectors in degrees (e.g. LATTICE PARAMETERS
        (ANGSTROM AND DEGREES) - PRIMITIVE CELL. A          B          C         ALPHA
        BETA     GAMMA        VOLUME. 3.98822    3.98822    3.98822     60.0000   60.0000
        60.0000      44.85631)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_angles'))

    x_crystal_properties_lattice_lengths = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        Lengths of primitive lattice vectors in angstroms (e.g. LATTICE PARAMETERS
        (ANGSTROM AND DEGREES) - PRIMITIVE CELL. A          B          C         ALPHA
        BETA     GAMMA        VOLUME. 3.98822    3.98822    3.98822     60.0000   60.0000
        60.0000      44.85631)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_lengths'))

    x_crystal_properties_lattice_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_value1'))

    x_crystal_properties_lattice_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_value2'))

    x_crystal_properties_lattice_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_value3'))

    x_crystal_properties_lattice_value4 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_value4'))

    x_crystal_properties_lattice_value5 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_value5'))

    x_crystal_properties_lattice_value6 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_value6'))

    x_crystal_properties_lattice_value7 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_value7'))

    x_crystal_properties_lattice_vectors = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        DIRECT LATTICE VECTOR COMPONENTS (ANGSTROM)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_vectors'))

    x_crystal_properties_lattice_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Primitive cell volume in cubic angstroms. (e.g. LATTICE PARAMETERS  (ANGSTROM AND
        DEGREES) - PRIMITIVE CELL. A          B          C         ALPHA      BETA
        GAMMA        VOLUME. 3.98822    3.98822    3.98822     60.0000   60.0000   60.0000
        44.85631)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_lattice_volume'))


class x_crystal_section_properties_warning(MSection):
    '''
    WARNING **** F90MAIN3 **** BF SYMMETRY ADAPTED-INFO MODIFIED BY BAND-CALL NEWK
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_properties_warning'))

    x_crystal_properties_warning_key = Quantity(
        type=str,
        shape=[],
        description='''
        WARNING **** F90MAIN3 **** BF SYMMETRY ADAPTED-INFO MODIFIED BY BAND-CALL NEWK
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_warning_key'))

    x_crystal_properties_warning_text = Quantity(
        type=str,
        shape=[],
        description='''
        WARNING **** F90MAIN3 **** BF SYMMETRY ADAPTED-INFO MODIFIED BY BAND-CALL NEWK
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_warning_text'))


class x_crystal_section_properties(MSection):
    '''
    program called properties, output file begins.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_properties'))

    x_crystal_properties_cappa_is1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_cappa_is1'))

    x_crystal_properties_cappa_is2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_cappa_is2'))

    x_crystal_properties_cappa_is3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_cappa_is3'))

    x_crystal_properties_cell_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CELL VOLUME (A.U.)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_cell_volume'))

    x_crystal_properties_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CONVERGENCE ON ENER
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_convergence'))

    x_crystal_properties_dek = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        DE(K)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_dek'))

    x_crystal_properties_energy_level_shifting = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENERGY LEVEL SHIFTING
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_energy_level_shifting'))

    x_crystal_properties_fermi_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        FERMI ENERGY
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_fermi_energy'))

    x_crystal_properties_gcalco_max_indices = Quantity(
        type=np.dtype(np.int32),
        shape=['n'],
        description='''
        GCALCO - MAX INDICES DIRECT LATTICE VECTOR
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_gcalco_max_indices'))

    x_crystal_properties_input_file = Quantity(
        type=str,
        shape=[],
        description='''
        properties input file
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_input_file'))

    x_crystal_properties_integer1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_integer1'))

    x_crystal_properties_integer2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_integer2'))

    x_crystal_properties_integer3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_integer3'))

    x_crystal_properties_irr_f = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_irr_f'))

    x_crystal_properties_irr_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_irr_p'))

    x_crystal_properties_k_pts_monk_net = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_k_pts_monk_net'))

    x_crystal_properties_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        KIN. ENERGY
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_kinetic_energy'))

    x_crystal_properties_matrix_size_f = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_matrix_size_f'))

    x_crystal_properties_matrix_size_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MATRIX SIZE: P(G)   31533, F(G)    5204, P(G) IRR    1802, F(G) IRR     964
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_matrix_size_p'))

    x_crystal_properties_max_gvector_index = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MAX G-VECTOR INDEX FOR 1- AND 2-ELECTRON INTEGRALS 247
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_max_gvector_index'))

    x_crystal_properties_number_of_atoms = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Info section related to program Properties, N. OF ATOMS PER CELL.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_number_of_atoms'))

    x_crystal_properties_number_of_core_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Info section related to program Properties, CORE ELECTRONS PER CELL.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_number_of_core_electrons'))

    x_crystal_properties_number_of_electrons = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Info section related to program Properties, N. OF ELECTRONS PER CELL.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_number_of_electrons'))

    x_crystal_properties_number_of_k_points_ibz = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF K POINTS IN THE IBZ
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_number_of_k_points_ibz'))

    x_crystal_properties_number_of_orbitals = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Info section related to program Properties, NUMBER OF AO.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_number_of_orbitals'))

    x_crystal_properties_number_of_scf_cycles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        N. OF SCF CYCLES
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_number_of_scf_cycles'))

    x_crystal_properties_number_of_shells = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Info section related to program Properties, NUMBER OF SHELLS.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_number_of_shells'))

    x_crystal_properties_number_of_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Info section related to program Properties, N. OF SYMMETRY OPERATORS.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_number_of_symmops'))

    x_crystal_properties_number_of_vectors = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NO.OF VECTORS CREATED 6999 STARS  105 RMAX    79.76041 BOHR
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_number_of_vectors'))

    x_crystal_properties_pole_order = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Info section related to program Properties, POLE ORDER IN MONO ZONE
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_pole_order'))

    x_crystal_properties_rmax_bohr = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        NO.OF VECTORS CREATED 6999 STARS  105 RMAX    79.76041 BOHR
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_rmax_bohr'))

    x_crystal_properties_shrink_gilat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        SHRINKING FACTOR(GILAT NET)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_shrink_gilat'))

    x_crystal_properties_shrink_monkh = Quantity(
        type=np.dtype(np.int32),
        shape=['n'],
        description='''
        SHRINK. FACT.(MONKH.)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_shrink_monkh'))

    x_crystal_properties_stars = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NO.OF VECTORS CREATED 6999 STARS  105 RMAX    79.76041 BOHR
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_stars'))

    x_crystal_properties_start_date = Quantity(
        type=str,
        shape=[],
        description='''
        Start date of program Properties (Properties performs e.g. band structure
        analysis) EEEEEEEEEE STARTING  DATE 26 05 2016 TIME 13:13:06.5.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_start_date'))

    x_crystal_properties_start_time = Quantity(
        type=str,
        shape=[],
        description='''
        Start time of program Properties (Properties performs e.g. band structure
        analysis). EEEEEEEEEE STARTING  DATE 26 05 2016 TIME 13:13:06.5
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_start_time'))

    x_crystal_properties_symmops_g = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_symmops_g'))

    x_crystal_properties_symmops_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        CAPPA:IS1 16;IS2 16;IS3 16; K PTS MONK NET 145; SYMMOPS:K SPACE  48;G SPACE  48
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_symmops_k'))

    x_crystal_properties_title = Quantity(
        type=str,
        shape=[],
        description='''
        Title following Properties starting date and time.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_title'))

    x_crystal_properties_tol_coulomb_overlap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Info section related to program Properties, tolerance T1 as power of 10 (e.g.
        COULOMB OVERLAP TOL          (T1) 10**   -6)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_tol_coulomb_overlap'))

    x_crystal_properties_tol_coulomb_penetration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Info section related to program Properties, tolerance T2 as power in 10 (e.g.
        COULOMB PENETRATION TOL      (T2) 10**   -6)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_tol_coulomb_penetration'))

    x_crystal_properties_tol_exchange_overlap = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Info section related to program Properties, tolerance T3 as power in 10 (e.g.
        EXCHANGE OVERLAP TOL         (T3) 10**   -6)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_tol_exchange_overlap'))

    x_crystal_properties_tol_pseudo_overlap_f = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Info section related to program Properties, tolerance T4 as power in 10 (e.g.
        EXCHANGE PSEUDO OVP (F(G))   (T4) 10**   -6)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_tol_pseudo_overlap_f'))

    x_crystal_properties_tol_pseudo_overlap_p = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Info section related to program Properties, tolerance T5 as power in 10 (e.g.
        EXCHANGE PSEUDO OVP (P(G))   (T5) 10**  -12)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_tol_pseudo_overlap_p'))

    x_crystal_properties_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL ENERGY
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_total_energy'))

    x_crystal_properties_type2 = Quantity(
        type=str,
        shape=[],
        description='''
        Following line, 2nd type of properties calculation (e.g. HARTREE-FOCK
        HAMILTONIAN),
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_type2'))

    x_crystal_properties_type = Quantity(
        type=str,
        shape=[],
        description='''
        Type of properties calculation (e.g. CRYSTAL - PROPERTIES - TYPE OF CALCULATION :
        RESTRICTED CLOSED SHELL)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_type'))

    x_crystal_properties_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_value1'))

    x_crystal_properties_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_value2'))

    x_crystal_properties_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_value3'))

    x_crystal_properties_virial_coefficient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VIR. COEFF.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_virial_coefficient'))

    x_crystal_properties_weight_f = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        WEIGHT OF F(I) IN F(I+1)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_properties_weight_f'))

    x_crystal_section_bands = SubSection(
        sub_section=SectionProxy('x_crystal_section_bands'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_bands'))

    x_crystal_section_properties_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_properties_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_properties_atom'))

    x_crystal_section_properties_lattice = SubSection(
        sub_section=SectionProxy('x_crystal_section_properties_lattice'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_properties_lattice'))

    x_crystal_section_properties_warning = SubSection(
        sub_section=SectionProxy('x_crystal_section_properties_warning'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_properties_warning'))

    x_crystal_section_restart = SubSection(
        sub_section=SectionProxy('x_crystal_section_restart'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_restart'))


class x_crystal_section_restart_band(MSection):
    '''
    BAND     INTEGRATED DOSS PER PROJECTION AND TOTAL. T.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_restart_band'))

    x_crystal_restart_band_doss_per = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        BAND     INTEGRATED DOSS PER PROJECTION AND TOTAL. T.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_band_doss_per'))

    x_crystal_restart_band_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        BAND     INTEGRATED DOSS PER PROJECTION AND TOTAL. T.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_band_number'))


class x_crystal_section_restart_dos_energy(MSection):
    '''
    *** ENERGY      TOTAL DENSITY OF STATES - FULL SCALE =   160.18198 AU
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_restart_dos_energy'))

    x_crystal_restart_dos_energy_dos = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL DENSITY OF STATES - FULL SCALE =   160.18198 AU
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_dos_energy_dos'))

    x_crystal_restart_dos_energy_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENERGY
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_dos_energy_energy'))

    x_crystal_restart_dos_energy_text = Quantity(
        type=str,
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_dos_energy_text'))


class x_crystal_section_restart_dos(MSection):
    '''
    *** ENERGY      TOTAL DENSITY OF STATES - FULL SCALE =   160.18198 AU
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_restart_dos'))

    x_crystal_restart_dos_scale_full = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        *** ENERGY      TOTAL DENSITY OF STATES - FULL SCALE =   160.18198 AU
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_dos_scale_full'))

    x_crystal_restart_dos_scale_t = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        *** INTEGRATED DENSITIES IN THE ENERGY INTERVAL PER PROJECTION AND TOTAL. T.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_dos_scale_t'))

    x_crystal_restart_dos_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT DOSS        TELAPSE        0.35 TCPU        0.35
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_dos_tcpu'))

    x_crystal_restart_dos_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT DOSS        TELAPSE        0.35 TCPU        0.35
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_dos_telapse'))

    x_crystal_section_restart_dos_energy = SubSection(
        sub_section=SectionProxy('x_crystal_section_restart_dos_energy'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_restart_dos_energy'))


class x_crystal_section_restart_kpoints(MSection):
    '''
    *** K POINTS COORDINATES (OBLIQUE COORDINATES IN UNITS OF IS = 12)
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_restart_kpoints'))

    x_crystal_restart_kpoints_is_units = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        *** K POINTS COORDINATES (OBLIQUE COORDINATES IN UNITS OF IS = 12)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_kpoints_is_units'))

    x_crystal_section_restart_kpoint = SubSection(
        sub_section=SectionProxy('x_crystal_section_restart_kpoint'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_restart_kpoint'))


class x_crystal_section_restart_kpoint(MSection):
    '''
    14-C(  7  1  0)
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_restart_kpoint'))

    x_crystal_restart_kpoint_coordinates = Quantity(
        type=np.dtype(np.int32),
        shape=['n'],
        description='''
        14-C(  7  1  0)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_kpoint_coordinates'))

    x_crystal_restart_kpoint_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        14-C(  7  1  0)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_kpoint_number'))

    x_crystal_restart_kpoint_symbol = Quantity(
        type=str,
        shape=[],
        description='''
        14-C(  7  1  0)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_kpoint_symbol'))


class x_crystal_section_restart(MSection):
    '''
    RESTART WITH NEW K POINTS NET
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_restart'))

    x_crystal_restart_bottom_of_virtual_b = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        BOTTOM OF VIRTUAL BANDS - BAND     15; K    1; EIG  1.2859066E-01 AU
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_bottom_of_virtual_b'))

    x_crystal_restart_bottom_of_virtual_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        BOTTOM OF VIRTUAL BANDS - BAND     15; K    1; EIG  1.2859066E-01 AU
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_bottom_of_virtual_energy'))

    x_crystal_restart_bottom_of_virtual_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        BOTTOM OF VIRTUAL BANDS - BAND     15; K    1; EIG  1.2859066E-01 AU
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_bottom_of_virtual_k'))

    x_crystal_restart_density_matrix_cycleplus = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        FERMI ENERGY AND DENSITY MATRIX CALCULATION ON COMPUTED EIGENVECTORS. DENSITY
        MATRIX AT SCF CYCLE ( 22+1)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_density_matrix_cycleplus'))

    x_crystal_restart_density_matrix_cycle = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        FERMI ENERGY AND DENSITY MATRIX CALCULATION ON COMPUTED EIGENVECTORS. DENSITY
        MATRIX AT SCF CYCLE ( 22+1)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_density_matrix_cycle'))

    x_crystal_restart_end_date = Quantity(
        type=str,
        shape=[],
        description='''
        EEEEEEEEEE TERMINATION  DATE 26 05 2016 TIME 13:13:06.9
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_end_date'))

    x_crystal_restart_end_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENDPROP. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT END         TELAPSE        0.35 TCPU
        0.35
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_end_tcpu'))

    x_crystal_restart_end_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ENDPROP. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT END         TELAPSE        0.35 TCPU
        0.35
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_end_telapse'))

    x_crystal_restart_end_time = Quantity(
        type=str,
        shape=[],
        description='''
        EEEEEEEEEE TERMINATION  DATE 26 05 2016 TIME 13:13:06.9
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_end_time'))

    x_crystal_restart_fl_band_max = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        TOTAL AND PROJECTED DENSITY OF STATES - FOURIER LEGENDRE METHOD. FROM BAND   11 TO
        BAND   14 ENERGY RANGE -0.10285E+01 -0.39686E+00
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_fl_band_max'))

    x_crystal_restart_fl_band_min = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        TOTAL AND PROJECTED DENSITY OF STATES - FOURIER LEGENDRE METHOD. FROM BAND   11 TO
        BAND   14 ENERGY RANGE -0.10285E+01 -0.39686E+00
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_fl_band_min'))

    x_crystal_restart_fl_energy_max = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL AND PROJECTED DENSITY OF STATES - FOURIER LEGENDRE METHOD. FROM BAND   11 TO
        BAND   14 ENERGY RANGE -0.10285E+01 -0.39686E+00
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_fl_energy_max'))

    x_crystal_restart_fl_energy_min = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOTAL AND PROJECTED DENSITY OF STATES - FOURIER LEGENDRE METHOD. FROM BAND   11 TO
        BAND   14 ENERGY RANGE -0.10285E+01 -0.39686E+00
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_fl_energy_min'))

    x_crystal_restart_insulating_state = Quantity(
        type=bool,
        shape=[],
        description='''
        INSULATING STATE
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_insulating_state'))

    x_crystal_restart_integer1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_integer1'))

    x_crystal_restart_integer2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_integer2'))

    x_crystal_restart_integer3 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_integer3'))

    x_crystal_restart_number_of_epoints = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF ENERGY POINTS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_number_of_epoints'))

    x_crystal_restart_number_of_kpsn = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF K POINTS OF SECONDARY NET
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_number_of_kpsn'))

    x_crystal_restart_number_of_lpols = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF LEGENDRE POLYNOMIALS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_number_of_lpols'))

    x_crystal_restart_number_of_projections = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF PROJECTIONS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_number_of_projections'))

    x_crystal_restart_number_of_sympws = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        NUMBER OF SYMMETRIZED PWS FOR EXPANSION
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_number_of_sympws'))

    x_crystal_restart_points_gilat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        POINTS(GILAT NET)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_points_gilat'))

    x_crystal_restart_points_ibz = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        POINTS IN THE IBZ
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_points_ibz'))

    x_crystal_restart_shrink_gilat = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        SHRINK FACTOR(GILAT)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_shrink_gilat'))

    x_crystal_restart_shrink_monkh = Quantity(
        type=np.dtype(np.int32),
        shape=['n'],
        description='''
        SHRINK FACTORS(MONK.)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_shrink_monkh'))

    x_crystal_restart_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CORE DENSITY MATRIX CALCULATION. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT NEWK
        TELAPSE        0.34 TCPU        0.34
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_tcpu'))

    x_crystal_restart_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CORE DENSITY MATRIX CALCULATION. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT NEWK
        TELAPSE        0.34 TCPU        0.34
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_telapse'))

    x_crystal_restart_top_of_valence_b = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        TOP OF VALENCE BANDS -    BAND     14; K    1; EIG -3.9685829E-01 AU
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_top_of_valence_b'))

    x_crystal_restart_top_of_valence_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TOP OF VALENCE BANDS -    BAND     14; K    1; EIG -3.9685829E-01 AU
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_top_of_valence_energy'))

    x_crystal_restart_top_of_valence_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        TOP OF VALENCE BANDS -    BAND     14; K    1; EIG -3.9685829E-01 AU
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_restart_top_of_valence_k'))

    x_crystal_section_restart_band = SubSection(
        sub_section=SectionProxy('x_crystal_section_restart_band'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_restart_band'))

    x_crystal_section_restart_dos = SubSection(
        sub_section=SectionProxy('x_crystal_section_restart_dos'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_restart_dos'))

    x_crystal_section_restart_kpoints = SubSection(
        sub_section=SectionProxy('x_crystal_section_restart_kpoints'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_restart_kpoints'))


class x_crystal_section_startinformation(MSection):
    '''
    Contains information about the starting conditions for this run.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_startinformation'))

    x_crystal_run_start_date = Quantity(
        type=str,
        shape=[],
        description='''
        The date when this run was started.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_run_start_date'))

    x_crystal_run_start_time = Quantity(
        type=str,
        shape=[],
        description='''
        The time when this run was started.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_run_start_time'))

    x_crystal_run_title = Quantity(
        type=str,
        shape=[],
        description='''
        Title of the runcry(14) task.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_run_title'))


class x_crystal_section_symmetry(MSection):
    '''
    Symmetry allowed directions.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_symmetry'))

    x_crystal_symmetry_allowed_directions = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Symmetry allowed directions.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_symmetry_allowed_directions'))

    x_crystal_symmetry_intscreen_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        CPU time used for calculating symmetry.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_symmetry_intscreen_tcpu'))

    x_crystal_symmetry_intscreen_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Elapsed time used for calculating symmetry.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_symmetry_intscreen_telapse'))

    x_crystal_symmetry_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Time used for calculating symmetry.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_symmetry_tcpu'))

    x_crystal_symmetry_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Time used for calculating symmetry.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_symmetry_telapse'))


class x_crystal_section_thermodynamic_contrib(MSection):
    '''
    HARMONIC VIBRATIONAL CONTRIBUTIONS TO THERMODYNAMIC FUNCTIONS AT GIVEN TEMPERATURE AND
    PRESSURE. THERMODYNAMIC FUNCTIONS WITH VIBRATIONAL CONTRIBUTIONS.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_thermodynamic_contrib'))

    x_crystal_thermodynamic_contrib_c1_aucell = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ET+PV-TS: AU/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_c1_aucell'))

    x_crystal_thermodynamic_contrib_c1_ev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ET+PV-TS: EV/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_c1_ev'))

    x_crystal_thermodynamic_contrib_c1_kjmol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ET+PV-TS : KJ/MOL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_c1_kjmol'))

    x_crystal_thermodynamic_contrib_c2_aucell = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EL+E0+ET+PV-TS: AU/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_c2_aucell'))

    x_crystal_thermodynamic_contrib_c2_ev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EL+E0+ET+PV-TS: EV/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_c2_ev'))

    x_crystal_thermodynamic_contrib_c2_kjmol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        EL+E0+ET+PV-TS: KJ/MOL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_c2_kjmol'))

    x_crystal_thermodynamic_contrib_e0_aucell = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ZERO-POINT ENERGY: AU/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_e0_aucell'))

    x_crystal_thermodynamic_contrib_e0_ev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ZERO-POINT ENERGY: EV/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_e0_ev'))

    x_crystal_thermodynamic_contrib_e0_kjmol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ZERO-POINT ENERGY: KJ/MOL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_e0_kjmol'))

    x_crystal_thermodynamic_contrib_el_aucell = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ELECTRONIC ENERGY: AU/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_el_aucell'))

    x_crystal_thermodynamic_contrib_el_ev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ELECTRONIC ENERGY: EV/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_el_ev'))

    x_crystal_thermodynamic_contrib_el_kjmol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ELECTRONIC ENERGY: KJ/MOL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_el_kjmol'))

    x_crystal_thermodynamic_contrib_et_aucell = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        THERMAL CONTRIBUTION TO THE VIBRATIONAL ENERGY: AU/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_et_aucell'))

    x_crystal_thermodynamic_contrib_et_ev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        THERMAL CONTRIBUTION TO THE VIBRATIONAL ENERGY: EV/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_et_ev'))

    x_crystal_thermodynamic_contrib_et_kjmol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        THERMAL CONTRIBUTION TO THE VIBRATIONAL ENERGY: KJ/MOL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_et_kjmol'))

    x_crystal_thermodynamic_contrib_pressure = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        AT GIVEN TEMPERATURE AND PRESSURE: (T =  ? K, P =   ? MPA)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_pressure'))

    x_crystal_thermodynamic_contrib_pv_aucell = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        PRESSURE * VOLUME: AU/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_pv_aucell'))

    x_crystal_thermodynamic_contrib_pv_ev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        PRESSURE * VOLUME: EV/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_pv_ev'))

    x_crystal_thermodynamic_contrib_pv_kjmol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        PRESSURE * VOLUME: KJ/MOL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_pv_kjmol'))

    x_crystal_thermodynamic_contrib_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        AT GIVEN TEMPERATURE AND PRESSURE: (T =  ? K, P =   ? MPA)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_temperature'))

    x_crystal_thermodynamic_contrib_ts_aucell = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TEMPERATURE * ENTROPY: AU/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_ts_aucell'))

    x_crystal_thermodynamic_contrib_ts_ev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TEMPERATURE * ENTROPY: EV/CELL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_ts_ev'))

    x_crystal_thermodynamic_contrib_ts_kjmol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        TEMPERATURE * ENTROPY: KJ/MOL
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_contrib_ts_kjmol'))


class x_crystal_section_thermodynamic(MSection):
    '''
    Thermodynamic quantities
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_thermodynamic'))

    x_crystal_thermodynamic_entropy_jmolk = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        OTHER THERMODYNAMIC FUNCTIONS: ENTROPY: J/(MOL*K)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_entropy_jmolk'))

    x_crystal_thermodynamic_entropy_mev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        OTHER THERMODYNAMIC FUNCTIONS: ENTROPY: mEV/(CELL*K)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_entropy_mev'))

    x_crystal_thermodynamic_entropy_mhartree = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        OTHER THERMODYNAMIC FUNCTIONS: ENTROPY: mHARTREE/(CELL*K)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_entropy_mhartree'))

    x_crystal_thermodynamic_heatcapacity_jmolk = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        OTHER THERMODYNAMIC FUNCTIONS: HEAT CAPACITY: J/(MOL*K)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_heatcapacity_jmolk'))

    x_crystal_thermodynamic_heatcapacity_mev = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        OTHER THERMODYNAMIC FUNCTIONS: HEAT CAPACITY: mEV/(CELL*K)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_heatcapacity_mev'))

    x_crystal_thermodynamic_heatcapacity_mhartree = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        OTHER THERMODYNAMIC FUNCTIONS: HEAT CAPACITY: mHARTREE/(CELL*K)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_thermodynamic_heatcapacity_mhartree'))

    x_crystal_section_thermodynamic_contrib = SubSection(
        sub_section=SectionProxy('x_crystal_section_thermodynamic_contrib'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_thermodynamic_contrib'))


class x_crystal_section_vibrational_modes_lo(MSection):
    '''
    VIBRATIONAL TEMPERATURES, LO MODES
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_modes_lo'))

    x_crystal_vibrational_modes_lo_irrep = Quantity(
        type=str,
        shape=[],
        description='''
        IRREP
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_modes_lo_irrep'))

    x_crystal_vibrational_modes_lo_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Mode number
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_modes_lo_number'))

    x_crystal_vibrational_modes_lo_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VIBRATIONAL TEMPERATURES (K)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_modes_lo_temperature'))


class x_crystal_section_vibrational_modes_to(MSection):
    '''
    VIBRATIONAL TEMPERATURES, TO MODES
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_modes_to'))

    x_crystal_vibrational_modes_to_irrep = Quantity(
        type=str,
        shape=[],
        description='''
        Mode number
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_modes_to_irrep'))

    x_crystal_vibrational_modes_to_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Mode number
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_modes_to_number'))

    x_crystal_vibrational_modes_to_temperature = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        VIBRATIONAL TEMPERATURES (K)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_modes_to_temperature'))


class x_crystal_section_vibrational_modes(MSection):
    '''
    VIBRATIONAL TEMPERATURES (K) [MODE NUMBER;IRREP]
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_modes'))

    x_crystal_section_vibrational_modes_lo = SubSection(
        sub_section=SectionProxy('x_crystal_section_vibrational_modes_lo'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_modes_lo'))

    x_crystal_section_vibrational_modes_to = SubSection(
        sub_section=SectionProxy('x_crystal_section_vibrational_modes_to'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_modes_to'))


class x_crystal_section_vibrational_mode(MSection):
    '''
    BORN CHARGE VECTOR IN THE BASIS OF NORMAL MODES
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_mode'))

    x_crystal_vibrational_mode_born_charge_vector = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        BORN CHARGE VECTOR IN THE BASIS OF NORMAL MODES (UNITS OF e*M_E**(-1/2) ).
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_mode_born_charge_vector'))

    x_crystal_vibrational_mode_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        BORN CHARGE VECTOR IN THE BASIS OF NORMAL MODES (UNITS OF e*M_E**(-1/2) ).
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_mode_number'))

    x_crystal_vibrational_mode_tensor = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        CARTESIAN AXES SYSTEM
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_mode_tensor'))

    x_crystal_vibrational_mode_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_mode_value1'))

    x_crystal_vibrational_mode_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_mode_value2'))

    x_crystal_vibrational_mode_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_mode_value3'))


class x_crystal_section_vibrational_multip(MSection):
    '''
    IRREP/CLA MULTIP Fu for GROUP OPERATORS
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_multip'))

    x_crystal_vibrational_multip_fu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Fu
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_multip_fu'))

    x_crystal_vibrational_multip_irrep_cla = Quantity(
        type=str,
        shape=[],
        description='''
        IRREP/CLA
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_multip_irrep_cla'))

    x_crystal_vibrational_multip_multip = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        MULTIP
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_multip_multip'))


class x_crystal_section_vibrational_symmetry(MSection):
    '''
    SYMMETRY ADAPTION OF VIBRATIONAL MODES: K-LITTLE GROUP: CLASS TABLE, CHARACTER TABLE.
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_symmetry'))

    x_crystal_vibrational_symmetry_class = Quantity(
        type=str,
        shape=[],
        description='''
        CLASS
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_symmetry_class'))

    x_crystal_vibrational_symmetry_group_operators = Quantity(
        type=np.dtype(np.int32),
        shape=['n'],
        description='''
        GROUP OPERATORS (SEE SYMMOPS KEYWORD)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_symmetry_group_operators'))

    x_crystal_vibrational_symmetry_text = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_symmetry_text'))


class x_crystal_section_vibrational(MSection):
    '''
    SYMMETRY ADAPTION OF VIBRATIONAL MODES
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_vibrational'))

    x_crystal_vibrational_dielectric_tensor_contrib = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        SUM TENSOR OF THE VIBRATIONAL CONTRIBUTIONS TO THE STATIC DIELECTRIC TENSOR
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_dielectric_tensor_contrib'))

    x_crystal_vibrational_dielectric_tensor_hf = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        HIGH FREQUENCY DIELECTRIC TENSOR (FROM INPUT)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_dielectric_tensor_hf'))

    x_crystal_vibrational_dielectric_tensor_static = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        STATIC DIELECTRIC TENSOR
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_dielectric_tensor_static'))

    x_crystal_vibrational_fu = Quantity(
        type=np.dtype(np.int32),
        shape=[2],
        description='''
        Fu vector
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_fu'))

    x_crystal_vibrational_integer1 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_integer1'))

    x_crystal_vibrational_integer2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_integer2'))

    x_crystal_vibrational_minus = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_minus'))

    x_crystal_vibrational_optical_longitudal_mode_direction = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        SYMMETRY ADAPTED DIRECTIONS FOR LONGITUDINAL OPTICAL MODES
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_optical_longitudal_mode_direction'))

    x_crystal_vibrational_text1 = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_text1'))

    x_crystal_vibrational_text2 = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_text2'))

    x_crystal_vibrational_text3 = Quantity(
        type=str,
        shape=[],
        description='''
        Temporary storage.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_text3'))

    x_crystal_vibrational_value1 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_value1'))

    x_crystal_vibrational_value2 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_value2'))

    x_crystal_vibrational_value3 = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Temporary storage
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_vibrational_value3'))

    x_crystal_section_irlo = SubSection(
        sub_section=SectionProxy('x_crystal_section_irlo'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irlo'))

    x_crystal_section_irto = SubSection(
        sub_section=SectionProxy('x_crystal_section_irto'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_irto'))

    x_crystal_section_thermodynamic = SubSection(
        sub_section=SectionProxy('x_crystal_section_thermodynamic'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_thermodynamic'))

    x_crystal_section_vibrational_modes = SubSection(
        sub_section=SectionProxy('x_crystal_section_vibrational_modes'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_modes'))

    x_crystal_section_vibrational_mode = SubSection(
        sub_section=SectionProxy('x_crystal_section_vibrational_mode'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_mode'))

    x_crystal_section_vibrational_multip = SubSection(
        sub_section=SectionProxy('x_crystal_section_vibrational_multip'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_multip'))

    x_crystal_section_vibrational_symmetry = SubSection(
        sub_section=SectionProxy('x_crystal_section_vibrational_symmetry'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_vibrational_symmetry'))


class x_crystal_section_wavefunctions_atom(MSection):
    '''
    Wavefunctions of an atom: initial conditions
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_wavefunctions_atom'))

    x_crystal_wavefunctions_atom_accuracy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ZNUC SCFIT  TOTAL HF ENERGY   KINETIC ENERGY   VIRIAL THEOREM ACCURACY. 11.0  12
        -1.616362095E+02  1.622491907E+02 -1.996221977E+00  2.6E-06
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_accuracy'))

    x_crystal_wavefunctions_atom_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ZNUC SCFIT  TOTAL HF ENERGY   KINETIC ENERGY   VIRIAL THEOREM ACCURACY. 11.0  12
        -1.616362095E+02  1.622491907E+02 -1.996221977E+00  2.6E-06
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_kinetic_energy'))

    x_crystal_wavefunctions_atom_nuclear_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): NUCLEAR CHARGE 11.0  SYMMETRY SPECIES            S
        P
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_nuclear_charge'))

    x_crystal_wavefunctions_atom_number_of_closed_shells_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): NUMBER OF CLOSED SHELLS     S:2    P:1
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_number_of_closed_shells_p'))

    x_crystal_wavefunctions_atom_number_of_closed_shells_s = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): NUMBER OF CLOSED SHELLS     S:2    P:1
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_number_of_closed_shells_s'))

    x_crystal_wavefunctions_atom_number_of_contracted_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): NUMBER OF CONTRACTED GTOS   S:4    P:3
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_number_of_contracted_p'))

    x_crystal_wavefunctions_atom_number_of_contracted_s = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): NUMBER OF CONTRACTED GTOS   S:4    P:3
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_number_of_contracted_s'))

    x_crystal_wavefunctions_atom_number_of_electrons = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): N. ELECTRONS   11.0  NUMBER OF PRIMITIVE GTOS   S:15
        P:7
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_number_of_electrons'))

    x_crystal_wavefunctions_atom_number_of_primitive_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): NUMBER OF PRIMITIVE GTOS   S:15    P:7
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_number_of_primitive_p'))

    x_crystal_wavefunctions_atom_number_of_primitive_s = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): NUMBER OF PRIMITIVE GTOS   S:15    P:7
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_number_of_primitive_s'))

    x_crystal_wavefunctions_atom_open_shell_occupation_p = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): OPEN SHELL OCCUPATION       S:1    P:0
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_open_shell_occupation_p'))

    x_crystal_wavefunctions_atom_open_shell_occupation_s = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        as in ATOMIC WAVEFUNCTION(S): OPEN SHELL OCCUPATION       S:1    P:0
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_open_shell_occupation_s'))

    x_crystal_wavefunctions_atom_scfit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        ZNUC SCFIT  TOTAL HF ENERGY   KINETIC ENERGY   VIRIAL THEOREM ACCURACY. 11.0  12
        -1.616362095E+02  1.622491907E+02 -1.996221977E+00  2.6E-06
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_scfit'))

    x_crystal_wavefunctions_atom_total_hf_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ZNUC SCFIT  TOTAL HF ENERGY   KINETIC ENERGY   VIRIAL THEOREM ACCURACY. 11.0  12
        -1.616362095E+02  1.622491907E+02 -1.996221977E+00  2.6E-06
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_total_hf_energy'))

    x_crystal_wavefunctions_atom_virial_theorem = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ZNUC SCFIT  TOTAL HF ENERGY   KINETIC ENERGY   VIRIAL THEOREM ACCURACY. 11.0  12
        -1.616362095E+02  1.622491907E+02 -1.996221977E+00  2.6E-06
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_virial_theorem'))

    x_crystal_wavefunctions_atom_znuc = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        ZNUC SCFIT  TOTAL HF ENERGY   KINETIC ENERGY   VIRIAL THEOREM ACCURACY. 11.0  12
        -1.616362095E+02  1.622491907E+02 -1.996221977E+00  2.6E-06
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_wavefunctions_atom_znuc'))


class x_crystal_section_wavefunctions(MSection):
    '''
    Wavefunctions
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='x_crystal_section_wavefunctions'))

    x_crystal_section_wavefunctions_atom = SubSection(
        sub_section=SectionProxy('x_crystal_section_wavefunctions_atom'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_wavefunctions_atom'))


class section_system(public.section_system):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_system'))

    x_crystal_atoms_in_asymmetric_unit = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atoms in asymmetric unit.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_atoms_in_asymmetric_unit'))

    x_crystal_atoms_in_unit_cell = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Atoms in unit cell.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_atoms_in_unit_cell'))

    x_crystal_bohr_angstrom = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Conversion factor Bohr as Angstroms, used by Crystal.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_bohr_angstrom'))

    x_crystal_centring_code_d = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Centring code denumerator.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_centring_code_d'))

    x_crystal_centring_code_n = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Centring code nominator.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_centring_code_n'))

    x_crystal_class_ref = Quantity(
        type=str,
        shape=[],
        description='''
        Reference for crystal classes.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_class_ref'))

    x_crystal_class = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal class.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_class'))

    x_crystal_density = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Crystal density in g/cm3.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_density'))

    x_crystal_dielectric_tensor = Quantity(
        type=np.dtype(np.float64),
        shape=['n', 'n'],
        description='''
        Dielectric tensor for frequency calculations.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_dielectric_tensor'))

    x_crystal_dimensionality = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        System dimensionality.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_dimensionality'))

    x_crystal_family = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal family.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_family'))

    x_crystal_geometry_consistent = Quantity(
        type=bool,
        shape=[],
        description='''
        Geometry is consistent with the group.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_geometry_consistent'))

    x_crystal_lattice_parameters = Quantity(
        type=np.dtype(np.float64),
        shape=[6],
        description='''
        Lattice parameters in angstroms and angles.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_lattice_parameters'))

    x_crystal_number_of_symmops = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Number of symmetry operators.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_number_of_symmops'))

    x_crystal_spacegroup_class = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal spacegroup class
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_spacegroup_class'))

    x_crystal_spacegroup = Quantity(
        type=str,
        shape=[],
        description='''
        Crystal spacegroup string resembling Hermann–Mauguin notation.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_spacegroup'))

    x_crystal_volume = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Simulation cell volume, in cubic angstroms.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_volume'))

    x_crystal_pointgroup = Quantity(
        type=str,
        shape=[],
        description='''
        Pointgroup number name.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_pointgroup'))

    x_crystal_pointgroup_number = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Pointgroup number.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_pointgroup_number'))

    x_crystal_pointgroup_number2 = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Pointgroup number 2.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_pointgroup_number2'))

    x_crystal_pointgroup_corresponding_spacegroup = Quantity(
        type=str,
        shape=[],
        description='''
        Spacegroup corresponding to the pointgroup.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_pointgroup_corresponding_spacegroup'))

    x_crystal_section_basis_set = SubSection(
        sub_section=SectionProxy('x_crystal_section_basis_set'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_basis_set'))

    x_crystal_section_cell = SubSection(
        sub_section=SectionProxy('x_crystal_section_cell'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_cell'))

    x_crystal_section_conventional_cell = SubSection(
        sub_section=SectionProxy('x_crystal_section_conventional_cell'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_conventional_cell'))

    x_crystal_section_frequency = SubSection(
        sub_section=SectionProxy('x_crystal_section_frequency'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_frequency'))

    x_crystal_section_info = SubSection(
        sub_section=SectionProxy('x_crystal_section_info'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_info'))

    x_crystal_section_kpoints = SubSection(
        sub_section=SectionProxy('x_crystal_section_kpoints'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_kpoints'))

    x_crystal_section_lattice = SubSection(
        sub_section=SectionProxy('x_crystal_section_lattice'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_lattice'))

    x_crystal_section_neighbors = SubSection(
        sub_section=SectionProxy('x_crystal_section_neighbors'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_neighbors'))

    x_crystal_section_primitive_cell = SubSection(
        sub_section=SectionProxy('x_crystal_section_primitive_cell'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_primitive_cell'))

    x_crystal_section_prim = SubSection(
        sub_section=SectionProxy('x_crystal_section_prim'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_prim'))

    x_crystal_section_symmetry = SubSection(
        sub_section=SectionProxy('x_crystal_section_symmetry'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_symmetry'))


class section_single_configuration_calculation(public.section_single_configuration_calculation):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_single_configuration_calculation'))

    x_crystal_initial_atomic_charges = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        scf cycles, initial step (e.g. TOTAL ATOMIC CHARGES:. 10.0000000  10.0000000)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_initial_atomic_charges'))

    x_crystal_initial_charge_normalization = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        scf cycles, initial step (e.g. CHARGE NORMALIZATION FACTOR   1.00000000)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_initial_charge_normalization'))

    x_crystal_initial_monmo3_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        scf cycles, initial step (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT MONMO3      TELAPSE
        0.62 TCPU        0.62)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_initial_monmo3_tcpu'))

    x_crystal_initial_monmo3_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles, initial step (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT MONMO3
        TELAPSE        0.62 TCPU        0.62)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_initial_monmo3_telapse'))

    x_crystal_initial_moqgad_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        scf cycles, initial step (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT MOQGAD      TELAPSE
        0.07 TCPU        0.07)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_initial_moqgad_tcpu'))

    x_crystal_initial_moqgad_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        scf cycles, initial step (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT MOQGAD      TELAPSE
        0.07 TCPU        0.07)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_initial_moqgad_telapse'))

    x_crystal_initial_shellx2_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        scf cycles, initial step (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT SHELLX2     TELAPSE
        0.61 TCPU        0.61)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_initial_shellx2_tcpu'))

    x_crystal_initial_shellx2_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        scf cycles, initial step (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT SHELLX2     TELAPSE
        0.61 TCPU        0.61)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_initial_shellx2_telapse'))

    x_crystal_scf_cycles = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Cycles when converged.
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_cycles'))

    x_crystal_scf_final_cycle = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        Final scf step, cycle number (e.g. in TOTAL ENERGY(HF)(AU)(  22)
        -6.2149540004172E+02 DE-3.7E-11 tst 1.6E-15 PX 1.2E-08)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_final_cycle'))

    x_crystal_scf_final_delta_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Final scf step, delta energy (e.g. in TOTAL ENERGY(HF)(AU)(  22)
        -6.2149540004172E+02 DE-3.7E-11 tst 1.6E-15 PX 1.2E-08)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_final_delta_energy'))

    x_crystal_scf_final_px = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Final scf step, px value (e.g. in TOTAL ENERGY(HF)(AU)(  22) -6.2149540004172E+02
        DE-3.7E-11 tst 1.6E-15 PX 1.2E-08)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_final_px'))

    x_crystal_scf_final_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Final scf step, total energy (e.g. in TOTAL ENERGY(HF)(AU)(  22)
        -6.2149540004172E+02 DE-3.7E-11 tst 1.6E-15 PX 1.2E-08)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_final_total_energy'))

    x_crystal_scf_final_tst = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Final scf step, tst value (e.g. in TOTAL ENERGY(HF)(AU)(  22) -6.2149540004172E+02
        DE-3.7E-11 tst 1.6E-15 PX 1.2E-08)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_final_tst'))

    x_crystal_scf_mode = Quantity(
        type=str,
        shape=[],
        description='''
        SCF mode (e.g. HF).
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_mode'))

    x_crystal_section_forces = SubSection(
        sub_section=SectionProxy('x_crystal_section_forces'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_forces'))

    x_crystal_section_wavefunctions = SubSection(
        sub_section=SectionProxy('x_crystal_section_wavefunctions'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_wavefunctions'))


class section_scf_iteration(public.section_scf_iteration):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_scf_iteration'))

    x_crystal_scf_atomic_charges = Quantity(
        type=np.dtype(np.float64),
        shape=['n'],
        description='''
        subsequent scf cycles (e.g.  TOTAL ATOMIC CHARGES:. 10.0158876   9.9841124)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_atomic_charges'))

    x_crystal_scf_bielet_zone_ee = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: BIELET ZONE E-E
        5.7175063847322E+02
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_bielet_zone_ee'))

    x_crystal_scf_charge_normalization = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. CHARGE NORMALIZATION FACTOR   1.00000000)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_charge_normalization'))

    x_crystal_scf_cycle = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        subsequent scf cycles, number of a particular scf iteration cycle (e.g.  CYC   0
        ETOT(AU) -2.750919138897E+02 DETOT -2.75E+02 tst  0.00E+00 PX  1.00E+00)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_cycle'))

    x_crystal_scf_ext_elpole = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: EXT EL-POLE
        -5.2914791274154E+02
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_ext_elpole'))

    x_crystal_scf_ext_spheropole = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: EXT EL-SPHEROPOLE
        3.9924168445258E+00
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_ext_spheropole'))

    x_crystal_scf_fdik_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT FDIK        TELAPSE
        0.63 TCPU        0.63)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_fdik_tcpu'))

    x_crystal_scf_fdik_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT FDIK        TELAPSE
        0.63 TCPU        0.63)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_fdik_telapse'))

    x_crystal_scf_insulating_state = Quantity(
        type=bool,
        shape=[],
        description='''
        subsequent scf cycles (contains text INSULATING STATE)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_insulating_state'))

    x_crystal_scf_kinetic_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: KINETIC ENERGY
        2.7465596172356E+02
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_kinetic_energy'))

    x_crystal_scf_monmo3_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT MONMO3      TELAPSE
        1.20 TCPU        1.20)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_monmo3_tcpu'))

    x_crystal_scf_monmo3_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT MONMO3      TELAPSE
        1.20 TCPU        1.20)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_monmo3_telapse'))

    x_crystal_scf_moqgad_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT MOQGAD      TELAPSE
        0.63 TCPU        0.63)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_moqgad_tcpu'))

    x_crystal_scf_moqgad_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT MOQGAD      TELAPSE
        0.63 TCPU        0.63)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_moqgad_telapse'))

    x_crystal_scf_pdig_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT PDIG        TELAPSE
        0.63 TCPU        0.63)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_pdig_tcpu'))

    x_crystal_scf_pdig_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT PDIG        TELAPSE
        0.63 TCPU        0.63)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_pdig_telapse'))

    x_crystal_scf_px = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. CYC   0 ETOT(AU) -2.750919138897E+02 DETOT -2.75E+02
        tst  0.00E+00 PX  1.00E+00)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_px'))

    x_crystal_scf_shellx2_tcpu = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT SHELLX2     TELAPSE
        1.19 TCPU        1.19)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_shellx2_tcpu'))

    x_crystal_scf_shellx2_telapse = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT SHELLX2     TELAPSE
        1.19 TCPU        1.19)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_shellx2_telapse'))

    x_crystal_scf_total_ee = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL E-E
        4.6595142576204E+01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_total_ee'))

    x_crystal_scf_total_en_ne = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL E-N + N-E
        -5.2283101954878E+02
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_total_en_ne'))

    x_crystal_scf_total_energy = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL   ENERGY
        -2.7466419192577E+02
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_total_energy'))

    x_crystal_scf_total_nn = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: TOTAL N-N
        -7.3084276676762E+01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_total_nn'))

    x_crystal_scf_tst = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. CYC   0 ETOT(AU) -2.750919138897E+02 DETOT -2.75E+02
        tst  0.00E+00 PX  1.00E+00)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_tst'))

    x_crystal_scf_valence_band = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TOP OF VALENCE BANDS -    BAND     10; K    1; EIG
        -3.4527266E-01 AU)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_valence_band'))

    x_crystal_scf_valence_eig = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TOP OF VALENCE BANDS -    BAND     10; K    1; EIG
        -3.4527266E-01 AU)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_valence_eig'))

    x_crystal_scf_valence_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        subsequent scf cycles (e.g. TOP OF VALENCE BANDS -    BAND     10; K    1; EIG
        -3.4527266E-01 AU)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_valence_k'))

    x_crystal_scf_virial_coefficient = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        +++ ENERGIES IN A.U. +++. ::: VIRIAL COEFFICIENT
        9.9998501747632E-01
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_virial_coefficient'))

    x_crystal_scf_virtual_band = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        subsequent scf cycles (e.g. BOTTOM OF VIRTUAL BANDS - BAND     11; K    1; EIG
        3.7948795E-01 AU)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_virtual_band'))

    x_crystal_scf_virtual_eig = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        subsequent scf cycles (e.g. BOTTOM OF VIRTUAL BANDS - BAND     11; K    1; EIG
        3.7948795E-01 AU)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_virtual_eig'))

    x_crystal_scf_virtual_k = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        subsequent scf cycles (e.g. BOTTOM OF VIRTUAL BANDS - BAND     11; K    1; EIG
        3.7948795E-01 AU)
        ''',
        a_legacy=LegacyDefinition(name='x_crystal_scf_virtual_k'))


class section_run(public.section_run):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_run'))

    x_crystal_section_endinformation = SubSection(
        sub_section=SectionProxy('x_crystal_section_endinformation'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_endinformation'))

    x_crystal_section_header = SubSection(
        sub_section=SectionProxy('x_crystal_section_header'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_header'))

    x_crystal_section_input = SubSection(
        sub_section=SectionProxy('x_crystal_section_input'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_input'))

    x_crystal_section_process = SubSection(
        sub_section=SectionProxy('x_crystal_section_process'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_process'))

    x_crystal_section_properties = SubSection(
        sub_section=SectionProxy('x_crystal_section_properties'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_properties'))

    x_crystal_section_startinformation = SubSection(
        sub_section=SectionProxy('x_crystal_section_startinformation'),
        repeats=True,
        a_legacy=LegacyDefinition(name='x_crystal_section_startinformation'))


m_package.__init_metainfo__()
