class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}

        for i in range(len(strs)):

            sortStr = ''.join(sorted(strs[i]))
            if sortStr in hashMap:
                hashMap[sortStr].append(strs[i])
            else:
                hashMap[sortStr] = [strs[i]]
        result = list(hashMap.values())
        return result