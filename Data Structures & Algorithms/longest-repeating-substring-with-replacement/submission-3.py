class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        freq = 0
        longest = 0
        mapping = {}

        for i in range(len(s)):
            mapping[s[i]] = mapping.get(s[i], 0) + 1
            freq = max(freq, mapping[s[i]])

            if (i - start + 1) - freq > k:
                mapping[s[start]] = mapping[s[start]] - 1
                start += 1
            
            longest = max(longest, i - start + 1)
        
        return longest
