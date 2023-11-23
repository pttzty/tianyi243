'''
LC 1492. The kth Factor of n
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
'''

import math

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # the factor is at most SQRT(N) except for itself
        max_factor = int(math.sqrt(n))
        factors = []
        reverse_factors = []
        for e in range(1, max_factor + 1):
            if n % e == 0:
                factors.append(e)
                if e != int(n/e):
                    reverse_factors.append(int(n/e))
        factors = factors + reverse_factors[::-1]
        if k <= len(factors):
            return factors[k-1]
        return -1

if __name__ == "__main__":
    S = Solution()
    print(S.kthFactor(12,3))
    print(S.kthFactor(7,2))
    print(S.kthFactor(4,4))
    print(S.kthFactor(24,6))