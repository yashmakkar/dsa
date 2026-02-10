"""
Problem: https://leetcode.com/problems/contains-duplicate/
Pattern: Hash Set
Time: O(n)
Space: O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks if the array contains any duplicate elements.

        This function uses a hash set to track unique values.
        If the size of the set is smaller than the list, at least
        one duplicate exists.

        Time Complexity:
            O(n), where n is the length of nums.

        Space Complexity:
            O(n), for storing elements in the set.

        Args:
            nums (List[int]): List of integers.

        Returns:
            bool: True if duplicates exist, otherwise False.
        """
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True)
    ]

    for nums, expected in test_cases:
        print(sol.containsDuplicate(nums) == expected)
