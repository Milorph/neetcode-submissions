class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def dfs(idx1, idx2, idx3):
            
            if idx1 + idx2 == len(s3):
                return True
            
            if (idx1 < len(s1) and s1[idx1] != s3[idx3]) and (idx2 < len(s2) and s2[idx2] != s3[idx3]):
                return False
            
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            
            if (idx1 < len(s1) and s1[idx1] == s3[idx3]) and (idx2 < len(s2) and s2[idx2] == s3[idx3]):
                
                memo[(idx1,idx2)] = dfs(idx1 + 1, idx2, idx3 + 1) or dfs(idx1, idx2 + 1, idx3 + 1)
            elif idx1 < len(s1) and s1[idx1] == s3[idx3]:
                memo[(idx1,idx2)] = dfs(idx1 + 1, idx2, idx3 + 1)
            elif idx2 < len(s2) and s2[idx2] == s3[idx3]:
                memo[(idx1,idx2)] = dfs(idx1, idx2 + 1, idx3 + 1)
            else:
                return False
            
            return memo[(idx1, idx2)]

        
        return dfs(0,0,0)