# Load tweets periodically with hashtag filters

import tweepy as tw
import pandas as pd
import matplotlib.pyplot as plt
from twitter_Credentials import CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tw.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth)

public_tweets = api.home_timeline()     # Access your home timeline
for tweet in public_tweets:
    print(tweet.text)


















