class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        lexiHash = {}
        for i in range(len(order)):
            lexiHash[order[i]] = i

        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]

            # flag: True if first or second is a substring of the other
            equal = True

            for j in range(min(len(first),len(second))):
                # only check lexi value if the letters are different
                if first[j] != second[j]:
                    if lexiHash[first[j]] > lexiHash[second[j]]:

                        return False
                    equal = False
                    break

            # not in order of the first word is longer than the second word
            # if they start with the same letters
            if equal and len(first) > len(second):
                return False

        return True
