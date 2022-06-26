class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l = k
        r = len(cardPoints)

        largest = sum(cardPoints[:l])
        prev_window_sum = largest

        while l != 0:
            l -= 1
            r -= 1

            window_sum = prev_window_sum - cardPoints[l] + cardPoints[r]
            prev_window_sum = window_sum


            largest = max(window_sum, largest)

        return largest

        
