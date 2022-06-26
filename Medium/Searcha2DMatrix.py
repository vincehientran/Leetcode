class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        current = (0,0)

        # traverse downwards until the target is less than the current
        # then traverse sidewards until the target is found or else return False
        return self.traverseDown(matrix, target, current)

    def traverseDown(self, matrix, target, current):
        if matrix[current[0]][current[1]] == target:
            return True
        else:
            if current[0] + 1 < len(matrix) and matrix[current[0] + 1][current[1]] <= target:
                current = (current[0] + 1, current[1])
                return self.traverseDown(matrix, target, current)
            elif current[1] + 1 < len(matrix[0]) and matrix[current[0]][current[1] + 1] <= target:
                current = (current[0], current[1] + 1)
                return self.traverseSide(matrix, target, current)
            else:
                return False

    def traverseSide(self, matrix, target, current):
        if matrix[current[0]][current[1]] == target:
            return True
        else:
            if current[1] + 1 < len(matrix[0]) and matrix[current[0]][current[1] + 1] <= target:
                current = (current[0], current[1] + 1)
                return self.traverseSide(matrix, target, current)
            else:
                return False
