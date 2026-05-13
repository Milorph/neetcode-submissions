class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setx = set()

        for num in nums:
            if num in setx:
                return True
            setx.add(num)

        return False