'''
LC 130 Surrounded Regions
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]

'''


'''
Thoughts: Start from O's in Matrix Boundaries and then perform BFS/DFS to them
'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # Initialize BFS Queue
        queue = set()
        for i in set([0,m-1]):
            for j in range(n):
                if board[i][j] == 'O':
                    queue.add((i,j))
        
        for j in set([0, n-1]):
            for i in range(m):
                if board[i][j] == 'O':
                    queue.add((i,j))
        print(queue)

        queue = list(queue)
        
        visited = set(queue)
        while queue:
            i,j = queue.pop(0)
            u = (i-1,j)
            d = (i+1,j)
            r = (i,j+1)
            l = (i,j-1)
            for x,y in (u,d,r,l):
                if 0<=x<m and 0<=y<n and (x,y) not in visited:
                    if board[x][y] == 'O':
                        queue.append((x,y))
                        visited.add((x,y))
                    else:
                        visited.add((x,y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
        return board


if __name__ == "__main__":
    S = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(S.solve(board))
    board = [["X"]]
    print(S.solve(board))
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","X","X"],["X","X","O","X"],["X","O","O","X"]]
    print(S.solve(board))
    board = [["X","X","X"],["X","O","X"],["X","X","X"]]
    print(S.solve(board))