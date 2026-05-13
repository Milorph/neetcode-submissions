class TimeMap:

    def __init__(self):
        self.mapping = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = [[value,timestamp]]
        else:
            self.mapping[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        low = 0
        high = len(self.mapping[key]) - 1
        string = ""
        while low <= high:
            mid = (low + high)//2

            if self.mapping[key][mid][1] == timestamp:
                return self.mapping[key][mid][0]

            elif self.mapping[key][mid][1] < timestamp:
                string = self.mapping[key][mid][0]
                low = mid+1

            elif self.mapping[key][mid][1] > timestamp:
                high = mid - 1

            else:
                low = mid + 1

        return string

