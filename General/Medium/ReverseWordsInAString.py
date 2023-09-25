class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()[::-1]
        s = ' '.join(lst)
        return s