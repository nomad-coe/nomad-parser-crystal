import pytest
import numpy as np
from crystalparser import CrystalParser
from nomad.datamodel import EntryArchive
from nomad.parsing.parsers import match_parser


def test_misc():
    """Generic tests for exceptional cases that the parser needs to take into
    consideration.
    """
    # The atomic number is given in the NAT convention
    filepath = "./misc/nat/HfS2_PBE0D3_ZD_fc3_supercell-00497.o"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    system = archive.section_run[0].section_system[0]
    assert set(system.atom_species) == set((16, 72))

    # Tests that ghost atoms are ignored in the system. Maybe they need their
    # own metainfo?
    filepath = "./misc/ghosts/fevo46_sngt_ti_zero.cryst.out"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    system = archive.section_run[0].section_system[0]
    assert set(system.atom_species) == set((8, 26, 22, 38))

    # Tests that supercells are handled correctly
    filepath = "./misc/supercell/fevo_x16_76_re.cryst.out"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)

    # Tests that substitutions are handled correctly
    filepath = "./misc/substitution/neutral.cryst.out"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    system = archive.section_run[0].section_system[0]
    assert set(system.atom_species) == set((8, 26, 22, 38))

    # Geometry optimization with constraints
    filepath = "./misc/constraints/ionic1_fullspin_spinfx_2.cryst.out"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)


def test_xc_functionals():
    """Tests that different kinds of XC functionals are correctly identified.
    """
    # PBE
    filepath = "./xc_functionals/pbe_1/supercell-00138.o"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    method = archive.section_run[0].section_method[0]
    assert method.XC_functional == "1.0*GGA_C_PBE+1.0*GGA_X_PBE"

    # PW91 Hybrid
    filepath = "./xc_functionals/pw91_hybrid/f075_l3_ph.o"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    method = archive.section_run[0].section_method[0]
    assert method.XC_functional == "1.0*GGA_C_PW91+0.9*GGA_X_PW91+0.1*HF_X"

    # WC1LYP
    filepath = "./xc_functionals/wc1lyp/albite_freq_intens.out"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    method = archive.section_run[0].section_method[0]
    assert method.XC_functional == "1.0*GGA_C_LYP+0.84*GGA_X_WC+0.16*HF_X"

    # PBE0
    filepath = "./xc_functionals/pbe0/ZrS2_band_structure_dos.prop.o"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive)
    method = archive.section_run[0].section_method[0]
    assert method.XC_functional == "1.0*HYB_GGA_XC_PBEH"


def test_molecule():
    """Tests that molecular calculations are parsed correctly.
    """
    filepath = "./molecule/w.out"
    archive = parse(filepath)
    asserts_basic(archive, system_type="0D")
    asserts_basic_code_specific(archive, system_type="0D")
    method = archive.section_run[0].section_method[0]
    assert method.XC_functional == "1.0*HYB_GGA_XC_PBEH"

def test_single_point_dft():
    """Tests that single point DFT calculations are parsed succesfully.
    """
    filepath = "./single_point/dft/output.out"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive, vdw="DFT-D3", forces=True)


def test_single_point_hf():
    """Tests that single point HF calculations are parsed succesfully.
    """
    filepath = "./single_point/hf/output.out"
    archive = parse(filepath)
    asserts_basic(archive, method_type="HF")
    asserts_basic_code_specific(archive, method_type="HF")


def test_single_point_forces():
    """Tests that forces are correctly parsed.
    """
    filepath = "./single_point/forces/HfS2_PBE0D3_ZD_fc3_supercell-00001.o"
    archive = parse(filepath)
    asserts_basic(archive, vdw="DFT-D3", forces=True)
    asserts_basic_code_specific(archive)


def test_geo_opt():
    """Tests that geometry optimization is parsed correctly.
    """
    filepath = "./geo_opt/nio_tzvp_pbe0_opt.o"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive, run_type="geo_opt")
    asserts_geo_opt(archive)


def test_band_structure():
    """Tests that band structure calculation is parsed correctly. Especially parsing the
    """
    filepath = "./band_structure/nacl_hf/NaCl.out"
    archive = parse(filepath)
    asserts_basic(archive, method_type="HF")
    asserts_basic_code_specific(archive, method_type="HF", run_type="band_structure")
    asserts_band_structure(archive)
    run = archive.section_run[0]
    method = run.section_method[0]
    assert method.XC_functional == "1.0*HF_X"


def test_band_structure_missing():
    """This band structure is missing the f25 file so not output should be
    generated for band structure. The functional should still be possible to
    read.
    """
    filepath = "./band_structure/tis2_dft/TiS2_band_structure.prop.o"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive, run_type="band_structure")
    run = archive.section_run[0]
    method = run.section_method[0]
    assert method.XC_functional == "1.0*HYB_GGA_XC_PBEH"


def test_dos():
    """Tests that DOS is parsed successfully.
    """
    filepath = "./dos/nacl_hf/NaCl.out"
    archive = parse(filepath)
    asserts_basic(archive)
    asserts_basic_code_specific(archive, run_type="dos")
    asserts_dos(archive)


def parse(filepath):
    parser = CrystalParser()
    archive = EntryArchive()
    logger = None
    parser.parse(filepath, archive, logger)
    return archive


