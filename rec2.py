#!/usr/bin/python3
from socket import *
import sys
import select
rec_ip="127.0.0.1"
rec_port=4444
s=socket(AF_INET,SOCK_DGRAM)
s.bind((rec_ip,rec_port))

addr=(rec_ip,rec_port)
data,addr=s.recvfrom(1024)
print("Recieved file:",data.strip())
filee=open(data.strip(),'wb')

data,addr=s.recvfrom(1024)
try:
	while(data):
		filee.write(data)
		s.settimeout(2)
		data,addr=s.recvfrom(1024)
except timeout:
	filee.close()
	s.close()
	print("file downloaded")
 
