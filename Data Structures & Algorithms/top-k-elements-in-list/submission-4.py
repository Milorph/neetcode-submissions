class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []

        buckets = [[] for _ in range(len(nums) + 1)]

        mappings = Counter(nums)

        for val, freq in mappings.items():
            buckets[freq].append(val)
        
        while k > 0:
            for i in range(len(buckets) - 1, -1, -1):
                if buckets[i]:
                    for j in range(len(buckets[i])):
                        if k == 0:
                            break
                        res.append(buckets[i][j])
                        k -= 1

        return res
            
