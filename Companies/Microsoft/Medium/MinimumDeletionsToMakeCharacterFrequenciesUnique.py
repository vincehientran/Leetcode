import collections
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.OrderedDict()
        
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        found = set()
        
        ret = 0
        
        for _, count in d.items():
            while count > 0 and count in found:
                ret += 1
                count -= 1
            found.add(count)
        
        return ret
            
        