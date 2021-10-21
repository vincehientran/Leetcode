class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        product = 1
        for num in nums:
            product *= num
            
        ret = []
        for i, num in enumerate(nums):
            if num == 0:
                withOutZeroProduct = 1
                for n in nums[:i] + nums[i+1:]:
                    withOutZeroProduct *= n
                ret.append(withOutZeroProduct)
            else:
                ret.append(product/num)
            
        return ret
            