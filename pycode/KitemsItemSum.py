'''
LC 2600
There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.

You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.

The bag initially contains:

numOnes items with 1s written on them.
numZeroes items with 0s written on them.
numNegOnes items with -1s written on them.
We want to pick exactly k items among the available items. Return the maximum possible sum of numbers written on the items.

'''

class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        if numOnes >=k:
            return k
        elif numOnes + numZeros >= k:
            return numOnes
        elif numOnes + numZeros + numNegOnes >= k:
            return numOnes - (k - numOnes - numZeros)
        else:
            return numOnes - numNegOnes

S = Solution()
print(S.kItemsWithMaximumSum(4, 2, 3, 1))