class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or (stack and stack.pop() != mappings.get(char)):
                    return False

        if stack:
            return False

        return True