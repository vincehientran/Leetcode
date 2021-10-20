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
                        # cancel both asteroids
                        stop = True
                        stack.pop()
                        break
                    elif stack[-1] > -asteroid:
                        # cancel the negative asteroid
                        stop = True
                        break
                    else:
                        # cancel the positive asteroid
                        stack.pop()
                        continue
                        
                if not stop:
                    # add the negative asteroid if it was not cancelled yet
                    stack.append(asteroid)
                    
                    
        return stack