class Solution:
    def canPartition(self, nums: List[int]) -> bool:
          
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        memo = {}
        
        def dfs(curSum, i):
            if curSum == target:
                return True

            if curSum > target or i == len(nums):
                return False
            
            if (i, curSum) in memo:
                return memo[i,curSum]

            include = dfs(curSum + nums[i], i + 1)
            exclude = dfs(curSum, i + 1)

            memo[(i, curSum)] = include or exclude

            return memo[(i,curSum)]

        return dfs(0,0)
#[1,2,4,5,6,2]