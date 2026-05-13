class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0] * len(temperatures)
        stack = []
        stack.append(0)

        for i in range(1, len(temperatures)):
            if stack and temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            if stack and temperatures[i] > temperatures[stack[-1]]:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    tempIndex = stack.pop()
                    temps[tempIndex] = i - tempIndex
                stack.append(i)
        
        return temps