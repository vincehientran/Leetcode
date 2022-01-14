class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        
        # trival base case
        if len(nums) < 3:
            return 0
        
        count = 0
        
        for i in range(len(nums)-2):
            # set left and right pointers
            left = i + 1
            right = len(nums) - 1
            
            # loop until left and right are next to each other
            while left < right:
                # move left pointer to the right if the sum is less than target
                # move right pointer to the left if the sum is greater than target
                # counter increments by (right - left) because if nums[i] + nums[left] + nums[right] < target,
                # then we know all of nums[i] + nums[left] + nums[x] is less than target where x is between left and right
                if nums[i] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            
        return count
            