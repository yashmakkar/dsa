"""
Problem: https://leetcode.com/problems/longest-consecutive-sequence/
Pattern: Hash Set + Sequence Expansion
Time: O(n)
Space: O(n)
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence.

        This solution uses a hash set for constant-time lookups.
        It only starts counting when a number is the beginning of
        a sequence (i.e., num - 1 is not present in the set).

        The sequence is expanded forward until consecutive numbers
        no longer exist.

        Time Complexity:
            O(n), where n is the number of elements in nums.

        Space Complexity:
            O(n), for storing elements in the set.

        Args:
            nums (List[int]): List of unsorted integers.

        Returns:
            int: Length of the longest consecutive sequence.
        """
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:   # start of sequence
                curr = num
                length = 1

                while curr + 1 in num_set:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([], 0)
    ]

    for nums, expected in test_cases:
        print(sol.longestConsecutive(nums) == expected)