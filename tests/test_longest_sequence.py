import unittest
from solutions import LongestConsecutiveSequence

class TestLongestConsecutiveSequence(unittest.TestCase):

    def test_longestConsecutive(self):
        lcs = LongestConsecutiveSequence()

        self.assertEqual(lcs.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(lcs.longestConsecutive([]), 0)
        self.assertEqual(lcs.longestConsecutive([1]), 1)
        self.assertEqual(lcs.longestConsecutive([10, 5, 12, 15]), 1)
        self.assertEqual(lcs.longestConsecutive([7, 7, 7]), 1)


if __name__ == "__main__":
    unittest.main()