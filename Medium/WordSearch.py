class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):

                if self.dfs(board, word, i, j, visited):
                    return True
        return False


    def dfs(self, board, word, i, j, visited):

        if len(word) == 0:
            return True
        elif i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or visited[i][j] == True or board[i][j] != word[0]:
            return False
        else:
            visited[i][j] = True

            if self.dfs(board, word[1:], i - 1, j, visited) or self.dfs(board, word[1:], i, j - 1, visited) or self.dfs(board, word[1:], i + 1, j, visited) or self.dfs(board, word[1:], i, j + 1, visited):
                return True
            else:

                # backtracking
                visited[i][j] = False
                return False
