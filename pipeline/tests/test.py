# imports
import unittest
import sys, os, inspect
import numpy as np

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from scripts import read_map_file


class TestReadMapFile(unittest.TestCase):

    map_file = '/home/krsc0813/toy_data/plink/simple.map'
    kmers = [[],
             [], 
             []]

    def test_cm_kmers(self):
        self.assertEqusl(read_map_file).cm_kmers(self.map_filee), self.all_kmers)

if __name__ == '__main__':
    unittest.main()
