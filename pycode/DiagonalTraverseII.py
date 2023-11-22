'''
LC 1424. Diagonal Traverse II
Given a 2D array nums, return all elements of nums in diagonal orders as shown in the below images.
'''

'''
Thoughts:
BFS and first visit down then right
Time Complexity O(N)
'''

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        queue = []
        queue.append((0,0))
        result = []
        visited = set()

        while queue:
            i,j = queue.pop(0)
            result.append(nums[i][j])
            d = (i+1, j)
            r = (i, j+1)
            dims = (d,r)
            for x,y in dims:
                if 0 <= x < n and 0<= y < (len(nums[x])):
                    if (x,y) not in visited:
                        visited.add((x,y))
                        queue.append((x,y))
        return result
    
if __name__ == "__main__":
    S = Solution()
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    print(S.findDiagonalOrder(nums))
    nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    print(S.findDiagonalOrder(nums))
