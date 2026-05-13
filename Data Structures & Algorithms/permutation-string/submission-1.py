class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        mapping = {}
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            mapping = Counter(s2[left:len(s1)+left])
            if mapping == s1Count:
                return True

            left += 1
            right += 1
            
        return False