class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            dp = [nums[0], max(nums[0], nums[1])]

            for i in range(2, len(nums)):

                # at the current house, the best we can do is
                # either how much we stole up to the last house OR
                # how much we stole up to the house 2 houses away PLUS the current house
                dp.append(max(dp[i-2] + nums[i], dp[i-1]))

            return dp[-1]

        # this can be made into constant space because
        # you only need to remember the previous two values of dp'''

        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            first = nums[0]
            second = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                current = max(first + nums[i], second)
                first = second
                second = current

            return second
