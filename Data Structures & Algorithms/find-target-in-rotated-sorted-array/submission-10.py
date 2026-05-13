class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        pivot = low
        start = 0
        end = len(nums)-1

        if target >= nums[pivot] and target <= nums[end]:
            start = pivot
        else:
            end = pivot - 1
        

        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1