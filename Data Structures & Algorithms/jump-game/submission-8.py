class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        dp[0] = True

        for i in range(len(nums) - 1):
            
            if dp[i] == True:
                if i + nums[i]>= len(nums):
                    dp[i:] = [True] * (len(dp) - i)
                else:
                    dp[i : i + nums[i] + 1] = [True] * (nums[i] + 1)
            
        return dp[-1]
            