'''
LC 347
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

## Bucket sort O(n)
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = defaultdict(int)
        n = len(nums)
        for t in nums:
            counter[t] += 1
        bucket = [[] for _ in range(n+1)]
        for t in counter:
            bucket[counter[t]].append(t)
        
        res = []
        for i in range(n,-1,-1):
            if not bucket[i]:
                continue
            else:
                res = res + bucket[i]
            if len(res) >= k:
                break
        return res

S = Solution()
print(S.topKFrequent([1,1,1,2,2,3],2))
print(S.topKFrequent([1,1,1],1))
print(S.topKFrequent([1],1))
print(S.topKFrequent([2,2,1,1,1,11,1],1))