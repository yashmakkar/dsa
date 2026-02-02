"""
Problem: https://leetcode.com/problems/maximum-subarray/
Pattern: Kadane’s Algorithm (Dynamic Programming)
Time: O(n)
Space: O(1)
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray with the largest sum.

        This function implements Kadane’s Algorithm. At each index,
        it decides whether to extend the previous subarray or start
        a new subarray from the current element, while tracking the
        maximum sum encountered so far.

        Time Complexity:
            O(n), where n is the length of nums.

        Space Complexity:
            O(1), constant extra space.

        Args:
            nums (List[int]): List of integers (can include negative numbers).

        Returns:
            int: Maximum sum of any contiguous subarray.
        """
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23)
    ]

    for nums, expected in test_cases:
        result = sol.maxSubArray(nums)
        print(result == expected)
