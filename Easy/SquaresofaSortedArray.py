# this is O(NlogN) due to the sorted()
'''
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i]**2

        nums = sorted(nums)
        return nums
'''

# this is one pass O(N)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1

        result = []


        # append the larger squares between the left and the right to result
        # at the end, return reversed(result)
        while left <= right:
            leftSquare = nums[left] ** 2
            rightSquare = nums[right] ** 2

            if leftSquare < rightSquare:
                result.append(rightSquare)
                right -= 1
            else:
                result.append(leftSquare)
                left += 1

        return result[::-1]
