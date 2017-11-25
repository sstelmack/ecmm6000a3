#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy
import time #https://github.com/tweepy/tweepy

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "FXrVkx1oBMIPku883GgQ1eGoS"
consumer_secret = "ANmQQKgvhjMhJLbkmizTkXuZa3dVdURTKeDAivQMcOGhq0ZU0K"
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

#this function collects twitter profile tweets and returns Tweet objects
def get_tweets(screen_name):
    try:
        #https://developer.twitter.com/en/docs/tweets/timelines/overview describes user_timeline
        tweets = api.user_timeline(screen_name, count=20)
    except:
        user_profile = "broken"

#pull most popular

user = api.get_user('CitronResearch')
allTweets = api.user_timeline('CitronResearch',count=200)
maxRecount = 0
tweetid = 0
for tweet in allTweets:
	if tweet.retweet_count > maxRecount:
	
		print(tweet.retweet_count)
		print(tweet.text)