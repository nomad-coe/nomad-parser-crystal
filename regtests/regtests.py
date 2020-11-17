import pytest
from crystalparser import CrystalParser
from nomad.datamodel import EntryArchive


def test_single_point_dft():
    """Tests that single point DFT calculations are parsed succesfully.
    """
    filepath = "./single_point/dft/output.out"
    archive = parse(filepath)
    asserts_basic(archive)


def test_single_point_hf():
    """Tests that single point HF calculations are parsed succesfully.
    """
    filepath = "./single_point/hf/output.out"
    archive = parse(filepath)
    asserts_basic(archive, method_type="HF")

def test_single_point_forces():
    """Tests that forces are correctly parsed.
    """
    filepath = "./single_point/forces/HfS2_PBE0D3_ZD_fc3_supercell-00001.o"
    archive = parse(filepath)
    asserts_basic(archive, vdw="DFT-D3", forces=True)


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


if __name__ == "__main__":
    test_single_point_forces()
