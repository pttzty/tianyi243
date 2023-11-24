'''
LC 55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array 
represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
             Its maximum jump length is 0, which makes it impossible to reach the last index.
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        right_most_idx = 0
        target_idx = len(nums) - 1
        for i in range(len(nums)):
            tmp_new_idx = i + nums[i]
            if tmp_new_idx > right_most_idx:
                right_most_idx = tmp_new_idx
            if right_most_idx >= target_idx:
                return True
            
            if i == right_most_idx:
                return False
        return False


if __name__ == "__main__":
    S = Solution()
    nums = [2,3,1,1,4]
    print(S.canJump(nums))
    nums = [3,2,1,0,4]
    print(S.canJump(nums))
    nums = [2,0,1]
    print(S.canJump(nums))