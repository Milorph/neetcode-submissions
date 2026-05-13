class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == ")":

                if not stack or not stack.pop() == "(":
                    return False
            elif s[i] == "}":

                if not stack or not stack.pop() == "{":
                    return False
            elif s[i] == "]":

                if not stack or not stack.pop() == "[":
                    return False
            else:
                stack.append(s[i])
        if stack:
            return False
        return True