"""
Problem: https://leetcode.com/problems/two-sum/
Pattern: Hash Map (One-pass lookup)
Time: O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Iterate through the array while storing previously seen numbers
        and their indices in a hash map.

        For each number:
        - Compute the complement (target - current number)
        - If complement exists in the map, return indices
        - Otherwise, store the current number with its index
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        # As per problem statement, exactly one solution always exists
        return []


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]

    for nums, target, expected in test_cases:
        result = sol.twoSum(nums, target)
        print(result == expected)
