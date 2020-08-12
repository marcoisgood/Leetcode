class Solution:
    def candyCrush(self, board):
        while True:
            crush = set()
            for i in range(len(board)):
                for j in range(len(board[0]):
                        if j > 1 and board[i][j] == board[i][j-1] == board[i][j-2]:
                                crush |= {(i,j),(i,j-1),(i,j-2)}

                        if i > 1 and board[i][j] == board[i-1][j] == board[i-2][j]:
                                crush |= {(i,j),(i-1, j),(i-2, j)}

            if not crush: break

            for i, j in crush:
                    board[i][j] = 0


            for j in range(len(board[0])):
                    idx = len(board) - 1
                    for i in reversed(range(len(board)):
                            if board[i][j] > 0:
                                board[idx][j] = board[i][j]
                                idx -= 1

                    for i in range(idx+1):
                            board[i][j] = 0

            return board    


if __name__ == "__main__":

    board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

    res = Solution().candyCrush(board)
    print(res)
