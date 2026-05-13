class TimeMap:

    def __init__(self):
        self.mapping = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = []
        self.mapping[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.mapping:
            lis = self.mapping[key]
            left = 0
            right = len(lis) - 1
            while left <= right:
                mid = (left + right)//2
                if lis[mid][1] == timestamp:
                    return lis[mid][0]
                elif lis[mid][1] > timestamp:
                    right = mid - 1
                else:
                    left = mid + 1
            if right >= 0:
                return lis[right][0]

        return ""
        
