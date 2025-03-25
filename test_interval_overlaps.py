import interval_overlaps as io
from datetime import datetime
import unittest


class TestIntervalIntersect(unittest.TestCase):
    def test_single_interval_overlap(self):
        i1 = (1,3)
        i2 = (2,4)
        self.assertEqual(io.interval_intersection(i1,i2), (2,3))

    def test_time_interval_overlap(self):
        i1 = (datetime(2020,1,1,10,00), datetime(2020,1,2,10,00))
        i2 = (datetime(2020,1,1,14,00), datetime(2020,1,1,16,00))
        self.assertEqual(io.interval_intersection(i1,i2), i2)

class TestIntervalOverlap(unittest.TestCase):
    def test_edge_ovl_interval_pair(self):
        i1 = [1,3]
        i2 = [2,4]
        self.assertTrue(io.interval_overlaps(i1,i2))
        
    def test_inner_interval_pair(self):
        i1 = [1,2]
        i2 = [0,4]
        self.assertTrue(io.interval_overlaps(i1,i2))

    def test_outer_interval_pair(self):
        i2 = [1,2]
        i1 = [0,4]
        self.assertTrue(io.interval_overlaps(i1,i2))

    def test_non_ovl_interval_pair_rev(self):
        i2 = [1,2]
        i1 = [3,4]
        self.assertFalse(io.interval_overlaps(i1,i2))

    def test_non_ovl_interval_pair_fw(self):
        i1 = [1,2]
        i2 = [3,4]
        self.assertFalse(io.interval_overlaps(i1,i2))

    def test_three_interval(self):
        i1 = [1,3]
        i2 = [3,5]
        i3 = [4,6]
        self.assertTrue(io.interval_overlaps(i1,i2,i3))


class TestIntervalListOverlap(unittest.TestCase):
    def test_single_interval_overlap(self):
        il1 = [(1,3),(4,6)]
        il2 = [(-1,0),(2,3.5),(8,9)]
        self.assertEqual(io.interval_list_overlaps(il1,il2),[(0,1)])

    def test_single_interval_overlaps_two(self):
        il1 = [(1,3),(4,6)]
        il2 = [(-1,0),(3.5,4.5),(5,9)]
        self.assertEqual(io.interval_list_overlaps(il1,il2),[(1,1),(1,2)])

if __name__ == "__main__":
    unittest.main()



