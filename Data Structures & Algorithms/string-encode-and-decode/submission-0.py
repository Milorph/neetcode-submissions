class Solution:

    def encode(self, strs: List[str]) -> str:
        resStr = ""
        for i in range(len(strs)):
            length = len(strs[i])
            resStr += str(length) + "#" + strs[i]
        return resStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            word = s[j+1:j+1+length]
            res.append(word)
            i = j+1+length
            
        return res
        