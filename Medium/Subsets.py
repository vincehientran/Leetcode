class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums,[], result)
        return result

    def dfs(self, nums, path, result):
        result.append(path)

        for i in range(len(nums)):
            newPath = path + [nums[i]]
            self.dfs(nums[i+1:], newPath, result)
