class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        
        maxLength = 0
        candidates = ['']
        
        for x in arr:
            for candidate in candidates:
                concat = x + candidate
                
                # is concat a valid candidate
                if len(concat) == len(set(concat)):
                    candidates.append(concat)
                    maxLength = max(maxLength, len(concat))
        
        return maxLength