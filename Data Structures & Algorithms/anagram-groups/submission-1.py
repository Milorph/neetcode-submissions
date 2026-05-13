class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in range(len(strs)):
            sortStr = ''.join(sorted(strs[i]))
            if sortStr not in hashMap.keys():
                hashMap[sortStr] = [strs[i]]
            else:
                hashMap[sortStr].append(strs[i])
        
        return list(hashMap.values())

