class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxArea = max(self.dfs(grid, i, j), maxArea)

        return maxArea

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0

        totalArea = 1
        grid[i][j] = 0

        totalArea += self.dfs(grid, i - 1, j)
        totalArea += self.dfs(grid, i, j - 1)
        totalArea += self.dfs(grid, i + 1, j)
        totalArea += self.dfs(grid, i, j + 1)

        return totalArea
