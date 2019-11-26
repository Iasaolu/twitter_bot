import tweepy
import time 

consumer_key = "MNsVKdHLL6OZuT7CQlW4fBscO"
consumer_secret = "JJnQYmmSYCIbg9PaOi6XFj66VbgWbUw7DRGeVFBpIpYhqmP5wH"
key = "1077862836758548480-H5bwrlnYYcp2j2AyCB5LnJmTDjWw7O"
secret = "bFtCWUFsyipAZgrGBJxNtMGyEUDHgoQLwNVvs7qSREQVu"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key,secret)
api = tweepy.API(auth)

hashtag = ("100daysofcode","python")
tweetNumber = 10
tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)

searchbot()