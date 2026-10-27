class User:
    def __init__(self, id):
        self.user_id = id
        self.following = []

    def unfollow(self, id):
        self.following.remove(id)

    def follow(self, id):
        if id not in self.following: 
            self.following.append(id)


class Twitter:

    def __init__(self):
        self.tweets = []
        self.users = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            new_user = User(userId)
            self.users[userId]  = new_user
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        output = []
        if userId not in self.users.keys():
            return output
        count = 10
        user = self.users[userId] 
        for tweet in self.tweets[::-1]:
            if not count:
                break
            if tweet[0] in user.following or tweet[0] == user.user_id:
                output.append(tweet[1])
                count -= 1
        return output


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            new_user = User(followerId)
            self.users[followerId]  = new_user
        if followeeId not in self.users:
            new_user = User(followeeId)
            self.users[followeeId]  = new_user
        self.users[followerId].following.append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
         if followerId not in self.users or followeeId not in self.users:
            return 
         try:
            self.users[followerId].following.remove(followeeId)
         except: 
            return 