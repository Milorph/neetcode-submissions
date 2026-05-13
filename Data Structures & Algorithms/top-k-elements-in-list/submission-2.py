class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = Counter(nums)
        
        buckets = [[] for i in range(len(nums) + 1)]

        res = []
        
        for key, freq in mapping.items():
            buckets[freq].append(key)
        
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res

