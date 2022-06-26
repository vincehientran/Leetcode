class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in range(len(board)):
            for j in range(len(board[i])):

                if self.dfs(board, word, i, j):
                    return True

        return False


    def dfs(self, board, word, i, j):
        
        if len(word) == 0:
            return True
        elif i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] != word[0]:
            return False
        else:
            originalValue = board[i][j]
            board[i][j] = ''

            if self.dfs(board, word[1:], i - 1, j) or self.dfs(board, word[1:], i, j - 1) or self.dfs(board, word[1:], i + 1, j) or self.dfs(board, word[1:], i, j + 1):
                return True
            else:
                # backtracking
                board[i][j] = originalValue
                return False
