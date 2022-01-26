class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        
        numRows = len(matrix)
        numCols = len(matrix[0])
        
        lenOfResult = numRows * numCols
        
        rightLimit = numCols
        bottomLimit = numRows
        leftLimit = 0
        topLimit = 1
        
        finished = False
        
        while not finished:
            # go right
            for i in range(leftLimit, rightLimit):
                ret.append(matrix[topLimit - 1][i])
                if len(ret) == lenOfResult:
                    finished = True
                    break
                
            # go down
            if not finished:
                for i in range(topLimit, bottomLimit):
                    ret.append(matrix[i][rightLimit - 1])
                    if len(ret) == lenOfResult:
                        finished = True
                        break
                
            # go left
            if not finished:
                for i in range(rightLimit - 2, leftLimit - 1, -1):
                    ret.append(matrix[bottomLimit - 1][i])
                    if len(ret) == lenOfResult:
                        finished = True
                        break
                
            # go up
            if not finished:
                for i in range(bottomLimit - 2, topLimit - 1, -1):
                    ret.append(matrix[i][leftLimit])
                    if len(ret) == lenOfResult:
                        finished = True
                        break
                
            rightLimit -= 1
            bottomLimit -= 1
            leftLimit += 1
            topLimit += 1
            
        return ret
        