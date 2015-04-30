import sys
import re
import pandas
from pymongo import MongoClient

from ui import gui

# Determine if tweet mentions a programming language using regular expression
def find_proglangs(tweet, lang):
    php_filter = re.compile("[\b\s|#]php")
    java_filter = re.compile("[\b\s|#]java[\s|\n|\t]")
    javascript_filter = re.compile("[\b\s|#]javascript")
    cplusplus_filter = re.compile("[\b\s|#]cplusplus|c\+\+")
    csharp_filter = re.compile("[\b\s|#]csharp|c\#")
    python_filter = re.compile("[\b\s|#]python")

    # Check tweets to see if they mention a programming language
    if lang is 'java' and java_filter.search(tweet.lower()):
        return True
    if lang is 'php' and php_filter.search(tweet.lower()):
        return True
    if lang is 'javascript' and javascript_filter.search(tweet.lower()):
        return True
    if lang is 'cplusplus' and cplusplus_filter.search(tweet.lower()):
        return True
    if lang is 'csharp' and csharp_filter.search(tweet.lower()):
        return True
    if lang is 'python' and python_filter.search(tweet.lower()):
        return True
    else:
        return False

# Create columns in dataframe to hold boolean values for each language
def add_proglangs(list):

    list['java'] = list['text'].apply(lambda tweet: find_proglangs(tweet, 'java'))
    list['javascript'] = list['text'].apply(lambda tweet: find_proglangs(tweet, 'javascript'))
    list['php'] = list['text'].apply(lambda tweet: find_proglangs(tweet, 'php'))
    list['cplusplus'] = list['text'].apply(lambda tweet: find_proglangs(tweet, 'cplusplus'))
    list['csharp'] = list['text'].apply(lambda tweet: find_proglangs(tweet, 'csharp'))
    list['python'] = list['text'].apply(lambda tweet:find_proglangs(tweet, 'python'))

def main():
    client = MongoClient()

    db = client.twitter
    coll = db.tweets

    cursor = coll.find()

    tweets_list = pandas.DataFrame()

    tweets_list['text'] = map(lambda tweet: tweet.get('text'), cursor)

    # Determine tweet mentions
    add_proglangs(tweets_list)

    # GUI
    app = gui.QApplication(sys.argv)
    form = gui.AppForm(tweets_list)
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()