class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(total, i, comb ):
            if total == target:
                res.append(comb.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            
            comb.append(nums[i])
            dfs(total + nums[i], i, comb)
            comb.pop()
            dfs(total, i + 1, comb)
        
        dfs(0, 0, [])

        return res
            