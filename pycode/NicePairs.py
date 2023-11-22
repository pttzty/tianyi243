'''
LC1814: Count Nice Pairs in an Array
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. 
For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.
'''

class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Basic idea: create a hash map of nums[i] - rev(nums[i]) and iteratively count the qualifying js
        so the key is only relevant to i.
        '''
        diff_map = {}
        count = 0
        for i in range(len(nums)):
            reverse = int(str(nums[i])[::-1])
            diff = nums[i] - reverse
            if diff in diff_map:
                count += diff_map[diff]
                diff_map[diff] += 1
            else:
                diff_map[diff] = 1
        return count % (10**9 + 7)

if __name__ == "__main__":
    nums = [42,11,1,97]
    print(Solution().countNicePairs(nums))
    nums = [13,10,35,24,76]
    print(Solution().countNicePairs(nums))
        