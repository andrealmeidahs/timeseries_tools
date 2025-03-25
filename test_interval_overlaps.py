import interval_overlaps as io
import unittest

class TestIntervalOverlap(unittest.TestCase):
    def test_edge_ovl_interval_pair(self):
        i1 = [1,3]
        i2 = [2,4]
        self.assertTrue(io.interval_overlap(i1,i2))
        
    def test_inner_interval_pair(self):
        i1 = [1,2]
        i2 = [0,4]
        self.assertTrue(io.interval_overlap(i1,i2))

    def test_outer_interval_pair(self):
        i2 = [1,2]
        i1 = [0,4]
        self.assertTrue(io.interval_overlap(i1,i2))

    def test_non_ovl_interval_pair_rev(self):
        i2 = [1,2]
        i1 = [3,4]
        self.assertFalse(io.interval_overlap(i1,i2))

    def test_non_ovl_interval_pair_fw(self):
        i1 = [1,2]
        i2 = [3,4]
        self.assertFalse(io.interval_overlap(i1,i2))


if __name__ == "__main__":
    unittest.main()



