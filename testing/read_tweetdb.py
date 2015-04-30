from pymongo import MongoClient
import pprint

client = MongoClient()

db = client['twitter']
collection = db['tweets']

cursor = collection.find()
tweets = db.tweets

def tweet_count():
    print tweets.find().count()

def get_db_details():
    print collection.name()

def get_hashtags():
    for tweet in cursor:
        print tweet['entities']['hashtags']
        print ''

def get_tweet():
    for tweet in tweets.find_one():
        pprint.pprint(tweet)

get_hashtags()