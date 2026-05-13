class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for string in strs:
            lenStr = str(len(string))
            encoding += lenStr + '#' + string
        return encoding
            


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            word = s[i: i + length]
            output.append(word)

            i = i + length
        return output
                