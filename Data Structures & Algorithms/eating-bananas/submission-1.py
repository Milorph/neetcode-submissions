class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        low = 1
        high = piles[-1]
        curMax = 0

        while low <= high:
            current = 0
            mid = (low + high)//2

            for i in range(len(piles)):
                current += math.ceil(piles[i]/mid)
            if current <= h:
                curMax = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return curMax
