class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        d = {}
        d['2'] = 'abc'
        d['3'] = 'def'
        d['4'] = 'ghi'
        d['5'] = 'jkl'
        d['6'] = 'mno'
        d['7'] = 'pqrs'
        d['8'] = 'tuv'
        d['9'] = 'wxyz'

        result = []

        if len(digits) == 0:
            return []

        elif len(digits) == 1:

            for letter in d[digits]:
                result.append(letter)
            return result

        else:

            # for every letter that the first number can make,
            # pair it up with the combinations that all of the other numbers make
            for letter in d[digits[0]]:
                for prev in self.letterCombinations(digits[1:]):
                    result.append(letter + prev)

            return result
