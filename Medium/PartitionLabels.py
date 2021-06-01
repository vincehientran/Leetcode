class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        rightmostIdx = {char:idx for idx, char in enumerate(s)}

        startPatternIdx = 0
        currentPointer = 0

        result = []

        for i in range(len(s)):

            currentPointer = max(currentPointer, rightmostIdx[s[i]])

            if i == currentPointer:
                result.append(len(s[startPatternIdx:currentPointer + 1]))
                startPatternIdx = currentPointer + 1

        return result
