class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resLen = -1
        string = ""
        for i in range(len(s)):
            l = i
            r = i
            if l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1

            if r - l > resLen:
                resLen = r - l
                string = s[l + 1 :r]
            
            l = i
            r = i + 1

            if l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1

            if r - l > resLen:
                resLen = r - l
                string = s[l + 1:r]
        
        return string
                