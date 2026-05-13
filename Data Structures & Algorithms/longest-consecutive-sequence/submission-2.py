class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        longSeq = 0

        for num in hashSet:
            if num - 1 not in hashSet:
                curNum = num
                curSeq = 1

                while curNum + 1 in hashSet:
                    curNum += 1
                    curSeq += 1
                
                longSeq = max(curSeq, longSeq)
                
        return longSeq
