class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while nums[right] == nums[right - 1] and left < right:
                        right -= 1
                    right -= 1
                    while nums[left] == nums[left + 1] and left < right:
                        left += 1
                    left += 1
                    
                elif nums[i] + nums[left] + nums[right] > 0:
                    while nums[right] == nums[right - 1] and left < right:
                        right -= 1
                    right -= 1
                else:
                    while nums[left] == nums[left + 1] and left < right:
                        left += 1
                    left += 1
        
        return res

