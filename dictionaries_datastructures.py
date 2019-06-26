#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:27:53 2019

@author: trejimmy5562
"""
import pprint

#create a cat object to hold dictionary values of cats
cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}
allCats = []
allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
allCats.append({'name': 'Fatty', 'age': 5, 'color': 'gray'})
print(allCats)

#Tic Tac Toe board game

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }
pprint.pprint(theBoard)

theBoard['mid-M'] = 'X'
pprint.pprint(theBoard)

#this dictionary is a datastructure for an actual tic tac toe
#board, it is not an actual representation, however rep.s
#all of the values necessary and can easily be tweaked into a
#game board

#function to create board
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

#pass our board to the function to print it;
printBoard(theBoard)

#find the type of data you are dealing with (datatype of variable)
type(theBoard) #this is a dictionary value


