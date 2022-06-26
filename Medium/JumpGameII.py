class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [len(nums) - 1 for _ in range(len(nums))]
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                continue
            dp[i] = min(dp[min(len(nums) - 1,i+1):i + 1 + nums[i]]) + 1

        return dp[0]
