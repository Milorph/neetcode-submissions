class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        
        curLong = 0
        maxLong = 0
        for num in hashSet:
            if num - 1 not in hashSet:
                curLong = 1
                while num + 1 in hashSet:
                    num +=1
                    curLong += 1
                maxLong = max(maxLong, curLong)

        return maxLong