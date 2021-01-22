import xml.etree.ElementTree as ET
from view.utils import convert_to_xml_date_time


# generates xml from a list of TweetData
def generate_xml_from_tweets_list(tweets):
    root = ET.Element("Tweets")
    for tweet in tweets:
        tweet_element = ET.SubElement(root, "Tweet",
                                      attrib={"ID": str(tweet.tweet_id)})

        # add all properties
        created = ET.SubElement(tweet_element, "created")
        created.text = convert_to_xml_date_time(tweet.created)

        text = ET.SubElement(tweet_element, "text")
        text.text = tweet.text

        geo = ET.SubElement(tweet_element, "geo")
        geo.text = tweet.geo

        coordinates = ET.SubElement(tweet_element, "coordinates")
        coordinates.text = tweet.coordinates

        place = ET.SubElement(tweet_element, "place")
        place.text = tweet.place

        retweet_count = ET.SubElement(tweet_element, "retweetcount")
        retweet_count.text = tweet.retweet_count

        favorite_count = ET.SubElement(tweet_element, "favoritecount")
        favorite_count.text = tweet.favorite_count

        lang = ET.SubElement(tweet_element, "lang")
        lang.text = tweet.lang

        user_location = ET.SubElement(tweet_element, "userlocation")
        user_location.text = tweet.user_location

        user_description = ET.SubElement(tweet_element, "userdescription")
        user_description.text = tweet.user_description

    # generates a bytes string, convert to regular one
    return ET.tostring(root).decode("utf-8")


def write_xml_string_to_file(file_path, xml_str):
    # file will be overwritten on every run
    with open(file_path, "w") as f:
        f.write(xml_str)
