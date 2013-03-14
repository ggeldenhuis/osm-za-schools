#!/usr/bin/python

import re
import csv
import pprint

# data/Masterlist_2012_Q4_Ordinary_Schools.csv

def printdata():
#  with open('data/Masterlist_2012_Q4_Ordinary_Schools.csv', 'rb') as csvfile:
  with open('../data/short.example.data', 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',',quotechar='"')
#    print datareader.fieldnames()
#    print type(datareader)
 
#    pp = pprint.PrettyPrinter(indent=2)
#    pp.pprint(datareader)
    for row in datareader:
      for item in row:
        print item
#      print type(row)
#      print row
#      pp.pprint(row)

def main():
  printdata()

if __name__ == '__main__':
  main()


#>>> with open('eggs.csv', 'rb') as csvfile:
#...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#...     for row in spamreader:
#...         print ', '.join(row)
#Spam, Spam, Spam, Spam, Spam, Baked Beans
#Spam, Lovely Spam, Wonderful Spam
