class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = Counter(nums)
        result = []

        sortedNums = sorted(mapping.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            result.append(sortedNums[i][0])
        
        return result

