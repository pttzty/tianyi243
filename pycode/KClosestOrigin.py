'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''

import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        h = []
        for i in range(len(points)):
            d = - 1 * (points[i][0] ** 2 + points[i][1] ** 2)
            if len(h) >= k:
                d1, p1 = heapq.heappop(h)
                if d1 < d:
                    heapq.heappush(h, (d, points[i]))
                else:
                    heapq.heappush(h, (d1, p1))
            else:
                heapq.heappush(h,(d, points[i]))
        
        output = []
        for i in range(k):
            pt = h[i][1]
            output.append(pt)
        return output

S = Solution()

print(S.kClosest([[1,3],[-2,2]],1))

print(S.kClosest([[3,3],[5,-1],[-2,4]],2))