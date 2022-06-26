class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = len(nums)-1

        # white is the pivot
        # if the color at the pivot is blue, then toss it to the end
        # if the color at the pivot is red, then toss it to the beginning
        # if the color at the pivot is white, then just increment the index of the pivot by 1
        while white <= blue:
            if nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            elif nums[white] == 1:
                white += 1
            elif nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
