import unittest
from solutions import LongestSubstringWithoutRepeatingChars

class TestLongestSubstringWithoutRepeatingChars(unittest.TestCase):

    def test_longestConsecutive(self):
        lswrc = LongestSubstringWithoutRepeatingChars()

        self.assertEqual(lswrc.lengthOfLongestSubstring("abcdef"), 6)
        self.assertEqual(lswrc.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lswrc.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lswrc.lengthOfLongestSubstring(""), 0)
        self.assertEqual(lswrc.lengthOfLongestSubstring("a"), 1)
        self.assertEqual(lswrc.lengthOfLongestSubstring("abc@!def@!"), 8)
        self.assertEqual(lswrc.lengthOfLongestSubstring("一二三二一"), 3)

if __name__ == "__main__":
    unittest.main()