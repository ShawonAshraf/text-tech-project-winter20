class TweetData(object):
    def __init__(self, tweet_id, created, text, geo, coordinates, place, retweet_count, favorite_count, lang,
                 user_location, user_description):
        self.tweet_id = tweet_id
        self.created = created
        self.text = text
        self.geo = geo
        self.coordinates = coordinates
        self.place = place
        self.retweet_count = retweet_count
        self.favorite_count = favorite_count
        self.lang = lang
        self.user_location = user_location
        self.user_description = user_description

    def __repr__(self):
        return str(self.__dict__)
