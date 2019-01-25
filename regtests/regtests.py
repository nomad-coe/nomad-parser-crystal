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

import os
import unittest
import logging
import numpy as np
from crystalparser import CrystalParser
from nomadcore.unit_conversion.unit_conversion import convert_unit


def get_result(folder, metaname=None):
    """Get the results from the calculation in the given folder. By default goes through different

    Args:
        folder: The folder relative to the directory of this script where the
            parsed calculation resides.
        metaname(str): Optional quantity to return. If not specified, returns
            the full dictionary of results.
    """
    dirname = os.path.dirname(__file__)
    filename = os.path.join("crystal_{}".format(VERSION), dirname, folder, "output.out")
    parser = CrystalParser(None, debug=True, log_level=logging.CRITICAL)
    results = parser.parse(filename)

    if metaname is None:
        return results
    else:
        return results[metaname]


class TestSinglePointHF(unittest.TestCase):
    """Tests that the parser can handle DFT energy calculations.
    """
    @classmethod
    def setUpClass(cls):
        cls.results = get_result("single_point/hf")
        # cls.results.print_summary()

    def test_program_name(self):
        result = self.results["program_name"]
        self.assertEqual(result, "Crystal")

    def test_program_version(self):
        result = self.results["program_version"]
        self.assertEqual(result, "14")

    def test_energy_total(self):
        result = self.results["energy_total"]
        expected_result = convert_unit(np.array(-2.7466419192575E+02), "hartree")
        self.assertTrue(np.array_equal(result, expected_result))

    def test_atom_labels(self):
        atom_labels = self.results["atom_labels"]
        expected_labels = np.array(["Mg", "O"])
        self.assertTrue(np.array_equal(atom_labels, expected_labels))

    def test_atom_positions(self):
        atom_position = self.results["atom_positions"]
        expected_position = convert_unit(np.array(
            [
                [0.000000000000E+00, 0.000000000000E+00, 0.000000000000E+00],
                [2.105000000000E+00, 2.105000000000E+00, 2.105000000000E+00],
            ]
        ), "angstrom")
        self.assertTrue(np.array_equal(atom_position, expected_position))

    def test_number_of_atoms(self):
        n_atoms = self.results["number_of_atoms"]
        self.assertEqual(n_atoms, 2)

    def test_electronic_structure_method(self):
        result = self.results["electronic_structure_method"]
        self.assertEqual(result, "DFT")

    def test_single_configuration_to_calculation_method_ref(self):
        result = self.results["single_configuration_calculation_to_method_ref"]
        self.assertEqual(result, 0)

    def test_single_configuration_calculation_to_system_description_ref(self):
        result = self.results["single_configuration_calculation_to_system_ref"]
        self.assertEqual(result, 0)

    def test_simulation_cell(self):
        cell = self.results["simulation_cell"]
        n_vectors = cell.shape[0]
        n_dim = cell.shape[1]
        self.assertEqual(n_vectors, 3)
        self.assertEqual(n_dim, 3)
        expected_cell = convert_unit(np.array(
            [
                [0.000000000000E+00, 0.210500000000E+01, 0.210500000000E+01],
                [0.210500000000E+01, 0.000000000000E+00, 0.210500000000E+01],
                [0.210500000000E+01, 0.210500000000E+01, 0.000000000000E+00]]
            ),
            "angstrom"
        )
        self.assertTrue(np.array_equal(cell, expected_cell))


