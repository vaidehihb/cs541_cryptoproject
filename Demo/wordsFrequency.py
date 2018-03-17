from dbConnect import getContent
from nltk.tokenize import word_tokenize  # to split sentences into words
from nltk.corpus import stopwords  # to get a list of stopwords
from collections import Counter  # to get words-frequency

# this is the list of tuples each having an article
content = getContent()

# split sentences into words
words = []
for row in content:
    text = unicode(row[0], errors='ignore')
    tokens = word_tokenize(text)
    words.extend(tokens)

# remove stopwords from our words list and also remove any word whose length is less than 3
# stopwords are commonly occuring words like is, am, are, they, some, etc.
stop_words = set(stopwords.words('english'))
words = [word for word in words if word not in stop_words and len(word) > 2]

# now, get the words and their frequency
words_freq = Counter(words)
print len(words_freq)
