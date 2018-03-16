from dbConnect import getDatabase
import csv

value_table = getDatabase()
c = csv.writer(open("temp.csv","wb"))
for row in value_table:
    c.writerow(row)
    #print row
