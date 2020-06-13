import os
import tweepy 
import sys
import time
import json

consumer_key= ""
consumer_secret=""
access_key=""
access_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)    
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

u = api.get_user("screen_name")
print(u.id)
