import sqlite3
from view.db import DataFactory
from view.generate_xml import generate_xml_from_tweets_list, write_xml_string_to_file
from view.utils import validate_xml

database_path = "./db/my_data.db"
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
t = factory.rank_top_n_rt(10)
connection.close()

xml = generate_xml_from_tweets_list(t)
# write to file
# default file directory is ./out
write_xml_string_to_file("./out/top_10_rt.xml", str(xml))

# validate
validation = validate_xml(xml_file_path="./out/id_1.xml", schema_file_path=xml_schema_path)
print(validation)