#!/usr/bin/python

import MySQLdb
import csv


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
    with open('list.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for c in currencies:
            writer.writerow(c)
    return currencies


def getContent():
    db = MySQLdb.connect(host="cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com", port=3306,
                         user="student", passwd="cs336student", db="CryptoNews")
    cursor = db.cursor()
    cursor.execute("select distinct(content) from cryptonews where date like '%2018-03-12%';")
    content = cursor.fetchall()
    db.close()
    return content

def readCurrencies():
    currencies = []
    with open('list.csv', 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            currencies.append(row)
    return currencies


def getDomains(c_name):
    db = MySQLdb.connect(host="cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com", port=3306,
                         user="student", passwd="cs336student", db="CryptoNews")
    cursor = db.cursor()
    cursor.execute(
        "SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(link, '/', 3), '://', -1), '/', 1), '?', 1),'www.',-2) as domain, count(*) as frequency from cryptonews where content like %s group by domain order by frequency desc",
        ("%" + str(c_name) + "%",))
    domains = cursor.fetchall()
    # print domains
    db.close()
    return domains

readCurrencies()