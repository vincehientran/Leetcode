class Solution(object):
    def permute(self, nums):
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, path, result):
        if len(nums) == 0:
            result.append(path)
        else:
            # pick a number out of nums and append it to path
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], result)
