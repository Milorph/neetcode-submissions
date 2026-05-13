class Solution:
    def canPartition(self, nums: List[int]) -> bool:
          
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        
        def dfs(curSum, i):
            if curSum == target:
                return True

            if curSum > target or i == len(nums):
                return False

            return dfs(curSum + nums[i], i + 1) or dfs(curSum, i + 1)

        return dfs(0,0)
#[1,2,4,5,6,2]