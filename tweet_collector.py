import tweepy
import pymongo
import json
import re

# Handles data obtained from stream
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        line = json.loads(data)
        if filter_lang(line):
            save_to_db(line)
            print line.get('text')
        return True

    def on_error(self, status):
        print status

# Save the data into MongoDB
def save_to_db(data):
    client = pymongo.MongoClient()

    db = client['twitter']
    coll = db['tweets']

    return coll.insert(data)

# Filter the results from the data
def filter_lang(line):

    if 'text' in line:
        tweet_text = line.get('text', '').lower()

    if 'entities' in line:
        tweet_tags = line.get('entities').get('hashtags', '')

    lang_filter = re.compile("[\b\s|#](php|javascript|java|cplusplus|c\+\+|csharp|c\#|python)")
    java_filter = re.compile("java production")
    python_filter = re.compile("monty[\b\s]")

    if line.get('lang', '') == 'en':
        if lang_filter.search(tweet_text) and not java_filter.search(tweet_text)\
                and not python_filter.search(tweet_text):
            return True

        else:
            for w in tweet_tags:
                    if lang_filter.search(w.get('text', '').lower()):
                        return True

# Setup the stream and gather tweets
def gather():
    # Oauth keys and tokens
    consumer_key = 'dDo9CZIe48EXcuF58zBnxLbfL'
    consumer_secret = 'aNMZStruSxTDCTclxsAMESet4bdh4KtuTOsX5UMGdRyW3oJrIZ'
    access_token = '1494797575-RFndPghcnTsTfaBBiJDUka899NukpsPEcbFbn4A'
    access_secret = 'bK6ec6eJ2KkqEwGefQp5AjSzb9zQQg24IJuQvgH8eN3FT'

    listener = StdOutListener()

    # Establish OAuth connection
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    # Create stream
    # api = tweepy.API(auth)
    stream = tweepy.streaming.Stream(auth, listener)
    stream.filter(track=['java', 'python', 'cplusplus', 'c\+\+', 'csharp', 'c\#', 'javascript', 'php'])

gather()