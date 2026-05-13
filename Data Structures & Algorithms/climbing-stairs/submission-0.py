class Solution:
    def climbStairs(self, n: int) -> int:
        memo = []
        memo.append(1)
        memo.append(2)

        for i in range(2, n):
            memo.append(memo[-1] + memo[-2])
        
        return memo[n-1]