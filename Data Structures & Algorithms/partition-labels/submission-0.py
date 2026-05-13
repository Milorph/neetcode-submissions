class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        mapping = defaultdict(int)

        for i in range(len(s)):

            mapping[s[i]] = max(mapping[s[i]], i)
        
        
        left = 0
        right = mapping[s[0]]
        res = []
        count = 0

        while left < len(s) and right < len(s):
            

            count += 1
            if left == right:
                res.append(count)
                count = 0
                if right + 1 < len(s):
                    right = mapping[s[right + 1]]
            right = max(right, mapping[s[left]])
            left += 1

        
        return res
