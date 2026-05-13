class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapS1 = Counter(s1)
        mapS2 = {}
        left = 0
        right = len(s1)-1
        while right < len(s2):
            mapWin = Counter(s2[left:len(s1)+left])
            print(mapWin)
            if mapWin == mapS1:
                return True

            left += 1
            right += 1
        
        
        return False
