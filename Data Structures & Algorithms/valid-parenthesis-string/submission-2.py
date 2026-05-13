class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stackOpen = []
        stackStar = []

        for i in range(len(s)):
            
            if s[i] == '(':
                stackOpen.append(i)
            elif s[i] == ')':
                if stackOpen:
                    stackOpen.pop()
                elif stackStar:
                    stackStar.pop()
                else:
                    return False
            else:
                stackStar.append(i)
        
        while stackOpen and stackStar:

            open_par = stackOpen.pop()
            star_index = stackStar.pop()

            if open_par > star_index:
                return False
                
            
                
        return not stackOpen
