class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        sumSubList = sum(cardPoints[:k])
        left = k - 1
        right = len(cardPoints) - 1
        
        maximumScore = sumSubList
        
        for _ in range(k):
            sumSubList = sumSubList - cardPoints[left] + cardPoints[right]
            left -= 1
            right -= 1
            
            maximumScore = max(maximumScore, sumSubList)
        
        return maximumScore
            