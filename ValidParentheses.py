class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # keeps track of the opening parens
        stack = []

        for paren in s:

            if paren == '(' or paren == '[' or paren == '{':
                stack.append(paren)
            else:
                if len(stack) == 0:
                    return False

                prevOpen = stack.pop(len(stack)-1)

                if paren == ')' and not prevOpen == '(':
                    return False
                elif paren == ']' and not prevOpen == '[':
                    return False
                elif paren == '}' and not prevOpen == '{':
                    return False


        if len(stack) > 0:
            return False

        return True
