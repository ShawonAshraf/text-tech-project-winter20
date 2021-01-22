import sqlite3
from view.tweet_data import TweetData
from view.utils import get_hashtag_from_text

"""
class DataFactory, given a connection to a database, runs queries
and returns results.
"""


class DataFactory(object):
    def __init__(self, connection):
        self.connection = connection

    # run a query and return the cursor
    def __run_query(self, query):
        cursor = self.connection.execute(query)
        return cursor

    # creates tweet array from a cursor
    # which you get as a result of executing a query
    def __prepare_tweet_array(self, cursor):
        tweets = []
        for row in cursor:
            tweet_data = TweetData(row[0], row[1], row[2], row[3], row[4],
                                   row[5], row[6], row[7], row[8], row[9],
                                   row[10])
            tweets.append(tweet_data)

        return tweets

    # returns all tweets as TweetData list
    def get_all_tweets(self):
        query = "SELECT * FROM TweetData"
        cursor = self.__run_query(query)
        return self.__prepare_tweet_array(cursor)

    # get by id
    # returns a list
    def get_tweet_by_id(self, tweet_id):
        query = f"SELECT * FROM TweetData WHERE id={tweet_id}"
        cursor = self.__run_query(query)
        return self.__prepare_tweet_array(cursor)

    # get tweets by language
    def get_tweets_by_lang(self, lang):
        query = f"select * from TweetData where lang is \"{lang}\""
        cursor = self.__run_query(query)
        return self.__prepare_tweet_array(cursor)

    def get_all_user_locations(self):
        idx = 9
        query = "select userlocation from TweetData"
        cursor = self.__run_query(query)

        locations = [row for row in cursor]
        return locations

    def get_all_texts(self):
        query = "select text from TweetData"
        cursor = self.__run_query(query)

        idx = 2
        texts = [text for text in cursor]
        return texts

    def get_all_hashtags(self):
        texts = self.get_all_texts()
        hashtags = set()

        for text in texts:
            # text is a tuple here
            tags = get_hashtag_from_text(text[0])
            for tag in tags:
                hashtags.add(tag)

        return hashtags

    # example: #Borat
    def get_tweets_by_hashtag(self, hashtag):
        query = f'select * from TweetData where text like "%{hashtag}%"'
        cursor = self.__run_query(query)

        return self.__prepare_tweet_array(cursor)

    # rank based on favorite count
    def rank_top_n_favorites(self, n):
        tweets = self.get_all_tweets()
        # sort in descending order
        sorted_tweets = sorted(tweets, key=lambda k: k.favorite_count, reverse=True)
        return sorted_tweets[:n]

    # rank top n retweeted
    def rank_top_n_rt(self, n):
        tweets = self.get_all_tweets()
        # sort in descending order
        sorted_tweets = sorted(tweets, key=lambda k: k.retweet_count, reverse=True)
        return sorted_tweets[:n]
