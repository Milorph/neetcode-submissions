class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            length = len(word)
            s += str(length) + "#" + str(word)
        
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            word = s[j + 1: j + length + 1]
            res.append(word)
            i = j + length + 1

        return res
