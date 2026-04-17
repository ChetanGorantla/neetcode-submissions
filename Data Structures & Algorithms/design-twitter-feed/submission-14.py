class Twitter:

    def __init__(self):
        # decrement time to make it a maxheap priority
        self.time = 0
        # stores a dict of user_id: maxheap(time, tweet_id)
        self.tweets = {}
        # follows
        self.follows = {}

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((self.time, tweetId))

            
        else:
            self.tweets[userId] = [(self.time, tweetId)]
        
        self.time-=1


    def getNewsFeed(self, userId: int) -> List[int]:
        # at runtime we need to create a new queue of all the
        # posts and their respective times
        # and then truncate it to 10 values and return it
        print(f"News feed for {userId}")
        overall_posts = []
        people = [userId]
        if userId in self.follows:
            print(f"{userId} follows {self.follows[userId]}")
            people += self.follows[userId]
        
        if userId not in self.tweets:
            self.tweets[userId] = []

        print(people)
        for person in people:
            for tweet in self.tweets[person]:
                heapq.heappush(overall_posts, tweet)
                print(tweet)
        extraction_vals = []
        out = []
        i = 0
        while overall_posts and i < 10:
            extraction_vals.append(heapq.heappop(overall_posts))
            i+=1



        return [val[1] for val in extraction_vals]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows:
            self.follows[followeeId] = []
        if followerId not in self.follows:
            self.follows[followerId] = []

        if followerId == followeeId or followeeId in self.follows[followerId]:
            return
        self.follows[followerId].append(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
    
