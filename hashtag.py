# Load tweets periodically with hashtag filters

import tweepy as tw
import pandas as pd
import matplotlib.pyplot as plt
from twitter_Credentials import CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tw.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth)  # Declare a tweepy API object

public_tweets = api.home_timeline()     # Access your home timeline
for tweet in public_tweets:
    print(tweet.text)


# This simple stream listener prints status text
class MyStreamListener(tw.StreamListener):
    def on_status(self, status):
        if status.retweeted_status:
            return
        print(status.retweeted_status)
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False


myStreamListener = MyStreamListener()
myStream = tw.Stream(auth=api.auth, listener=myStreamListener)

# Most twitter streams will use filter, user_stream, or sitestream
# To find user ID: http://gettwitterid.com/
# myStream.filter(track=['#jre'], follow=['427089628'], is_async=True)
# myStream.filter(track=['trump', 'clinton'], is_async=True)
myStream.filter(follow=['911594293667749888'], is_async=True)



# https://twitter.com/lexfridman
# 427089628














