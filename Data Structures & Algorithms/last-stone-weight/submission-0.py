class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ stone * -1 for stone in stones]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_one = heapq.heappop(stones)
            stone_two = heapq.heappop(stones)
            smash = (stone_one * -1) - (stone_two * -1)
            if smash > 0:
                heapq.heappush(stones, smash * -1)
        
        if stones:
            return -stones[-1]
        
        return 0