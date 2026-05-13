class Solution:
    def reverse(self, x: int) -> int:
        
        
        original = x
        x = abs(x)
        copy_reverse = int(str(x)[::-1])
        
        if original < 0:
            copy_reverse *= -1
        
        if copy_reverse > 2**31 -1 or copy_reverse < -2**31:
            return 0
        
        
        return copy_reverse