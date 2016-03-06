#!usr/bin/env python
import sys
import os

headers = open('headers', 'r')
filename = sys.argv[1]

fileToWrite = open(filename+'.cpp', 'w')
fileToWrite.write(headers.read())
headers.close()

testKases = int(sys.argv[2])

if testKases == 1:
	contents = open('test_contents', 'r')
else:
	contents = open('contents', 'r')
	
fileToWrite.write(contents.read())

contents.close()
fileToWrite.close()
