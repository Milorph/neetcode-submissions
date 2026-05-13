class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []

        def isPalindrome(string, i, j):

            while i < j :
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
                
            return True

        def dfs(i):

            if i >= len(s):
                res.append(parts.copy())
                return
            
            for j in range(i, len(s)):

                if isPalindrome(s, i, j):
                    parts.append(s[i : j+1])
                    dfs(j+1)
                    parts.pop()
        
        dfs(0)

        return res
                
        
