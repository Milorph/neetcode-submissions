class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(row, col):
            
            if row == m - 1 and col == n - 1:
                return 1
            
            if row < 0 or row > m - 1 or col < 0 or col > n - 1:
                return 0
            
            
            res = dfs(row + 1, col) + dfs(row, col + 1)

            return res
        

        return dfs(0, 0)