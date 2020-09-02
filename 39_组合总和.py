class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        return self.combinationSumRecursively(candidates,target)

    def combinationSumRecursively(self, sorted_candidates, target):
        ret = []
        if target == 0:
            return [[],]
        elif target < 0:
            return None
        for idx,candidate in enumerate(sorted_candidates):
            previous_ret = self.combinationSumRecursively(sorted_candidates[idx:], target-candidate)
            if previous_ret is None:
                continue
            else:
                for p_ret in previous_ret:
                    ret.append(p_ret+[candidate,])
        return None if ret == [[],] else ret        