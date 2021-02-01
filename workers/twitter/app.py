import tweepy
from settings import *


class TwitterEngine():
    def __init__(self):
        self.auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN_KEY, TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def parser(self, screen_name, twitter_count=GET_TWEET_COUNT, retweet=False):
        tweet = []
        try:
            new_tweets = self.api.user_timeline(screen_name=screen_name, count=twitter_count, tweet_mode="extended",
                                                include_rts=retweet)
            user = self.api.get_user(screen_name=screen_name)
            full_name = user.name
            location = user.location
            protected = user.protected
            creation_date = user.created_at.timestamp()  # epoch time

            for i in new_tweets:
                tweet.append({"text": i.full_text, "publish_date": i.created_at.timestamp()})  # epoch time

            return {"twitter_location": location,
                    "twitter_creation_date": creation_date,
                    "twitter_full_name": full_name,
                    "twitter_text": tweet,
                    "protected": protected
                    }

        except tweepy.TweepError as e:
            if e.api_code == 34:
                print("not exist this user")
            if e.args[0] == "Not authorized.":
                print("Not authorized..follow {}".format(screen_name))
                try:
                    user = self.api.get_user(screen_name=screen_name)
                    self.api.create_friendship(user.id)
                except:
                    pass