class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return res

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        comb = []

        def backtrack(index):

            if len(comb) == len(digits):
                res.append(''.join(comb))
                return

            for letter in mapping[digits[index]]:
                comb.append(letter)
                backtrack(index + 1)
                comb.pop()

        backtrack(0)
        
        return res

