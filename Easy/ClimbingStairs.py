class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        lst = [1,2]

        for i in range(n-2):
            lst.append(lst[-2] + lst[-1])

        return lst[-1]   
