import heapq

class Tweet:
    COUNT = 0

    def __int__(self, user_id, tweet_text):
        self.id = Tweet.COUNT
        self.user_id = user_id
        self.tweet_text = tweet_text
        Tweet.COUNT += 1

    @classmethod
    def create(cls, user_id, tweet_text):
        return cls(user_id, tweet_text)

class MiniTwitter:
    TIMESTAMP = 0  # we have multiple , need to tract each user id

    def __init__(self):
        self.user_tweets = {}
        self.user_followings = {}

    def postTweet(self, user_id, tweet_text):
        MiniTwitter.TIMESTAMP += 1
        tweets = self.user_tweets.get(user_id, [])
        tweet = Tweet.create(user_id, tweet_text)
        tweets.append((MiniTwitter.TIMESTAMP, tweet))
        self.user_tweets[user_id] = tweets
        return tweet

    def getNewsFeed(self, user_id):
        friends = self.user_followings.get(user_id, set())
        all_last_10 = [self.user_tweets.get(user_id, [])[-1:-11:-1]]
        for friend in friends:
            all_last_10.append(self.user_tweets.get(friend, [])[-1:-11:-1])
        return self._sort_news_feed(all_last_10)

    # merge k sorted lists using priority queue
    def _sort_news_feed(self, all_last_10):
        heap = []
        for last_10 in all_last_10:
            if len(last_10) == 0:
                continue
            itr = iter(last_10)
            item = next(itr)
            # heap is always min order in python3, so we need to reverse the timestamp
            # heap is not object oriented in python3
            heapq.heappush(heap, (-item[0], item[1], itr))

        result = []
        while len(result) < 10 and len(heap) > 0:
            _, tweet, itr = heapq.heappop(heap)
            result.append(tweet)
            # python3 has no hasNext method
            next_item = next(itr, None)
            if not next_item:  # if not valid
                continue
            heapq.heappush(heap, (-next_item[0], next_item[1], itr))

        return result

    def getTimeline(self, user_id):
        tweets = self.user_tweets.get(user_id, [])
        # return last 10 tweets from most recent to least
        last_10 = tweets[-1:-11:-1]
        # retrieve tweets
        return [t[1] for t in last_10]

    def follow(self, from_user_id, to_user_id):
        followings = self.user_followings.get(from_user_id, set())
        followings.add(to_user_id)
        self.user_followings[from_user_id] = followings

    def unfollow(self, from_user_id, to_user_id):
        followings = self.user_followings.get(from_user_id, set())
        if to_user_id in followings:
            followings.remove(to_user_id)