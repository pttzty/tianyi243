'''
LC 373. Find K Pairs with Smallest Sums
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
'''

'''
Thoughts:
1. We can use a heap to store the current smallest k pairs
2. We keep two pointers, one for nums1, one for nums2, and we keep adding the next smallest pair to the heap
3. We need to be careful about the duplicate pairs, we need to skip them
4. We need to be careful about the boundary conditions
5. once we have k pairs, we can stop
'''
import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        '''
        Time Complexity: O(klogk)
        Space Complexity: O(k)
        if k>n, then O(nlogn)
        '''
        if not nums1 or not nums2:
            return []
        heap = []
        heapq.heapify(heap)
        result = []
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited = set()
        visited.add((0, 0))
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        return result
    
if __name__ == "__main__":
    S = Solution()
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    print(S.kSmallestPairs(nums1, nums2, k))
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    print(S.kSmallestPairs(nums1, nums2, k))