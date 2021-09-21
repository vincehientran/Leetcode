class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ret = 0
        power = 0
        for i in range(len(columnTitle) - 1, -1, -1):

            letterValue = ord(columnTitle[i])-ord('A')+1
            ret += (26**power) * letterValue
            power += 1
            

        return ret
