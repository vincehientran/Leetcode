class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums = sorted(nums)

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ret.add((nums[i], nums[l], nums[r]))
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
                    
        return [list(tup) for tup in ret]