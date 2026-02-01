"""
Problem: https://leetcode.com/problems/subarray-sum-equals-k/
Pattern: Prefix Sum + Hash Map
Time: O(n)
Space: O(n)
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Counts the number of continuous subarrays whose sum equals k.

        This function uses the prefix sum technique combined with a hash map
        to achieve an O(n) time complexity. For each index, it checks whether
        there exists a previous prefix sum such that the difference between
        the current prefix sum and that previous sum equals k.

        Key Insight:
            If prefix_sum[j] - prefix_sum[i] = k,
            then the subarray nums[i+1 : j+1] sums to k.

        Approach:
        - Maintain a running prefix sum.
        - Use a dictionary to store the frequency of prefix sums encountered.
        - For each element, check how many times (current_sum - k) has appeared.
        - Accumulate the count of valid subarrays.

        This approach works for arrays containing negative numbers,
        unlike the sliding window technique.

        Time Complexity:
            O(n), where n is the length of nums.

        Space Complexity:
            O(n), for storing prefix sums in the hash map.

        Args:
            nums (List[int]): List of integers (can include negative numbers).
            k (int): Target sum for subarrays.

        Returns:
            int: Number of continuous subarrays whose sum equals k.
        """
        count = 0

        n = len(nums)
        sums = 0

        d = {}
        d[0] = 1

        for i in range(n):
            sums += nums[i]
            count += d.get(sums-k, 0)
            d[sums] = d.get(sums, 0) + 1
                          
        return count

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1,1,1], 2, 2),
        ([1,2,3], 3, 2),
        ([1,-1,0], 0, 3)
    ]

    for nums, k, expected in test_cases:
        result = sol.subarraySum(nums, k)
        print(result == expected)