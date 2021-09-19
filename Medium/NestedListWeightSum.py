class Solution(object):
    def depthSum(self, nestedList, depth=1):
        weightedSum = 0

        for item in nestedList:
            if type(item) == int:
                weightedSum += item * depth
            else:
                weightedSum += self.depthSum(item, depth=depth+1)
                
        return weightedSum

sol = Solution()
test = [1,[4,[6]]]
print(sol.depthSum(test))
