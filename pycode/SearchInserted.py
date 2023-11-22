'''
LC 35 Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

import pytest

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1
        return left_idx
    
S = Solution()
print(S.searchInsert([1,3,5,6], 5))
print(S.searchInsert([1,3,5,6], 2))