import subset_sums
import unittest


class TestGrid(unittest.TestCase):

    def subset_sum_should_not_work(self):
        k = 3
        set = [1,1]
        res = subset_sums.find_subset_that_sum_equals_k(set, k)
        self.assertFalse(res)
