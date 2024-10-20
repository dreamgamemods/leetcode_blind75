from typing import List

class LongestSubstringWithoutRepeatingChars:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        last_index = {}
        start = 0

        for end, char in enumerate(s):
            if char in last_index:
                start = max(start, last_index[char])
            max_length = max(max_length, end-start+1)
            last_index[char] = end+1

        return max_length
