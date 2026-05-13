class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        output = []

        buckets = [[] for i in range(len(nums) + 1)]
        
        for num, freq in freqMap.items():
            buckets[freq].append(num)
        
        for i in range(len(buckets) -1, -1, -1):
            if buckets[i]:
                for j in range(len(buckets[i])):
                    output.append(buckets[i][j])
                    k -= 1
                    if k == 0:
                        return output
        return output