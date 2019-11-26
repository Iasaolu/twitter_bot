import tweepy
import time

consumer_key = 
consumer_secret = 
key = 
secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key,secret)

api = tweepy.API(auth)
#tweet on timeline
#api.update_status('Hello WOrld! - Two')
#print("Status Updated")


#print(tweets[1].text)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    last_seen_id = (file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return 

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if "welovecrypto" in tweet.full_text.lower():
            print("New Tweet Found")
            print(str(tweet.id) + ' - ' + tweet.full_text)

            api.update_status("@"+ tweet.user.screen_name + " Heyo There, We do Love Crypto", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(15)


