class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        found = [False for _ in range(len(nums))]
        
        for num in nums:
            # if it is a valid index
            if num >= 0 and num < len(found):
                found[num] = True
                
        for i in range(len(found)):
            # find the first index that isnt found yet
            if not found[i]:
                return i
        
        # if all indices are found, then output the number after the largest index
        return len(nums)