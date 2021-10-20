class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []
        for asteroid in asteroids:
            if asteroid > 0 or len(stack) == 0:
                stack.append(asteroid)
            else:
                stop = False
                while stack and stack[-1] > 0:
                    if stack[-1] == -asteroid:
                        stop = True
                        stack.pop()
                        break
                    elif stack[-1] > -asteroid:
                        stop = True
                        break
                    else:
                        stack.pop()
                        continue
                        
                if not stop:
                    stack.append(asteroid)
                    
                    
        return stack