class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        maxProd = nums[0]
        minProd = nums[0]

        
        for i in range(1, len(nums)):
            
            if nums[i] < 0: 
                maxProd, minProd = minProd, maxProd
            
            maxProd = max(nums[i], maxProd * nums[i])
            minProd = min(nums[i], minProd * nums[i])

            res = max(res, maxProd)
        
        return res