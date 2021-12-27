class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        correctNumbers = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                holder = nums[correctNumbers]
                nums[correctNumbers] = nums[i]
                nums[i] = holder

                correctNumbers += 1
