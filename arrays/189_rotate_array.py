"""
Problem: https://leetcode.com/problems/rotate-array/
Pattern: Array Reversal
Time: O(n)
Space: O(1)
"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.

        This solution uses the array reversal technique:
        1. Reverse the entire array
        2. Reverse the first k elements
        3. Reverse the remaining n - k elements

        Time Complexity:
            O(n), where n is the length of nums.

        Space Complexity:
            O(1), constant extra space.

        Args:
            nums (List[int]): Array of integers to rotate.
            k (int): Number of steps to rotate the array.
        """
        n = len(nums)
        k %= n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
        ([1], 0, [1])
    ]

    for nums, k, expected in test_cases:
        sol.rotate(nums, k)
        print(nums == expected)
