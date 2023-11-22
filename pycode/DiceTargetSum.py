'''
LC 1155 Number of Dice Rolls With Target Sum
You have n dice, and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice,
so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.
'''

class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """

        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, target+1):
                for l in range(1, k+1):
                    if j >= l:
                        dp[i][j] += dp[i-1][j-l]
        return dp[n][target] % (10**9 + 7)

S = Solution()
print(S.numRollsToTarget(1, 6, 3))
print(S.numRollsToTarget(2, 6, 7))
print(S.numRollsToTarget(30, 30, 500))