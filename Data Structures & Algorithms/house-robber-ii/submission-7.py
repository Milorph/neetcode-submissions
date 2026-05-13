class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <=2 :
            return max(nums)

        def robbing(houses):

            for i in range(2, len(houses)):
                
                if i > 2:
                    houses[i] = max(houses[i-2] + houses[i], houses[i-3] + houses[i])

                else:
                    houses[i] = houses[i-2] + houses[i]
            return max(houses[-1], houses[-2])

        return max(robbing(nums[:-1]), robbing(nums[1:]))
            

# 9 -> 8 -> 3 -> 6 -> 2 -> 9