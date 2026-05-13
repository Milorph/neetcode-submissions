class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        hashset = set()

        start = 0
        for i in range(len(s)):

            if s[i] not in hashset:
                hashset.add(s[i])
                longest = max(longest, len(hashset))
            else:
                while s[start] != s[i]:
                    hashset.remove(s[start])
                    start += 1
                start += 1
        
        return longest
            
