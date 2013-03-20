#!/usr/bin/python

import re
import csv
import pprint

# data/Masterlist_2012_Q4_Ordinary_Schools.csv

def printdata():
  csv_file = csv.DictReader(open('../data/short.example.data', 'rb'), delimiter=',', quotechar='"')
  for line in csv_file:
    row_being_build = ''
    row_being_build += line['NatEmis']+','
    row_being_build += line['EmisNo']+','
    row_being_build += line['Institution']+','# fix name 
    row_being_build += line['PaypointNo']+','
    row_being_build += line['ExamNo']+','
    row_being_build += line['ExamCentre']+','# make boolean
    row_being_build += line['GIS_Long']+','
    row_being_build += line['GIS_Lat']+','
    row_being_build += line['NoFeeSchool']+','
    print 'empty',line['Snap_Learners_2007']
    # some years have empty data.
    # average should only for years with data

#    average_students = int(line['Snap_Learners_2007']) + int(line['Snap_Learners_2008'])
#    print average_students/2
#    print row_being_build   

def main():
  printdata()

if __name__ == '__main__':
  main()
