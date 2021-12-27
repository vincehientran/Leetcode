class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        self.dfs(sorted(candidates), target, [], result, 0)
        return result

    def dfs(self, candidates, target, path, result, currentIdx):
        if target == 0:
            # the path adds up to the target perfectly
            result.append(path)
            return
        elif target < 0:
            # there is no way the path will add up to the target
            return
        else:
            for i in range(currentIdx, len(candidates)):
                if i > currentIdx and candidates[i - 1] == candidates[i]:
                    # this combindation was already added to the result, just skip this.
                    continue
                # continue dfs with the currentIdx to be the one after i
                # so after each recursive call, the for loop is basically going over candidates[i+1:]
                # instead of passing candidates[i+1:] in as the new candidates list,
                # we need to pass in the whole candidates list because we want to check the above condition
                self.dfs(candidates, target - candidates[i], path + [candidates[i]], result, i + 1)
