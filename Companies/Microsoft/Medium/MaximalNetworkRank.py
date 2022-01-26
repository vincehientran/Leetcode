import collections
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        vertices = collections.OrderedDict()
        
        for road in roads:
            start, end = road
            if start in vertices:
                vertices[start].append(tuple(road))
            else:
                vertices[start] = [tuple(road)]
                
            if end in vertices:
                vertices[end].append(tuple(road))
            else:
                vertices[end] = [tuple(road)]
                
        maxRank = 0
        
        for i in range(n-1):
            for j in range(i+1,n):
                vertex1 = []
                vertex2 = []
                if i in vertices:
                    vertex1 = vertices[i]
                if j in vertices:
                    vertex2 = vertices[j]
                maxRank = max(len(set(vertex1 + vertex2)), maxRank)
        
        return maxRank
                