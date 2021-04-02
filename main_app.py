from pymongo import MongoClient
from hashtag_search import getHashtag_Media_by
import json

uri = "mongodb+srv://mohssine_toor:R553MicmK@cluster0.xwrme.mongodb.net/IG_posts?retryWrites=true&w=majority"
client = MongoClient(uri) # Use the mongodb python client

db = client["IG_posts"] # Connect to the database
collection = db["posts"] # Get access to the posts collection

##################Get All posts linked to a hashtag ##########################
hashtags = ["ripjacqueschirac", "mortjacqueschirac", "ripchirac"] #hashtags to search for
media_types = ["top_media", "recent_media"]# type of retrieved data
for hashtag in hashtags:
    for media_type in media_types:
        response = getHashtag_Media_by(hashtag, media_type)# hit the api for some posts!
        try:
            collection.insert_many(response)# insert the data to the database
        except:
            print("error")
