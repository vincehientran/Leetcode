class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        
        if n % 2 == 0:
            for i in range(1,int(n/2)+1):
                ret.append(-i)
            for i in range(1,int(n/2)+1):
                ret.append(i)
        else:
            for i in range(1,int(n/2)+1):
                ret.append(-i)
            ret.append(0)
            for i in range(1,int(n/2)+1):
                ret.append(i)
        
        return ret