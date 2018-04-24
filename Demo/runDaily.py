from dbConnect import getCurrencyNames, getContent
from similarity import getCurrencyPopularity

print 'getting the list of currencies...'
getCurrencyNames()
print 'getting the content...'
getContent()
print 'getting the currency popularity...'
getCurrencyPopularity()
