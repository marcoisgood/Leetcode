"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""
import collections

class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        #DFS

        dfs_fun(rooms,row,col,d):
            dict = [(1,0),(-1,0),(0,1),(0,-1)]
            for i, j in dict:
                if 0 <= row+i < len(rooms) and 0 <= col+j < len(rooms) and rooms[row+i][col+j] > rooms[i][j]:
                    rooms[row+i][col+j] = d
                    dfs_fun(rooms,row+i,col+j, d+1)
            return rooms

        if not rooms: return []

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dfs_fun(rooms,i,j,1)

        #BFS
        if not rooms: return[]

        Q = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    Q.append((i,j))


        while Q:
            row, col = Q.popleft()
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0 <= row+i < len(rooms) and 0 <= col+j < len(rooms) and rooms[row+i][col+j] > rooms[i][j]:
                    rooms[row+i][col+j] = rooms[row][col] + 1
                    q.append((row+i, col+j))

if __name__ == "__main__":
    rooms = [[INF  -1  0  INF],[INF INF INF  -1],[INF  -1 INF  -1],[0  -1 INF INF]]

    res = Solution().wallsAndGates(rooms)

    print(res)
