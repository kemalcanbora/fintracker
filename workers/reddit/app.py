import praw
from settings import (REDDIT_USERNAME,
                      REDDIT_USER_AGENT,
                      REDDIT_PASSWORD,
                      REDDIT_CLIENT_SECRET,
                      REDDIT_CLIENT_ID)


class RedditEngine:
    @staticmethod
    def parser(sub_reddit):
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                             client_secret=REDDIT_CLIENT_SECRET,
                             password=REDDIT_PASSWORD,
                             user_agent=REDDIT_USER_AGENT,
                             username=REDDIT_USERNAME)

        subreddit = reddit.subreddit(sub_reddit)
        for comment in subreddit.stream.comments(skip_existing=True):
            print({"source": sub_reddit,
                   "author": comment.author.name,
                   "created_utc": comment.created_utc,
                   "body": comment.body,
                   "url": comment.link_id}
                  )
