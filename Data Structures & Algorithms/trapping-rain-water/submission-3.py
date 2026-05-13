class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        maxTrap = 0
        totalTrap = 0
        while left < right:
            possTrap = 0
            if height[left] < height[right]:
                possTrap = maxTrap - height[left]
            else:
                possTrap = maxTrap - height[right]
            if possTrap > 0:
                totalTrap += possTrap

            maxTrap = max(maxTrap, min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return totalTrap

            
