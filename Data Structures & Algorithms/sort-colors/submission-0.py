class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr = [0] * 3

        for num in nums:
            arr[num] += 1
        
        for i in range(len(nums)):

            if arr[0] > 0:
                nums[i] = 0
                arr[0] -= 1

            elif arr[1] > 0:
                nums[i] = 1
                arr[1] -= 1

            else:
                nums[i] = 2
                arr[2] -= 1

        