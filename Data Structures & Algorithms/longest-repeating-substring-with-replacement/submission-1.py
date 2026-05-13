class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        mapping = {}
        start = 0
        longest = 0

        for i in range(len(s)):
            mapping[s[i]] = mapping.get(s[i], 0) + 1
            longest = max(longest, mapping[s[i]])

            if (i - start - longest + 1) > k:
                mapping[s[start]] -= 1
                start += 1
        
        return len(s) - start


