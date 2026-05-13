class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]

        heapq.heapify(maxHeap)

        res = 0

        for i in range(k):
            res = heapq.heappop(maxHeap)
        
        return -res
