class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        comb = []
        
        candidates.sort()

        def backtrack(total, i):

            if total == target:
                res.add(tuple(comb.copy()))
                return
            
            if i >= len(candidates) or total > target:
                return
            
            comb.append(candidates[i])
            backtrack(total + candidates[i],i+1)
            comb.pop()
            backtrack(total,i+1)
        
        backtrack(0,0)

        return [list(t) for t in res]