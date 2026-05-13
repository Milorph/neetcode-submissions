class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.followMap = defaultdict(set)
        self.postMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        if len(self.followMap[userId]) >= 10:
            maxHeap = []
            for followeeId in self.followMap[userId]:
                if followeeId in self.postMap:
                    index = len(self.postMap[followeeId]) - 1
                    timestamp, tweetId = self.postMap[followeeId][index]
                    heapq.heappush(maxHeap, [timestamp, tweetId, followeeId, index - 1])
                if len(maxHeap) > 10:
                    heapq.heappop(maxHeap)
            while maxHeap:
                timestamp, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-timestamp, tweetId, followeeId, index])

        else:
            for followeeId in self.followMap[userId]:
                if followeeId in self.postMap: 
                    index = len(self.postMap[followeeId]) - 1
                    timestamp, tweetId = self.postMap[followeeId][index]
                    heapq.heappush(minHeap, [-timestamp, tweetId, followeeId, index - 1])
        
        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                timestamp, tweetId = self.postMap[followeeId][index]
                heapq.heappush(minHeap, [-timestamp, tweetId, followeeId, index - 1] )
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