def asserts_basic(archive, method_type="DFT", system_type="3D", vdw=None, forces=False):
    run = archive.section_run[0]
    systems = run.section_system
    method = run.section_method[0]
    sccs = run.section_single_configuration_calculation
    n_atoms = len(systems[0].atom_species)

    assert run
    assert sccs
    assert systems
    assert method

    assert run.program_name is not None
    assert run.program_version is not None
    assert run.time_run_date_start is not None
    assert run.time_run_date_end is not None

    if method_type == "DFT":
        assert method.XC_functional is not None
        assert method.electronic_structure_method == "DFT"
    if vdw:
        assert method.van_der_Waals_method == vdw

    for system in systems:
        assert system.atom_positions is not None
        assert system.atom_species is not None
        assert system.atom_labels is not None
        if system_type != "0D":
            assert system.lattice_vectors is not None
            assert system.lattice_vectors.shape == (3, 3)
            assert system.configuration_periodic_dimensions == [True, True, True]
        assert system.atom_positions.shape[0] == n_atoms
        assert system.atom_species.shape[0] == n_atoms
        assert len(system.atom_labels) == n_atoms

    assert method.scf_max_iteration is not None
    assert method.scf_threshold_energy_change is not None

    for scc in sccs:
        assert scc.single_configuration_calculation_to_system_ref is not None
        assert scc.single_configuration_to_calculation_method_ref is not None
        scf = scc.section_scf_iteration
        if scf:
            assert scc.single_configuration_calculation_converged is True
            assert scc.number_of_scf_iterations is not None
            for scf in scc.section_scf_iteration:
                assert scf.energy_total_scf_iteration is not None
                assert scf.energy_change_scf_iteration is not None
        if forces:
            assert scc.atom_forces is not None
            assert scc.atom_forces.shape[0] == n_atoms


def asserts_basic_code_specific(archive, method_type="DFT", system_type="3D", run_type="scf", vdw=None, forces=False):
    run = archive.section_run[0]
    systems = run.section_system
    method = run.section_method[0]
    sccs = run.section_single_configuration_calculation
    n_atoms = len(systems[0].atom_species)

    assert run.program_name == "Crystal"
    assert run.program_basis_set_type == "gaussians"

    assert method.x_crystal_n_atoms is not None
    assert method.x_crystal_n_shells is not None
    assert method.x_crystal_n_orbitals is not None
    assert method.x_crystal_n_electrons is not None
    assert method.x_crystal_n_core_electrons is not None
    assert method.x_crystal_n_symmops is not None
    assert method.x_crystal_tol_coulomb_overlap is not None
    assert method.x_crystal_tol_coulomb_penetration is not None
    assert method.x_crystal_tol_exchange_overlap is not None
    assert method.x_crystal_tol_pseudo_overlap_f is not None
    assert method.x_crystal_tol_pseudo_overlap_p is not None
    assert method.x_crystal_pole_order is not None
    assert method.x_crystal_type_of_calculation is not None
    if system_type != "0D":
        assert method.x_crystal_is1 is not None
        assert method.x_crystal_is2 is not None
        assert method.x_crystal_is3 is not None
        assert method.x_crystal_k_pts_monk_net is not None
        assert method.x_crystal_symmops_k is not None
        assert method.x_crystal_symmops_g is not None
        assert method.x_crystal_shrink_gilat is not None
        assert method.x_crystal_n_k_points_ibz is not None
        assert method.x_crystal_shrink is not None
    assert method.x_crystal_weight_f is not None

    bases = run.section_basis_set_atom_centered
    for basis in bases:
        assert isinstance(basis.basis_set_atom_number, np.int32)
        for shell in basis.x_crystal_section_shell:
            assert shell.x_crystal_shell_type is not None
            assert shell.x_crystal_shell_range is not None
            assert shell.x_crystal_shell_coefficients.shape[1] == 4


def asserts_geo_opt(archive, method_type="DFT", system_type="3D", vdw=None, forces=False):
    run = archive.section_run[0]
    sampling_method = run.section_sampling_method[0]
    fs = run.section_frame_sequence[0]
    assert sampling_method.sampling_method == "geometry_optimization"
    assert sampling_method.geometry_optimization_energy_change is not None
    assert sampling_method.geometry_optimization_geometry_change is not None
    assert sampling_method.geometry_optimization_geometry_change is not None
    assert fs.frame_sequence_local_frames_ref is not None
    assert fs.number_of_frames_in_sequence is not None
    assert fs.geometry_optimization_converged is True


def asserts_band_structure(archive, method_type="DFT", system_type="3D", vdw=None, forces=False):
    run = archive.section_run[0]
    scc = run.section_single_configuration_calculation[0]
    bands = scc.section_k_band[0]
    assert scc.energy_reference_fermi is not None
    assert bands.reciprocal_cell.shape == (3, 3)
    assert bands.band_structure_kind is not None
    for segment in bands.section_k_band_segment:
        assert segment.band_k_points.shape[1] == 3
        assert segment.band_energies is not None
        assert segment.band_energies.shape[1] == segment.band_k_points.shape[0]
        assert segment.band_segm_start_end is not None
        assert segment.number_of_k_points_per_segment is not None


def asserts_dos(archive, method_type="DFT", system_type="3D", vdw=None, forces=False):
    run = archive.section_run[0]
    dos_found = False
    for scc in run.section_single_configuration_calculation:
        dos = scc.section_dos
        if dos:
            dos = dos[0]
            dos_found = True
            assert scc.energy_reference_fermi is not None or scc.energy_reference_highest_occupied is not None
            assert dos.dos_kind is not None
            assert dos.number_of_dos_values is not None
            assert dos.dos_energies.shape == (dos.number_of_dos_values,)
            assert dos.dos_values.shape == (1, dos.number_of_dos_values)
    assert dos_found


if __name__ == "__main__":
    test_single_point_forces()
    test_single_point_dft()
    test_single_point_hf()
    test_geo_opt()
    test_band_structure()
    test_band_structure_missing()
    test_dos()
    test_xc_functionals()
    test_molecule()
    test_misc()
