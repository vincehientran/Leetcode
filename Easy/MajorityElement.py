class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        maxNum = nums[0]
        maxCount = 0
        for k, v in hashmap.items():
            if v > maxCount:
                maxCount = v
                maxNum = k

        return maxNum
