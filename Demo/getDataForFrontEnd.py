from pandas import *
import csv

class getFrontEndData(object):
    def __init__(self, filepath = "Demo/csvFiles/currency_data.csv"):
        self.filepath = filepath
        self.data = DataFrame()

    def readFile(self):
        try:

        except IOError:
            print "Could not read file at:", self.filepath
        except:
            print "An unexpected error occured. The request could not be completed."
