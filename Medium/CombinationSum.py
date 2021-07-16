class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        self.dfs(candidates, target, [], result)
        return result


    def dfs(self, candidates, target, path, result):
        if target == 0:
            # the path perfectly adds up to the target
            result.append(path)
            return
        elif target < 0:
            # the path does not lead to the target
            return
        else:
            for i in range(len(candidates)):
                self.dfs(candidates[i:], target - candidates[i], path + [candidates[i]], result)
        
