class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.' and self.isValidCell(board, board[i][j], i, j):
                    return False
        return True

    def isValidCell(self, board, num, i, j):
        return not (self.isValidRow(board, board[i][j], i, j) and self.isValidCol(board, board[i][j], i, j) and self.isValidBox(board, board[i][j], i, j))

    def isValidRow(self, board, num, row, col):
        return not (num in board[row][:col] + board[row][col+1:])

    def isValidCol(self, board, num, row, col):
        for i in range(len(board)):
            if row != i and board[i][col] == num:
                return False
        return True

    def isValidBox(self, board, num, row, col):
        for i in range(row - (row % 3), row - (row % 3) + 3):
            for j in range(col - (col % 3), col - (col % 3) + 3):
                if row != i and col != j and board[i][j] == num:
                    return False
        return True
