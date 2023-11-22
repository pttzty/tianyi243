'''
LC 1743 Restore the Array From Adjacent Pairs

There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
Return the original array nums. If there are multiple solutions, return any of them.
'''

'''
Thoughts: Since all elements are unique, this is essentially a graph.
Lot of items have a degree of 2 except for only two elements should have degrees of 1, they should be put in the first (or last)
'''


class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        for i, j in adjacentPairs:
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)
            if j not in graph:
                graph[j] = [i]
            else:
                graph[j].append(i)
        # Initialize queue with degree one elements
        queue = [x for x in graph if len(graph[x]) == 1]

        # pick one element would be good
        queue = [queue[0]]
        result = []
        visited = set()
        while queue:
            element = queue.pop(0)
            result.append(element)
            visited.add(element)
            for k in graph[element]:
                if k not in visited:
                    queue.append(k)
        return result

if __name__ == "__main__":
    S = Solution()
    adjacentPairs = [[2,1],[3,4],[3,2]]
    print(S.restoreArray(adjacentPairs))
    adjacentPairs = [[4,-2],[1,4],[-3,1]]
    print(S.restoreArray(adjacentPairs))
    adjacentPairs = [[100000,-100000]]
    print(S.restoreArray(adjacentPairs))