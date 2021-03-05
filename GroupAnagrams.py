class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for string in strs:
            letters = sorted(string)
            letters = tuple(letters)
            if letters not in d:
                d[letters] = [string]
            else:
                d[letters].append(string)

        ret = []
        for _,v in d.items():
            ret.append(v)

        return ret
