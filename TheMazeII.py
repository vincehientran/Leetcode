class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        queue = []
        queue.append((start[0], start[1], 0))

        walls = [[-1 if maze[x][y] == 1 else float('inf') for y in range(len(maze[0]))] for x in range(len(maze))]

        while queue:

            row, col, distance = queue.pop(0)

            # travel upwards until it reaches a wall
            i = row
            d = distance
            while (i > 0 and walls[i-1][col] != -1):
                d += 1
                i -= 1
                walls[i][col] = d
            # return result if it reached the destination
            if (i == destination[0] and col == destination[1]):
                return walls[i][col]
            # append the new start point
            if (i != row):
                queue.append((i, col, d))

            # travel downwards until it reaches a wall
            i = row
            d = distance
            while (i < len(walls)-1 and walls[i+1][col] != -1):
                d += 1
                i += 1
                walls[i][col] = d
            if (i == destination[0] and col == destination[1]):
                return walls[i][col]
            if (i != row):
                queue.append((i, col, d))

            # travel leftwards until it reaches a wall
            j = col
            d = distance
            while (j > 0 and walls[row][j-1] != -1):
                d += 1
                j -= 1
                walls[row][j] = d
            if (row == destination[0] and j == destination[1]):
                return walls[row][j]
            if (j != col):
                queue.append((row, j, d))

            # travel rightwards until it reaches a wall
            j = col
            d = distance
            while (j < len(walls[0])-1 and walls[row][j+1] != -1):
                d += 1
                j += 1
                walls[row][j] = d
            if (row == destination[0] and j == destination[1]):
                return walls[row][j]
            if (j != col):
                queue.append((row, j, d))

        return -1

s = Solution()
maze = [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
start = [0,0]
destination = [8,6]
result = s.shortestDistance(maze, start, destination)

print(result)
