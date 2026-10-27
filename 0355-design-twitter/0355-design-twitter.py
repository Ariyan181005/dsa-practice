class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.following[userId] | {userId}
        for user in users:
            tweets = self.tweets[user]
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush(heap, (-time, tweetId, user, idx))
        feed = []
        while heap and len(feed) < 10:
            neg_time, tweetId, user, idx = heapq.heappop(heap)
            feed.append(tweetId)
            idx -= 1
            if idx >= 0:
                time, nextTweetId = self.tweets[user][idx]
                heapq.heappush(heap, (-time, nextTweetId, user, idx))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)