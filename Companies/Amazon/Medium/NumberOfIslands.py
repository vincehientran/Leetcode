class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        countIsland = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    countIsland += 1
                    self.dfs(grid, i, j)
                    
        return countIsland
        
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or j >= len(grid[0]) or i >= len(grid) or grid[i][j] == '0':
            return
        else:
            grid[i][j] = '0'
            self.dfs(grid,i-1,j)
            self.dfs(grid,i,j-1)
            self.dfs(grid,i+1,j)
            self.dfs(grid,i,j+1)