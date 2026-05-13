class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapping = {}
        start = 0
        maxFreq = 0
        for i in range(len(s)):
            mapping[s[i]] = mapping.get(s[i], 0) + 1
            maxFreq = max(maxFreq, mapping[s[i]])

            if(i - start + 1) - maxFreq > k:
                mapping[s[start]] -= 1
                start += 1
        return (i - start + 1)





