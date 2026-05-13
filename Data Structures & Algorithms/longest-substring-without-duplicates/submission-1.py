class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longSub = 0
        hashSet = set()
        start = 0
        for i in range(len(s)):
            while s[i] in hashSet:
                hashSet.remove(s[start])
                start += 1
            hashSet.add(s[i])
            longSub = max(longSub, i - start + 1)
        
        return longSub

