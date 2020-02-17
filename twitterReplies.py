# Attempting to pull all tweet replies on a given tweet
# The big caveat here is that the search API only returns results for the last 7 days.

# Load tweets periodically with hashtag filters

import twitter
import sys
import json
import time
import logging
import urllib.parse
from twitter_Credentials import CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

from os import environ as e

t = twitter.Api(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token_key=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    sleep_on_rate_limit=True
)

















