class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            low = 1
            high = max(piles)
            res = 0

            while low <= high:
                mid = (low + high)//2
                total = 0
                for pile in piles:
                    time = math.ceil(pile/mid)
                    total += time
                if total <= h:
                    res = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return res