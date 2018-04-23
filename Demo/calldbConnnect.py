from dbConnect import getCurrencyNames
import csv

value_table = getCurrencyNames()
c = csv.writer(open("Demo/csvFiles/temp.csv", "wb"))
for row in value_table:
    c.writerow(row)
    print row
