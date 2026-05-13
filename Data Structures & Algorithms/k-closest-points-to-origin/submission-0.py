class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []

        for i in range(len(points)):

            eucl_dist = math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)**2)

            heapq.heappush(maxHeap, (-eucl_dist, points[i]))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [point for (_, point) in maxHeap]