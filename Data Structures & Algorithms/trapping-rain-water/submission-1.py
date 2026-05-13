class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0

        total = 0

        left = 0
        right  = len(height) - 1

        while left < right:

            maxLeft = max(height[left], maxLeft)
            maxRight = max(height[right], maxRight)

            if height[left] < height[right]:
                left += 1
                possTrap = min(maxLeft,maxRight)
                totalTrap = possTrap - height[left]
                if totalTrap > 0:
                    total += totalTrap
            else:
                right -= 1
                possTrap = min(maxLeft,maxRight)
                totalTrap = possTrap - height[right]
                if totalTrap > 0:
                    total += totalTrap
        return total

