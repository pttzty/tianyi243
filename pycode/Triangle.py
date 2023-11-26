'''
LC 120. Triangle
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, 
if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
    2
   3 4
  6 5 7
 4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10

'''

'''
First Solution:
O(n ** 2) extra space DP, O(n ** 2) time complexity, n is the number of elements
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[0 for _ in range(x)] for x in range(1, n+1)]
        # Intialize DP matrix
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(0,i+1):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1],dp[i-1][j])
        return min(dp[n-1])




'''
Thought for O(n) extra space, we basically need effective pruning, since every step can only move to i, i+1 in the future step
while the truth is after we pass a layer, that is no longer relevant to us, we only need to maintain two layers
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        # Intialize DP matrix
        last_layer = triangle[0]

        for i in range(1,n):
            curr_layer = [99999 for _ in range(i+1)]
            for j in range(0,i+1):
                if j == 0:
                    curr_layer[j] = last_layer[j] + triangle[i][j]
                elif j == i:
                    curr_layer[j] = last_layer[j-1] + triangle[i][j]
                else:
                    curr_layer[j] = triangle[i][j] + min(last_layer[j-1],last_layer[j])
            last_layer = curr_layer
        return min(curr_layer)


if __name__ == "__main__":
    S = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(S.minimumTotal(triangle))
    triangle = [[-10]]
    print(S.minimumTotal(triangle))
    triangle = [[2],[3,4],[-10,5,7],[4,1,8,3]]
    print(S.minimumTotal(triangle))