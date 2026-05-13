class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxi = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            if curSum + nums[i] < nums[i]:
                curSum = nums[i]
            else:
                curSum += nums[i]
            maxi = max(maxi, curSum)
        
        return maxi