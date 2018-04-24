from scipy import stats
import numpy as np
from scipy.stats import kurtosis, skew
from getAPIData import CryptoCompareData, CoinMarketCapData
from similarity import readPopularity


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


# def getRating(currencies_list):
#     popularity = getCurrencyPopularity()
#     print popularity[0:20]


a = CryptoCompareData()
a.getCoinList()
currency_list = a.coinlist.head(n=10)
currency_list = currency_list[['SortOrder', 'Name', 'CoinName', 'FullName', 'Id', 'Symbol', 'TotalCoinSupply']]
# currency_list = currency_list.head(n=10)
print currency_list
# print data_by_days['close'].tolist()
# a.getDataByHour()
