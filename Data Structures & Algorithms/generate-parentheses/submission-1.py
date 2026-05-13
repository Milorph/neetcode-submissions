class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def generate(numOpen, numClose, n, string):
            if len(string) == n*2:
                res.append(string)
                return
            
            if numOpen < n:
                generate(numOpen + 1, numClose, n, string + '(')
            if numClose < numOpen:
                generate(numOpen, numClose + 1, n, string + ")")
        
        generate(0, 0, n, "")
        return res
                