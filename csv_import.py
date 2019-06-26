#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:49:02 2019

@author: trejimmy5562
"""

import csv


#open csv file and make a table object to hold it
csvfile = open('Book1.csv', 'r')
Table = csv.reader(csvfile)
#we will take the data from the csv and put it into the 'data' variable
data = []
#x = 0
for row in Table:
    print(row[0])
    data.append(row[0])
    #x = x + 1
    
#check that it worked by checking length
print(len(data))




#close the csv
csvfile.close()
