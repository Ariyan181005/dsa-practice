class User:
    def __init__(self, userId):
        self.id = userId
        self.tweets = {}
        self.following = set()
class Twitter:
    def __init__(self):
        self.time = 0
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.users.get(userId, User(userId))
        self.users[userId] = user
        user.tweets[tweetId] = self.time
        self.time += 1
    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.users:
            return []
        pq, ans = [], []
        heapq.heapify_max(pq)
        for tweetId, tweet in self.users[userId].tweets.items(): 
            heapq.heappush_max(pq, (tweet, tweetId))
        for user in self.users[userId].following:
            for tweetId, tweet in self.users[user].tweets.items():
                heapq.heappush_max(pq, (tweet, tweetId))
        i = 0
        while i < 10 and pq:
            ans.append(heapq.heappop_max(pq)[1])
            i += 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        follower = self.users.get(followerId, User(followerId))
        self.users[followerId] = follower
        followee = self.users.get(followeeId, User(followeeId))
        self.users[followeeId] = followee
        follower.following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].following.discard(followeeId)
