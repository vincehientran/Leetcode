class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for i in range(num + 1):
            countOfOnes = 0
            number = i
            while number != 0:
                countOfOnes += number & 1
                number //= 2
            result.append(countOfOnes)

        return result
