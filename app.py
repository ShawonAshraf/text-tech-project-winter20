import sqlite3
from view.db import DataFactory
from view.generate_xml import generate_xml_from_tweets_list, write_xml_string_to_file, generate_xml_for_single_lists
from view.utils import validate_xml

database_path = "./db/my_data_merge.db"
xml_schema_path = "./schema/TweetDataSchema.xsd"

# open a connection to the database
connection = sqlite3.connect(database_path)
factory = DataFactory(connection)

# t = factory.get_all_user_locations()
# t = factory.get_tweet_by_id(1)
# t = factory.get_tweets_by_hashtag("#Borat")
# t = factory.get_all_texts()
# t = factory.get_all_hashtags()
# t = factory.rank_top_n_favorites(10)
#t = factory.rank_top_n_rt(10)
t = factory.get_all_tweets()
connection.close()

# xml = generate_xml_from_tweets_list(t)
# write to file
# default file directory is ./generated
# write_xml_string_to_file("generated/top_10_rt.xml", str(xml))

# validate
# validation = validate_xml(xml_file_path="generated/top_10_rt.xml", schema_file_path=xml_schema_path)
# print(validation)

# generate xml for all hashtags
# xml = generate_xml_for_single_lists(t, "HashTags", "HashTag")
# write_xml_string_to_file("generated/list_hashtags.xml", xml)

# generate xml for all locations
# xml = generate_xml_for_single_lists(t, "Locations", "Location")
# write_xml_string_to_file("generated/list_locations.xml", xml)

# generate xml for all tweets
xml = generate_xml_from_tweets_list(t)
write_xml_string_to_file("generated/all_tweets_merge.xml", xml)
