import requests
import json
import time
from pandas import *


class CryptoCompareData(object):
    def __init__(self, baseurl='https://min-api.cryptocompare.com/data/', params={}):
        self.baseurl = baseurl
        self.params = {'tsym': 'USD', 'toTS': time.time(), 'extraParams': 'CryptoSales'}
        self.coinlist = DataFrame()

    def callAPI(self, url):
        try:
            req = requests.get(url)
            response = req.json()
            return response
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getCoinList(self):
        try:
            url = self.baseurl + 'all/coinlist'
            response = self.callAPI(url)
            coindata = []
            for coin, details in response['Data'].iteritems():
                coindata.append(details)
            df = DataFrame(coindata)
            df.sort_values(by=['SortOrder'], ascending=[True])
            self.coinlist = df
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getDataByDays(self, days=30, aggregate=1, currency='BTC'):
        try:
            self.params['aggregate'] = aggregate
            self.params['limit'] = days
            self.toTS = int(time.time())
            self.params['fsym'] = currency
            qstring = '?allData'

            for p, value in self.params.iteritems():
                qstring += '&' + str(p) + '=' + str(value)

            url = self.baseurl + 'histoday' + qstring
            response = self.callAPI(url)
            df = DataFrame(response['Data'])
            return df
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getDataByHour(self, hours=24, aggregate=1, currency='BTC'):
        try:
            self.params['aggregate'] = aggregate
            self.params['limit'] = hours
            self.toTS = int(time.time())
            self.params['fsym'] = currency
            qstring = '?allData'

            for p, value in self.params.iteritems():
                qstring += '&' + str(p) + '=' + str(value)

            url = self.baseurl + 'histohour' + qstring
            response = self.callAPI(url)
            df = DataFrame(response['Data'])
            return df
        except:
            print "An unexpected error occurred. Data could not be fetched."


class CoinMarketCapData(object):
    def __init__(self, baseurl='https://api.coinmarketcap.com/v1/'):
        self.baseurl = baseurl
        self.data = DataFrame()
        self.globaldata = DataFrame()

    def callAPI(self, url):
        try:
            req = requests.get(url)
            response = req.json()
            return response
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getData(self):
        try:
            url = self.baseurl + 'ticker/'
            response = self.callAPI(url)
            self.data = DataFrame(response)
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getGlobalData(self):
        try:
            url = self.baseurl + 'global/'
            response = self.callAPI(url)
            self.globaldata = DataFrame(response, index=[0])
        except:
            print "An unexpected error occurred. Data could not be fetched."

    def getDataForCurrency(self, id=None):
        try:
            if id:
                df = self.data.loc[(self.data['id'] == id) | (self.data['symbol'] == id)]
                return df
        except:
            print "An unexpected error occurred. Data could not be fetched."

# if __name__ == '__main__':
#     a = CryptoCompareData()
#     a.getCoinList()
#     a.getDataByDays()
#     a.getDataByHour()
#
#     b = CoinMarketCapData()
#     b.getGlobalData()
#     b.getData()
#     df = b.getDataForCurrency('bitcoin')
