class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}
        length = len(nums)
        for num in nums:

            mapping[num] = mapping.get(num, 0) + 1
            if mapping[num] > length//2:
                return num