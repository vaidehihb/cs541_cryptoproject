from dbConnect import getContent, getCurrencyNames
from nltk.tokenize import word_tokenize  # to split sentences into words
from nltk.corpus import stopwords  # to get a list of stopwords
from collections import Counter  # to get words-frequency
import json


def getWordsFreq():
    # this is the list of tuples each having an article
    content = getContent()

    # split sentences into words
    words = []
    for row in content:
        text = unicode(row[0], errors='ignore')
        tokens = word_tokenize(text)
        words.extend(tokens)
    words = map(lambda x: x.lower(), words)

    # remove stopwords from our words list and also remove any word whose length is less than 4
    # stopwords are commonly occuring words like is, am, are, they, some, etc.
    stop_words = set(stopwords.words('english'))
    # common = ['can', 'people']
    # common1 = map(lambda x: unicode(x, errors='ignore'), common)
    stop_words.add(unicode('can', errors='ignore'))
    stop_words.add(unicode('people', errors='ignore'))
    # print stop_words
    words = [word for word in words if word not in stop_words and len(word) > 3]

    words_freq = Counter(words).most_common()

    words_json = [{'text': str(word[0]), 'weight': int(word[1])} for word in words_freq]
    # json.dumps is used to convert json object i.e. dictionary or list into a string
    return json.dumps(words_json)
