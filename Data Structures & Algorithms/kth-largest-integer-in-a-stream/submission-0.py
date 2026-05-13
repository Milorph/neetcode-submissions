class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.count = k
        heapq.heapify(nums)

    def add(self, val: int) -> int:

        heapq.heappush(self.nums, val)
        maxi = heapq.nlargest(self.count, self.nums)
        return maxi[-1]

        
