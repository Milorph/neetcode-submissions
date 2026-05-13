class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        if len(nums) <= 2:
            return max(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            if i > 2:
                dp[i] = max(nums[i] + dp[i-2], nums[i] + dp[i-3])
            else:
                dp[i] = dp[i - 2] + nums[i]

        print(nums)
        print(dp)
        return max(dp[-1], dp[-2])