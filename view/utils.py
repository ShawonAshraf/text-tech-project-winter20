import xmlschema
from datetime import date, time


def get_hashtag_from_text(text):
    hashtags = set()

    splits = text.split()

    for s in splits:
        if s.startswith("#"):
            hashtags.add(s)

    return hashtags


# convert tweet.created string to xml supported datetime
def convert_to_xml_date_time(created):
    # 2021/1/4 23:28
    date_string, time_string = created.split()

    # process date_string
    year, month, day = date_string.split("/")

    # process time_string
    parts = time_string.split(":")

    hour = int(parts[0])
    minutes = int(parts[1])

    if len(parts) == 2:
        seconds = 0
    else:
        seconds = parts[2]

    # merge into one string
    formatted = f"{str(date(int(year), int(month), int(day)))}T{str(time(hour, minutes, seconds))}"
    return formatted


# validates xml against a schema
# params: path to xml, path to schema file(xsd)
def validate_xml(xml_file_path, schema_file_path):
    schema = xmlschema.XMLSchema(schema_file_path)
    return schema.is_valid(xml_file_path)

# text = "\\xf0\\x9f\\x98\\x82\\n\\n\\xf0\\x9f\\x8e\\xa5"
# d = "b'Video Game Fan | 19 | \\xe2\\x99\\x82| Nintendo | RPGs | Fighting Games | Etc. |'"
# print(d.encode("utf-8"))
#
# text2 = "Diving back into #Cyberpunk2077 tonight on my #Twitch. #gaming #atreaming #cyberpunk #ps4"
