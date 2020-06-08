"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution(object):
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count+=1
        return count
    def dfs(self, grid, m, n):
        if 0 <= m < len(grid) and 0 <= n < len(grid[0]) and grid[m][n] == '1':
            grid[m][n] ='#'
            self.dfs(grid, m, n-1)
            self.dfs(grid, m+1, n)
            self.dfs(grid, m-1, n)
            self.dfs(grid, m, n+1)
        return

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    result = Solution().numIslands(grid)
    print(result)
