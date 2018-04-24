from scipy import stats
import numpy as np
from scipy.stats import kurtosis, skew
from getAPIData import CryptoCompareData, CoinMarketCapData
import csv
import time


def getSlope(volume):
    x = list(range(len(volume)))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, volume)
    return slope, intercept


start = time.time()

a = CryptoCompareData()
a.getCoinList()

currency_data = a.coinlist.head(n=500)
currency_data = currency_data[['CoinName', 'FullName', 'Id', 'Name', 'SortOrder', 'Symbol']]

# print currency_data

temp_name_list = currency_data['CoinName'].tolist()
temp_symbol_list = currency_data['Symbol'].tolist()

volume_slope_column = []
volume_intercept_column = []
standard_deviation = []
kurtosis_measure = []
skewness = []
rating = []

print "Calculating measures..."

for symbol in temp_symbol_list:
    try:
        closing_data = a.getDataByDays(currency=symbol)
        average_prices = closing_data['close'].tolist()
        volumes = closing_data['volumefrom'].tolist()

        vol_slope, vol_intercept = getSlope(volumes)
        std_dev = np.std(average_prices)
        kurto = kurtosis(average_prices)
        ske = skew(average_prices)

        # rating =

        volume_slope_column.append(vol_slope)
        volume_intercept_column.append(vol_intercept)
        standard_deviation.append(std_dev)
        kurtosis_measure.append(kurto)
        skewness.append(ske)

    except:
        print "Couldn't get data for: " + symbol
        for index, row in currency_data.iterrows():
            if row['Symbol'] == symbol:
                currency_data.drop(index, inplace=True)
        continue

currency_data['volumeSlope'] = volume_slope_column
currency_data['volumeIntercept'] = volume_intercept_column
currency_data['stdDeviation'] = standard_deviation
currency_data['kurtosis'] = kurtosis_measure
currency_data['skewness'] = skewness

print currency_data

print time.time() - start
