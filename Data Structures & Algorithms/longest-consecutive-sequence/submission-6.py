class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        maxStreak = 0

        for num in hashSet:
            streak = 1
            cpyNum = num
            while cpyNum - 1 in hashSet:
                cpyNum -= 1
                streak += 1
            maxStreak = max(maxStreak, streak)
            
        
        return maxStreak



        