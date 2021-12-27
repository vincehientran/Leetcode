class Solution(object):
    def __init__(self):
        # max nodes is 1000 so we want a max index of 1000
        self.parent = [i for i in range(1001)]

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        for edge in edges:
            if self.find(edge[0]) == self.find(edge[1]) or not self.union(edge[0], edge[1]):
                return edge

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            # node2 is in the same set as node1
            return False
        else:
            self.parent[parent2] = parent1
            return True
