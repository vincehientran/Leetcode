class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        # up=0, left=1, down=2, right=3
        facing = 0
        x, y = 0, 0
        
        for instruction in instructions:
            # keeps track of direction
            if instruction == 'L':
                if facing == 0:
                    facing = 3
                else:
                    facing -= 1
            elif instruction == 'R':
                if facing == 3:
                    facing = 0
                else:
                    facing += 1
                    
            # keeps track of location
            else:
                if facing == 0:
                    y += 1
                elif facing == 1:
                    x += 1
                elif facing == 2:
                    y -= 1
                else:
                    x -= 1
            
        # circle it goes back to (0, 0) or if its not facing upwards 
        if facing != 0 or (x == 0 and y == 0):
            return True