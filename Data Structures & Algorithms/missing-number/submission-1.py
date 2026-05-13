class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total = sum(nums)
        n = len(nums)

        res = 0
        for i in range(n + 1):
            res += i
        
        return res - total
