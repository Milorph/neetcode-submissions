class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[len(height) - 1]

        totalTrap = 0

        left = 0
        right = len(height) - 1

        while left < right:
            if maxRight > maxLeft:
                left += 1
                trapped = min(maxRight, maxLeft) - height[left]
                totalTrap += trapped if trapped > 0 else 0
                maxLeft = max(maxLeft, height[left])
            else:
                right -= 1
                trapped = min(maxRight, maxLeft) - height[right]
                totalTrap += trapped if trapped > 0 else 0
                maxRight = max(maxRight, height[right])
        
        return totalTrap

