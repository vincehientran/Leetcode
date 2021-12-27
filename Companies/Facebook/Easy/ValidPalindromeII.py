class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if (s == s[::-1]):
            return True
        else:
            l = 0
            r = len(s) -1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    removeLeft = s[l+1:r+1]
                    removeRight = s[l:r]
                    if removeLeft == removeLeft[::-1] or removeRight == removeRight[::-1]:
                        return True
                    else:
                        return False