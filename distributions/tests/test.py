# imports
import unittest
import sys, os, inspect
import numpy as np

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from scripts import sample_major_format


class TestSampleMajorFormat(unittest.TestCase):

    def test_transpose_data(self):
        self.assertNotEqual(sample_major_format.transpose_data(self.db1), self.smf2)

if __name__ == '__main__':
    unittest.main()
