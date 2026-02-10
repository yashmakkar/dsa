"""
Problem: https://leetcode.com/problems/valid-anagram/
Pattern: Frequency Array / Counting
Time: O(n)
Space: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks whether two strings are anagrams of each other.

        This function uses a fixed-size frequency array for lowercase
        English letters. It increments counts for characters in the
        first string and decrements for the second string in a single pass.

        If all frequency values are zero at the end, the strings are anagrams.

        Time Complexity:
            O(n), where n is the length of the strings.

        Space Complexity:
            O(1), since the array size is fixed to 26.

        Args:
            s (str): First string.
            t (str): Second string.

        Returns:
            bool: True if s and t are anagrams, otherwise False.
        """
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for cs, ct in zip(s, t):
            freq[ord(cs) - ord("a")] += 1
            freq[ord(ct) - ord("a")] -= 1

        return all(count == 0 for count in freq)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "a", True)
    ]

    for s, t, expected in test_cases:
        print(sol.isAnagram(s, t) == expected)
