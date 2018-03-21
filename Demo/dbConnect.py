#!/usr/bin/python

import MySQLdb


def getCurrencyNames():
    # Open database connection
    db = MySQLdb.connect(host="cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com", port=3306,
                         user="student", passwd="cs336student", db="CryptoNews")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method and save the data using fetchall()
    cursor.execute("select distinct(currency_name) from Value")
    currencies = cursor.fetchall()
    # disconnect from server
    db.close()
    return currencies


def getContent():
    db = MySQLdb.connect(host="cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com", port=3306,
                         user="student", passwd="cs336student", db="CryptoNews")
    cursor = db.cursor()
    cursor.execute("select distinct(content) from cryptonews where date like '%2018-03-13%';")
    content = cursor.fetchall()
    db.close()
    return content

def getDomains(c_name):
    db = MySQLdb.connect(host="cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com", port=3306,
                         user="student", passwd="cs336student", db="CryptoNews")
    cursor = db.cursor()
    query = "SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(link, '/', 3), '://', -1), '/', 1), '?', 1),'www.',-2) as domain, count(*) as frequency from cryptonews where content like %s group by domain order by frequency desc"
    cursor.execute("SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(link, '/', 3), '://', -1), '/', 1), '?', 1),'www.',-2) as domain, count(*) as frequency from cryptonews where content like %s group by domain order by frequency desc", ("%" + str(c_name) + "%",))
    domains = cursor.fetchall()
    # print domains
    db.close()
    return domains

