class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}
        
        def dfs(i, total):
            
            if i >= len(coins) or total > amount:
                return 0
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            if total == amount:
                return 1
            
            take = dfs(i, total + coins[i])
            skip = dfs(i+1, total)
            
            dp[(i, total)] = take + skip

            return dp[(i,total)]
        
        return dfs(0, 0)

        