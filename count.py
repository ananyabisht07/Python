#!/usr/bin/python3
infile=open('/home/abisht/Desktop/feed.txt','r')
data=infile.read()
num_lines = len(data.splitlines())
num_words = len(data.split())
num_chars = len(data)
print(num_lines)
print(num_words)
print(num_chars)
 

