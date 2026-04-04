import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.fol = {}
        self.heap = []
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        heapq.heappush(self.heap, (-self.t, userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        x = heapq.nsmallest(len(self.heap), self.heap)
        out = []
        follows = self.fol.get(userId, set())

        for _, uid, tweet in x:
            if uid == userId or uid in follows:
                out.append(tweet)
        if len(out)>10:
            return out[0:10]
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.fol:
            self.fol[followerId] = set()
        self.fol[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.fol:
            self.fol[followerId].discard(followeeId)