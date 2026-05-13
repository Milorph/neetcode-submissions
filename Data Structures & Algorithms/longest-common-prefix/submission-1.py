class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        string = ""
        i = 0

        while True:
            if i >= len(strs[0]):
                break
            current_char = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != current_char:
                    return string
            string += current_char
            i += 1
        
        return string
            

        