class Solution(object):
    def rotate(self, matrix):

        # iterate through the positions that need to be rotate on the outer border
        # then move to the inner squares and repeat
        for i in range(len(matrix)//2):
            for j in range(i,len(matrix[0])-1-i):
                length = len(matrix)

                # variables holding the four values that needs to be swapped
                holder = matrix[i][j]
                left = matrix[length - 1 - j][i]
                right = matrix[j][length - 1 - i]
                across = matrix[length - 1 - i][length - 1 - j]

                # swapping
                matrix[i][j] = left
                matrix[length - 1 - j][i] = across
                matrix[j][length - 1 - i] = holder
                matrix[length - 1 - i][length - 1 - j] = right
