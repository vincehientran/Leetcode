class Solution(object):
    def wallsAndGates(self, rooms):
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i,j))

        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                i,j = queue.pop(0)

                if (i > 0 and rooms[i-1][j] > count):
                    queue.append((i-1,j))
                    rooms[i-1][j] = count
                if (j > 0 and rooms[i][j-1] > count):
                    queue.append((i,j-1))
                    rooms[i][j-1] = count
                if (i < len(rooms)-1 and rooms[i+1][j] > count):
                    queue.append((i+1,j))
                    rooms[i+1][j] = count
                if (j < len(rooms[0])-1 and rooms[i][j+1] > count):
                    queue.append((i,j+1))
                    rooms[i][j+1] = count

sol = Solution()
rooms = [[0,2147483647,-1,2147483647,2147483647,-1,-1,0,0,-1,2147483647,2147483647,0,-1,2147483647,2147483647,2147483647,2147483647,0,2147483647,0,-1,-1,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,-1,0,0,-1,0,0,0,2147483647,0,2147483647,-1,-1,0,-1,0,0,0,2147483647],[2147483647,0,-1,2147483647,0,-1,-1,-1,-1,0,0,2147483647,2147483647,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,0,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,0,2147483647,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,2147483647,0,-1,2147483647,-1,-1,-1,0,2147483647]]
sol.wallsAndGates(rooms)
print(rooms)
