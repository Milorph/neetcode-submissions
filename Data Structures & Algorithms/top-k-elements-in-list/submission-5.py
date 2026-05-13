class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        freqmap = Counter(nums)

        for num, freq in freqmap.items():
            buckets[freq].append(num)
        
        res = []
        
        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                k -= 1
                if k <= 0:
                    return res