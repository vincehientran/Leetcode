class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        retList = s.split()[::-1]
        
        retStr = ''
        
        for word in retList:
            retStr += word + ' '
            
        return retStr[:-1]