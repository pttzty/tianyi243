'''
LC 45. Jump Game II
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
'''

'''
Thoughts: 
1. Build a graph that connects i to j where i <= j - k, k is the step length
2. Run a BFS
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # First build graph
        graph = {}
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 0

        for i in range(len(nums) - 1):
            if nums[i] > 0:
                graph[i] = [i + k for k in range(1, nums[i] + 1)]
        
        # run BFS
        queue = []
        queue.append((0,0))
        d = 0
        visited = set()
        while queue:
            i,d = queue.pop(0)
            if i == len(nums) - 1:
                return d
            if i not in graph:
                continue
            for element in graph[i]:
                if element not in visited:
                    queue.append((element,d+1))
                    visited.add(element)
        return -1

if __name__ == "__main__":
    S = Solution()
    nums = [2,3,1,1,4]
    print(S.jump(nums))
    nums = [2,3,0,1,4]
    print(S.jump(nums))
    nums = [2,5,1,1,1,1,1,1,4]
    print(S.jump(nums))
    nums = [5,8,1,8,9,8,7,1,7,5,8,6,5,4,7,3,9,9,0,6,6,3,4,8,
             0,5,8,9,5,3,7,2,1,8,2,3,8,9,4,7,6,2,5,2,8,2,7,9,3,7,6,9,2,0,8,2,7,8,4,
             4,1,1,6,4,1,0,7,2,0,3,9,8,7,7,0,6,9,9,7,3,6,3,4,8,6,4,3,3,2,7,8,5,8,6,0]
    print(S.jump(nums))
