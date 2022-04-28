# imports
import unittest
import sys, os, inspect
import numpy as np

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from scripts import shared_sites

class TestSharedSites(unittest.TestCase):
    q1 = [0, 0, 0, 0, 0]
    q2 = [1, 1, 1, 1, 1]
    q3 = [0, 1, 0, 1, 2]
    m1 = [0, 0, 0, 0, 0]
    m2 = [1, 1, 1, 1, 1]
    m3 = [2, 2, 2, 2, 2]

    def test_count_shared_sites(self):
        self.assertEqual(shared_sites.count_shared_sites(self.q1, self.m1), 5)
        self.assertEqual(shared_sites.count_shared_sites(self.q1, self.m2), 0)
        self.assertEqual(shared_sites.count_shared_sites(self.q1, self.m3), 0)
        self.assertEqual(shared_sites.count_shared_sites(self.q2, self.m1), 0)
        self.assertEqual(shared_sites.count_shared_sites(self.q2, self.m2), 5)
        self.assertEqual(shared_sites.count_shared_sites(self.q2, self.m3), 0)
        self.assertEqual(shared_sites.count_shared_sites(self.q3, self.m1), 2)
        self.assertEqual(shared_sites.count_shared_sites(self.q3, self.m2), 2)
        self.assertEqual(shared_sites.count_shared_sites(self.q3, self.m3), 1)

    def test_percent_shared_sites(self):
        self.assertEqual(shared_sites.percent_shared_sites(self.q1, self.m1), 1.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q1, self.m2), 0.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q1, self.m3), 0.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q2, self.m1), 0.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q2, self.m2), 1.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q2, self.m3), 0.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q3, self.m1), 0.4)
        self.assertEqual(shared_sites.percent_shared_sites(self.q3, self.m2), 0.4)
        self.assertEqual(shared_sites.percent_shared_sites(self.q3, self.m3), 0.2)


class TestOrderedIndices(unittest.TestCase):
    ssp = [[1., 0., .8, .4, .3]]
    i = [[0, 2, 3, 4, 1]]

    def test_sort_shared_sites_percentages(self):
        print(list(shared_sites.sort_shared_sites_percentages(self.ssp)))
        print(self.i)
        self.assertTrue((shared_sites.sort_shared_sites_percentages(self.ssp) == self.i), True)




if __name__ == '__main__':
    unittest.main()
