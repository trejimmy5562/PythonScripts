#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:33:26 2019

@author: trejimmy5562
"""
import pprint
#Dictionary Data Type
#index for dic is called a key
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')
#dictionaries also have no order, not like a list,
# order doesnt matter only key
#boolean;
'disposition' in myCat
#different values/keys in the dictionary
print(list(myCat.keys()))
print(list(myCat.values()))
#both;
print(list(myCat.items()))

for k in myCat.keys():
    print(k)

for v in myCat.values():
    print(v)

for k, v in myCat.items():
    print(k, v)
#instead of if, we can use get
#if key does not exist, defaults to second value
print(myCat.get('color', 0))
print(myCat.get('age', '--'))
#opposite of get
#this if statement does the same as setdefault
if 'age' not in myCat:
    myCat['age'] = 'black'


myCat.setdefault('poop', 'red')

for k, v in myCat.items():
    print(k, v)
    
#----------------#
message = 'It was a bright cold day in April, and the clocks were striking thirteem.'

count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
#this prints dictionaries prettily
pprint.pprint(count)