class TestSinglePointDFT(unittest.TestCase):
    """Tests that the parser can handle DFT energy calculations.
    """
    @classmethod
    def setUpClass(cls):
        cls.results = get_result("single_point/dft")
        # cls.results.print_summary()

    def test_program_name(self):
        result = self.results["program_name"]
        self.assertEqual(result, "Crystal")

    def test_program_version(self):
        result = self.results["program_version"]
        self.assertEqual(result, "14")

    def test_program_basis_set_type(self):
        result = self.results["program_basis_set_type"]
        self.assertEqual(result, "gaussians")

    def test_energy_total(self):
        result = self.results["energy_total"]
        expected_result = convert_unit(np.array(-5.7330058382967E+02), "hartree")
        self.assertTrue(np.array_equal(result, expected_result))

    def test_atom_labels(self):
        atom_labels = self.results["atom_labels"]
        expected_labels = np.array(["Si", "Si"])
        self.assertTrue(np.array_equal(atom_labels, expected_labels))

    def test_atom_positions(self):
        atom_position = self.results["atom_positions"]
        expected_position = convert_unit(np.array(
            [
                [6.775000000000E-01, 6.775000000000E-01, 6.775000000000E-01],
                [-6.775000000000E-01, -6.775000000000E-01, -6.775000000000E-01],
            ]
        ), "angstrom")
        self.assertTrue(np.array_equal(atom_position, expected_position))

    def test_number_of_atoms(self):
        n_atoms = self.results["number_of_atoms"]
        self.assertEqual(n_atoms, 2)

    def test_electronic_structure_method(self):
        result = self.results["electronic_structure_method"]
        self.assertEqual(result, "DFT")

    def test_single_configuration_to_calculation_method_ref(self):
        result = self.results["single_configuration_calculation_to_method_ref"]
        self.assertEqual(result, 0)

    def test_single_configuration_calculation_to_system_description_ref(self):
        result = self.results["single_configuration_calculation_to_system_ref"]
        self.assertEqual(result, 0)

    def test_simulation_cell(self):
        cell = self.results["simulation_cell"]
        n_vectors = cell.shape[0]
        n_dim = cell.shape[1]
        self.assertEqual(n_vectors, 3)
        self.assertEqual(n_dim, 3)
        expected_cell = convert_unit(np.array(
            [
                [0.000000000000E+00, 0.271000000000E+01, 0.271000000000E+01],
                [0.271000000000E+01, 0.000000000000E+00, 0.271000000000E+01],
                [0.271000000000E+01, 0.271000000000E+01, 0.000000000000E+00]]
            ),
            "angstrom"
        )
        self.assertTrue(np.array_equal(cell, expected_cell))

    def test_xc_functional(self):
        result = self.results["xc_functional"]
        self.assertEqual(result, "1.0*GGA_X_B88+1.0*LDA_C_PZ")

        names = self.results["xc_functional_name"]
        self.assertTrue(np.array_equal(names, np.array(["GGA_X_B88", "LDA_C_PZ"])))

    def test_scf_max_iteration(self):
        result = self.results["scf_max_iteration"]
        self.assertEqual(result, 50)

    def test_single_configuration_calculation_converged(self):
        result = self.results["single_configuration_calculation_converged"]
        self.assertTrue(result)

    def test_scf_threshold_energy_change(self):
        result = self.results["scf_threshold_energy_change"]
        self.assertEqual(result, convert_unit(1.00E-07, "hartree"))

    def test_scf_dft_number_of_iterations(self):
        result = self.results["number_of_scf_iterations"]
        self.assertEqual(result, 9)

    def test_energy_total_scf_iteration(self):
        result = self.results["energy_total_scf_iteration"]
        # Test the first and last energies
        expected_result = convert_unit(np.array(
            [
                [-5.730466534391E+02],
                [-5.733005838297E+02],
            ]), "hartree")
        self.assertTrue(np.array_equal(np.array([[result[0]], [result[-1]]]), expected_result))

    def test_energy_change_scf_iteration(self):
        result = self.results["energy_change_scf_iteration"]
        expected_result = convert_unit(np.array(
            [
                [-5.73E+02],
                [-3.17E-08],
            ]), "hartree")
        self.assertTrue(np.array_equal(np.array([[result[0]], [result[-1]]]), expected_result))

if __name__ == '__main__':

    VERSIONS = ["14"]

    for VERSION in VERSIONS:
        suites = []
        suites.append(unittest.TestLoader().loadTestsFromTestCase(TestSinglePointHF))
        suites.append(unittest.TestLoader().loadTestsFromTestCase(TestSinglePointDFT))
        alltests = unittest.TestSuite(suites)
        unittest.TextTestRunner(verbosity=0).run(alltests)
