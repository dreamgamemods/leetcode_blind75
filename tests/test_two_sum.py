import unittest
from solutions import TwoSum

class TestTwoSum(unittest.TestCase):

    def test_twosum(self):
        ts = TwoSum()

        self.assertEqual(ts.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(ts.twoSum([1, 2, 3], 6), [0, 0])
        self.assertEqual(ts.twoSum([3, 3],6), [0, 1])
        self.assertEqual(ts.twoSum([-1, -2, -3, -4, -5], -8), [2, 4])
        self.assertEqual(ts.twoSum([1, -2, 3, 8, -5], 6), [1, 3])


if __name__ == "__main__":
    unittest.main()