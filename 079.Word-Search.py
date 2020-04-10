"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""


class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(i,j,board, word, 0): return True
        return False

    def helper(self, i, j, board, word, wordIndex):

        if wordIndex == len(word): return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[wordIndex]:
            return False

        board[i][j] = "#"

        found = self.helper(i-1,j,board,word, wordIndex+1) or self.helper(i+1,j,board,word, wordIndex+1) or self.helper(i,j-1,board,word, wordIndex+1) or self.helper(i,j+1,board,word, wordIndex+1)

        board[i][j] = word[wordIndex]

        return found

if __name__ == "__main__":
    board =[
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = "ABCCED"
    result = Solution().exist(board, word)
    print(result)
