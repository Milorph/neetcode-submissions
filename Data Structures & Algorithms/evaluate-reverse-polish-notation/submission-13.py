class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char not in {'+', '-', '*', '/'}:
                stack.append(char)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if char == '+':
                    stack.append(num1 + num2)
                elif char == "-":
                    stack.append(num1 - num2)
                elif char == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(math.trunc(num1/num2))
        
        return int(stack[-1])
