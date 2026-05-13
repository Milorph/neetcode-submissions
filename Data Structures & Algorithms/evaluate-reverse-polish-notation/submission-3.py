class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):
            print(stack)
            if tokens[i] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)

            elif tokens[i] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)

            elif tokens[i] == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(math.trunc(num2/num1))

            elif tokens[i] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]


        