class Solution(object):
    def getRow(self, rowIndex):

        # create the pascal array
        # 1 0 0 0
        # 1 1 0 0
        # 1 2 1 0
        # 1 3 3 1
        array = []
        firstRow = []
        firstRow.append(1)
        for i in range(rowIndex):
            firstRow.append(0)
        array.append(firstRow)

        for i in range(1, rowIndex+1):
            # the first number in any row is 1
            newRow = [1]

            for j in range(1,rowIndex+1):
                # each item in the new row will be the sum of the
                # item on the top left and top of it
                newRow.append(array[i-1][j-1] + array[i-1][j])

            array.append(newRow)

        return array[rowIndex]
