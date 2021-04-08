class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            pivot = len(nums)//2

            breakpoint = self.partition(nums, pivot)


            if k < breakpoint+1:
                return self.findKthLargest(nums[:breakpoint], k)
            elif k > breakpoint+1:
                return self.findKthLargest(nums[breakpoint+1:], k-(breakpoint+1))
            else:
                return nums[breakpoint]



    def partition(self, lst, pivot):
        lst[-1], lst[pivot] = lst[pivot], lst[-1]

        breakpoint = 0

        for i in range(len(lst)-1):
            if lst[i] > lst[-1]:
                lst[breakpoint], lst[i] = lst[i], lst[breakpoint]
                breakpoint += 1

        lst[breakpoint], lst[-1] = lst[-1], lst[breakpoint]

        return breakpoint
