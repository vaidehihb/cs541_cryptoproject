#!/usr/bin/python

import MySQLdb
import csv

def getDatabase():
    # Open database connection
    db = MySQLdb.connect(host="cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com", port=3306,
                     user="student", passwd="cs336student", db="CryptoNews")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method and save the data using fetchall()
    #cursor.execute("select distinct(currency_name) from Value")
    cursor.execute("select v.currency_name, count(c.content) as frequency from cryptonews c "
                   "inner join Value v on c.content like concat('%', v.currency_name, '%') "
                   "and c.date like '%2018-02-19%' "
                   "group by v.currency_name order by frequency desc;")
    value_table = cursor.fetchall()

    '''
    cursor.execute("select * from cryptonews")
    cryptonews_table = cursor.fetchall()
    cursor.execute("select * from currency_news")
    currency_news_table = cursor.fetchall()
    '''

    # disconnect from server
    db.close()

    return value_table
