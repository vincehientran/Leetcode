class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findLeftBound(nums, target), self.findRightBound(nums, target)]



    def findLeftBound(self, nums, target):

        left = 0
        right = len(nums) - 1
        ret = -1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                right = mid - 1
                ret = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return ret


    def findRightBound(self, nums, target):

        left = 0
        right = len(nums) - 1
        ret = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                left = mid + 1
                ret = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return ret
