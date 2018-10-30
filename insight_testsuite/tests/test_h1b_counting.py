#!/usr/bin/python3
'''Unit tests for all functions in h1b_counting'''
from src.h1b_counting import check_parameters, yearly_headers, find_year, get_certified_h1b, sort_dictionaries, write_occupation, write_state
import os
import unittest
import subprocess


class TestData(unittest.TestCase):
    '''testing all functions in src/h1b_counting.py class'''

    @classmethod
    def setUpClass(cls):
        cls.occ_test = {'SOFTWARE DEVELOPERS, APPLICATIONS': 6, 'ACCOUNTANTS AND AUDITORS': 1, 'COMPUTER SYSTEMS ANALYST': 1, 'total': 10, 'COMPUTER OCCUPATIONS, ALL OTHER': 1, 'DATABASE ADMINISTRATORS': 1}
        cls.state_test = {'AL': 1, 'GA': 1, 'NJ': 1, 'CA': 1, 'FL': 2, 'total': 10, 'WA': 1, 'TX': 1, 'MD': 1, 'DE': 1}
        cls.input_file = 'h1b_input.csv'
        cls.input_path = './input'
        cls.header = yearly_headers['2017']
     
    @classmethod
    def tearDownClass(cls):
        del cls.occ_test
        del cls.state_test
        del cls.input_file
        del cls.input_path
        del cls.header

    def test_checking_docstrings_functions(self):
        self.assertIsNotNone(check_parameters.__doc__)
        self.assertIsNotNone(find_year.__doc__)
        self.assertIsNotNone(get_certified_h1b.__doc__)


    def test_find_year(self):
        input_file = 'H1B_FY_2017.csv'
        input_file2 = 'H1B_FY_2016.csv'
        input_file3 = 'h1b_input.csv'
        self.assertEqual(find_year(input_file), '2017')
        self.assertEqual(find_year(input_file2), '2016')
        self.assertEqual(find_year(input_file3), '2017')


    def test_sort(self):
        arr = []
        arr.append(sorted(self.occ_test.items(), key=lambda x: (-x[1], x[0])))
        arr.append(sorted(self.occ_test.items(), key=lambda x: (-x[1], x[0])))

        length = len(arr[0]) - 1
        for da_list in arr:
            for index in range(len(da_list)):
                if index < length:
                    self.assertTrue(da_list[index][1] >= da_list[index + 1][1])
    
    def test_open_file(self):
        occ, state = get_certified_h1b(self.input_path, self.input_file, self.header)
        self.assertDictEqual(self.occ_test, occ)
        self.assertDictEqual(self.state_test, state) 

if __name__ == '__main__':
    unittest.main()
