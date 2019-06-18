#!/usr/bin/python2
#sender
from socket import *
import sys
rev_ip="127.0.0.1"
rev_port=4444

s=socket(AF_INET,SOCK_DGRAM)
addr=(rev_ip,rev_port)

filename=sys.argv[1]
s.sendto(filename,addr)
filee=open(filename,'rb')
file_data=filee.read(1024)
while(file_data):
	if(s.sendto(file_data,addr)):
		print("sending....")
		file_data=filee.read(1024)
	
s.close()
filee.close()
