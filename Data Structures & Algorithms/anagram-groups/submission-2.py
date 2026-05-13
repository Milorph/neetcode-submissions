class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        
        for i in range(len(strs)):
            srtStr = "".join(sorted(strs[i]))
            if srtStr in hashmap:
                hashmap[srtStr].append(strs[i])
            else:
                hashmap[srtStr] = [strs[i]]
        
        return hashmap.values()
