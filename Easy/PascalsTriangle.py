class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        holder = [[1 if i == 0 else 0 for i in range(numRows)] for _ in range(numRows)]

        for row in range(1, numRows):
            for col in range(1, numRows):
                val = holder[row - 1][col -1] + holder[row - 1][col]
                holder[row][col] = val

        ret = []

        for i in range(numRows):
            ret.append(holder[i][:i+1])

        return ret
