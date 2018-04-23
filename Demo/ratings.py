from dbConnect import getQuotes
from scipy import stats
import numpy as np
from scipy.stats import kurtosis, skew
from similarity import getCurrencyPopularity


def getSlope(volume):
    # quotes = getQuotes(currency)
    # quotes = [quote[1] for quote in quotes]
    x = list(range(len(volume)))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, volume)
    return slope, intercept


def getStd(quotes):
    return np.std(quotes)


def getKurtosis(quotes):
    return kurtosis(quotes)


def getSkew(quotes):
    return skew(quotes)


def getRating():
    popularity = getCurrencyPopularity()
    print popularity[0:20]


getRating()

# s, i = getSlope('Bitcoin')
# print s, i
