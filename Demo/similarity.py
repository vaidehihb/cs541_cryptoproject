import gensim
from dbConnect import getContent, getCurrencyNames, readCurrencies
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv
import time


def createSims(content):
    gen_docs = [[w.lower() for w in word_tokenize(text)] for text in content]
    dictionary = gensim.corpora.Dictionary(gen_docs)
    print type(dictionary)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    sims = gensim.similarities.Similarity('similarity', tf_idf[corpus], num_features=len(dictionary))
    return dictionary, tf_idf, sims


def getSimilarity(query_content, dictionary, tf_idf, sims):
    query_doc = [w.lower() for w in word_tokenize(query_content)]
    query_doc_bow = dictionary.doc2bow(query_doc)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print sims[query_doc_tf_idf]


def getCurrencyPopularity(cloud=False, count=None):
    content_raw = getContent()
    content = [unicode(article[0], errors='ignore') for article in content_raw]
    currencies = readCurrencies()
    for c in currencies:
        c[0] = c[0].lower()
    gen_docs = [[w.lower() for w in word_tokenize(text)] for text in content]
    dictionary = gensim.corpora.Dictionary(currencies)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    total_currencies = [[index, 0] for index in range(len(currencies))]
    stop_words = set(stopwords.words('english'))
    # common = ['can', 'people']
    # common1 = map(lambda x: unicode(x, errors='ignore'), common)
    if not cloud:
        stop_words.add(unicode('can', errors='ignore'))
        stop_words.add(unicode('people', errors='ignore'))
        stop_words.add(unicode('crypto', errors='ignore'))
        stop_words.add(unicode('change', errors='ignore'))
        stop_words.add(unicode('data', errors='ignore'))
        stop_words.add(unicode('social', errors='ignore'))
        stop_words.add(unicode('tokens', errors='ignore'))
        stop_words.add(unicode('read', errors='ignore'))
        stop_words.add(unicode('real', errors='ignore'))
        stop_words.add(unicode('money', errors='ignore'))
        stop_words.add(unicode('version', errors='ignore'))
        stop_words.add(unicode('force', errors='ignore'))
        stop_words.add(unicode('verify', errors='ignore'))
        stop_words.add(unicode('purpose', errors='ignore'))

    for article in corpus:
        for currency in article:
            index = currency[0]
            total_currencies[index][1] += 1

    popular_currencies = [currency for currency in total_currencies if
                          currency[1] > 0 and str(currencies[currency[0]][0]).lower() not in stop_words]
    popular_currencies = sorted(popular_currencies, key=lambda x: x[1], reverse=True)
    popularity_list = []
    for currency in popular_currencies:
        popularity_list.append([currencies[currency[0]], currency[1]])
    with open('Demo/csvFiles/popularity_list.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for p in popularity_list:
            writer.writerow([p[0][0], p[1]])
    if count:
        return popularity_list[:count]
    else:
        return popularity_list


def readPopularity():
    popularity_list = []
    with open('Demo/csvFiles/popularity_list.csv', 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            popularity_list.append(row)
    return popularity_list
