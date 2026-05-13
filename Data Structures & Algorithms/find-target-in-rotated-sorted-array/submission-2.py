class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Find the pivot
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        left = 0
        right = len(nums) - 1

        # Handle the case where the array is not rotated
        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1