class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {} #key = (index, total), val = number of combinations


        def dfs(i, total):

            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            if i >= len(nums):
                return 0
            
            if (i, total) in dp:
                return dp[(i,total)]
            
            #option 1 is to add
            add = dfs(i + 1, total + nums[i])
            #option 2 is to subtract
            sub = dfs(i + 1, total - nums[i])

            dp[(i,total)] = add + sub

            return dp[(i,total)] 

        return dfs(0,0)
