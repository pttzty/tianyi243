'''
LC 1762
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
'''
class Solution(object):
    def OceanView(self, heights):
        if not heights:
            return []
        output = []
        n = len(heights)
        curr_max = float('-inf')
        for i in range(n-1,-1,-1):
            if heights[i] > curr_max:
                output.append(i)
                curr_max = heights[i]
        output.reverse()
        return output

S = Solution()
print(S.OceanView([4,2,3,1]))
print(S.OceanView([1,3,2,4]))
print(S.OceanView([2,2,2,2]))