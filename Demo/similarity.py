import gensim
from dbConnect import getContent, getCurrencyNames, readCurrencies
from nltk.tokenize import word_tokenize
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


def getCurrencyPopularity(content):
    currencies = readCurrencies()
    for c in currencies:
        c[0] = c[0].lower()
    gen_docs = [[w.lower() for w in word_tokenize(text)] for text in content]
    dictionary = gensim.corpora.Dictionary(currencies)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    # print corpus
    total_currencies = [[index, 0] for index in range(len(currencies))]
    for article in corpus:
        for currency in article:
            index = currency[0]
            total_currencies[index][1] += 1
    # print total_currencies
    popular_currencies = [currency for currency in total_currencies if currency[1] > 0]
    popular_currencies = sorted(popular_currencies, key=lambda x: x[1], reverse=True)
    for currency in popular_currencies:
        print currencies[currency[0]], currency[1]
    print "Total articles: ", len(content)
    print "Total currencies: ", len(currencies)


# content_list = ["I'm taking the show on the road crypto bitcoin.", "My socks are a force multiplier.",
#                 "I am the barber who cuts everyone's hair who doesn't cut their own.",
#                 "Legend has it that the mind is a mad monkey.", "I make my own fun."]
# query = "Socks are a force for good."

start = time.time()
content = getContent()
content_list = [unicode(article[0], errors='ignore') for article in content]
end = time.time()
print "\nTime to get content: ", end - start, "\n"

query = content_list[0]

start = time.time()
getCurrencyPopularity(content_list)
end = time.time()
print "\nTime to get popular currencies: ", end - start

# dictionary, tf_idf, sims = createSims(content_list)
# getSimilarity(query, dictionary, tf_idf, sims)
