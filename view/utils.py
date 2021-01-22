def get_hashtag_from_text(text):
    hashtags = set()

    splits = text.split()

    for s in splits:
        if s.startswith("#"):
            hashtags.add(s)

    return hashtags



# text = "\\xf0\\x9f\\x98\\x82\\n\\n\\xf0\\x9f\\x8e\\xa5"
# d = "b'Video Game Fan | 19 | \\xe2\\x99\\x82| Nintendo | RPGs | Fighting Games | Etc. |'"
# print(d.encode("utf-8"))
#
# text2 = "Diving back into #Cyberpunk2077 tonight on my #Twitch. #gaming #atreaming #cyberpunk #ps4"




