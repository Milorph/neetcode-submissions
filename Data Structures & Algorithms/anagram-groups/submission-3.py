class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            original = string
            sortstr = "".join(sorted(string))
            if sortstr in hashmap:
                hashmap[sortstr].append(original)
            else:
                hashmap[sortstr] = [original]
        
        return list(hashmap.values())
