import tweepy
import csv
import json

# input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('retrieve.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)
# outfile = open("retrieve.json", 'w')
for tweet in tweepy.Cursor(api.search, q="#Cyberpunk2077", lang="en",  # count=100
                           since="2020-01-01").items():
    # json.dump(tweet._json, outfile)

    # print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at,
                        tweet.text.encode('utf-8'),
                        tweet.geo,
                        tweet.coordinates,
                        tweet.place,
                        tweet.retweet_count,
                        tweet.favorite_count,
                        tweet.lang.encode('utf-8'),
                        tweet.user.location.encode('utf-8'),
                        tweet.user.description.encode('UTF-8')])
