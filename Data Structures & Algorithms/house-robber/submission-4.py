class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        for i in range(2, len(nums)):
            if i > 2:
                nums[i] = max(nums[i] + nums[i-2], nums[i] + nums[i-3])
            else:
                nums[i] = nums[i-2] + nums[i]

        return max(nums[-1], nums[-2])