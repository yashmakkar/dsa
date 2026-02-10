"""
Problem: https://leetcode.com/problems/group-anagrams/
Pattern: Hash Map + Frequency Array
Time: O(n · k)
Space: O(n · k)
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups strings that are anagrams of each other.

        Each string is represented using a fixed-size frequency array
        of 26 lowercase letters. This frequency array is converted to
        a tuple and used as a hash map key.

        Strings with identical character frequencies belong to the same group.

        Time Complexity:
            O(n · k), where n is the number of strings and k is the average length.

        Space Complexity:
            O(n · k), for storing frequency keys and grouped strings.

        Args:
            strs (List[str]): List of input strings.

        Returns:
            List[List[str]]: Grouped anagrams.
        """
        groups = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            groups[tuple(freq)].append(s)

        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"], ["tan","nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ]

    for strs, _ in test_cases:
        print(sol.groupAnagrams(strs))
