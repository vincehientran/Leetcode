class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [True if i == 0 else False for i in range(len(rooms))]
        stack = []

        for key in rooms[0]:
            stack.append(key)

        while stack:
            key = stack.pop()
            if visited[key]:
                continue
            else:
                visited[key] = True
                for key in rooms[key]:
                    stack.append(key)

        return all(visited)
