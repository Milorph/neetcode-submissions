class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(curStr, openCount, closeCount):

            if len(curStr) == 2*n:
                result.append(curStr)
                return
            
            if openCount < n:
                backtrack(curStr + "(", openCount + 1, closeCount)
            
            if closeCount < openCount:
                backtrack(curStr + ")", openCount, closeCount + 1)
        
        backtrack("", 0, 0)

        return result