__author__ = 'asong'

from pymongo import MongoClient

client = MongoClient()

db = client['twitter']
collection = db['tweets']
collection_backup = db['tweets']

cursor = collection.find()
tweets = db.tweets

def copy_deb(new_db):
    collection_backup.find()

def remove_poison_data(poison):
    for tweet in tweets.find():

        print 'Searching for poisoned data'

        if poison in tweet['text'].lower():

            print 'Found poisoned data'
            # print tweet['text']

            collection.remove({'id': tweet['id']})

            print 'Removed poisoned data'

# poison_word = ''
# remove_poison_data(poison_word)
