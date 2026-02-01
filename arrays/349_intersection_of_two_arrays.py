"""
Problem: https://leetcode.com/problems/intersection-of-two-arrays/
Pattern: Hash Set
Time: O(n + m)
Space: O(n + m)
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Returns the intersection of two arrays.

        This function uses hash sets to remove duplicates and enable
        constant-time lookups. The intersection is computed by iterating
        over the smaller set to minimize membership checks.

        Approach:
        - Convert both input lists into sets to remove duplicates.
        - Iterate over the smaller set and check presence in the larger set.
        - Collect common elements in a result list.

        Time Complexity:
            O(n + m), where n and m are the lengths of nums1 and nums2.

        Space Complexity:
            O(n + m), for storing elements in sets.

        Args:
            nums1 (List[int]): First list of integers.
            nums2 (List[int]): Second list of integers.

        Returns:
            List[int]: List of unique elements present in both arrays.
        """
        inter = []

        nums1 = set(nums1)
        nums2 = set(nums2)

        if len(nums1) <= len(nums2):
            for num in nums1:
                if num in nums2:
                    inter.append(num)
        else:
            for num in nums2:
                if num in nums1:
                    inter.append(num)

        return inter


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 2, 1], [2, 2], [2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
        ([1], [2], [])
    ]

    for nums1, nums2, expected in test_cases:
        result = sol.intersection(nums1, nums2)
        print(sorted(result) == sorted(expected))
