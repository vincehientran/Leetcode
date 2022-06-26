class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        result = []
        nums = [i for i in range(1, n + 1)]
        self.dfs(nums, k, [], result)
        return result

    def dfs(self, nums, k, path, result):
        if len(path) == k:
            # stop because the path is long enough
            result.append(path)
            return
        else:
            for i in range(len(nums)):
                self.dfs(nums[i + 1:], k, path + [nums[i]], result)
