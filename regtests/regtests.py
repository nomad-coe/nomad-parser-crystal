import pytest
import numpy as np
from crystalparser import CrystalParser
from nomad.datamodel import EntryArchive


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
    asserts_basic_code_specific(archive)
    asserts_geo_opt(archive)

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

    assert run.program_name == "Crystal"
    assert run.program_basis_set_type == "gaussians"
    assert run.time_run_date_start is not None
    assert run.time_run_date_end is not None

    if method_type == "DFT":
        assert run.electronic_structure_method == "DFT"
        assert method.XC_functional is not None
    if vdw:
        assert method.van_der_Waals_method == vdw

    for system in systems:
        assert system.atom_positions is not None
        assert system.atom_species is not None
        assert system.lattice_vectors is not None
        assert system.lattice_vectors.shape == (3, 3)
        if system_type == "3D":
            assert system.configuration_periodic_dimensions == [True, True, True]
        assert system.atom_positions.shape[0] == n_atoms
        assert system.atom_species.shape[0] == n_atoms

    assert method.scf_max_iteration is not None
    assert method.scf_threshold_energy_change is not None

    for scc in sccs:
        assert scc.energy_total is not None
        assert scc.number_of_scf_iterations is not None
        assert scc.single_configuration_calculation_converged is True
        for scf in scc.section_scf_iteration:
            assert scf.energy_total_scf_iteration is not None
            assert scf.energy_change_scf_iteration is not None
        if forces:
            assert scc.atom_forces is not None
            assert scc.atom_forces.shape[0] == n_atoms

def asserts_basic_code_specific(archive, method_type="DFT", system_type="3D", vdw=None, forces=False):
    run = archive.section_run[0]
    systems = run.section_system
    method = run.section_method[0]
    sccs = run.section_single_configuration_calculation
    n_atoms = len(systems[0].atom_species)

    assert run.x_crystal_run_title is not None
    assert run.x_crystal_hostname is not None
    assert run.x_crystal_datetime is not None
    assert run.x_crystal_distribution is not None
    assert run.x_crystal_version_minor is not None
    assert run.x_crystal_version_date is not None
    assert run.x_crystal_input_path is not None
    assert run.x_crystal_output_path is not None
    assert run.x_crystal_executable_path is not None
    assert run.x_crystal_tmpdir is not None

    # print(method.x_crystal_n_k_points_gilat)
    assert method.x_crystal_fock_ks_matrix_mixing is not None
    assert method.x_crystal_coulomb_bipolar_buffer is not None
    assert method.x_crystal_exchange_bipolar_buffer is not None
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
    assert method.x_crystal_is1 is not None
    assert method.x_crystal_is2 is not None
    assert method.x_crystal_is3 is not None
    assert method.x_crystal_k_pts_monk_net is not None
    assert method.x_crystal_symmops_k is not None
    assert method.x_crystal_symmops_g is not None
    assert method.x_crystal_convergence_deltap is not None
    assert method.x_crystal_shrink is not None
    assert method.x_crystal_shrink_gilat is not None
    assert method.x_crystal_weight_f is not None
    assert method.x_crystal_n_k_points_ibz is not None
    assert method.x_crystal_n_k_points_gilat is not None
    if method_type == "DFT":
        assert method.x_crystal_toldee is not None

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
    assert sampling_method.sampling_method == "geometry_optimization"
    assert sampling_method.geometry_optimization_energy_change is not None
    assert sampling_method.geometry_optimization_geometry_change is not None

if __name__ == "__main__":
    # test_single_point_forces()
    # test_single_point_dft()
    # test_single_point_hf()
    test_geo_opt()
