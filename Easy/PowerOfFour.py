class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 4:
            n = float(n) / 4
        if n == 1:
            return True
        else:
            return False
