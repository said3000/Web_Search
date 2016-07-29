#!/usr/bin/python 
import sys
import urllib2
import re
import time
import logging
import datetime
import Web_Search
import os

# from Web_Search import myClass

filePath = "input.txt"

# Search for the user input
file = open('urls.txt', 'r').readlines()
lines = []

# Read every line of a file 
for line in file: 
	# The rstrip method gets rid of the "\n" at the end of each line
	lines.append(line.rstrip())
print(lines)

# theWebsite = req.read()

# Use define time interval to 'ping' the url periodically
max_time = int(raw_input('Enter the amount of seconds you want to run this: '))

# The start time of execution
start_time = time.time()

webSearch = Web_Search.myClass()

logFile = open("Log_file.log", "w")
logFile.close()

mytable = open("workbook.xlsx", "w")
mytable.close()

file = open(filePath)
wordList = []
for line in file:
	for word in line.split():
		webSearch.myMethod(word, lines, None)
		wordList.append(word)
	# for word in wordList:
file.close()