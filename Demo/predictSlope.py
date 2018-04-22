from dbConnect import getQuotes
from scipy import stats
import MySQLdb

def getSlope(currency):
    quotes = getQuotes(currency)
    quotes = [quote[1] for quote in quotes]
    x = list(range(len(quotes)))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, quotes)
    return slope, intercept


s, i = getSlope('Bitcoin')
print s, i
