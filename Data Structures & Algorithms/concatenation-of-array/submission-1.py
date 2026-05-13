class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums) * 2
        res = [0] * length
        for i in range(len(nums)):
            res[i] = nums[i]
            res[i+len(nums)] = nums[i]
        return res