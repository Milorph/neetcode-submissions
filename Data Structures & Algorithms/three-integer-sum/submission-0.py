class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            
            low = i + 1
            high = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while low < high:
                
                if nums[low] + nums[high] + nums[i] == 0:
                    res.append([nums[i],nums[low],nums[high]])
                    low += 1
                    high -= 1
                    while nums[low] == nums[low-1] and low < high:
                        low += 1
                    while nums[high] == nums[high + 1] and low < high:
                        high -= 1
                elif nums[low] + nums[high] + nums[i] < 0 and low < high:
                    low += 1
                    while nums[low] == nums[low-1] and low < high:
                        low += 1
                else:
                    high -= 1
                    while nums[high] == nums[high + 1] and low < high:
                        high -= 1
        return res
  
                    
        