#!/usr/bin/python2
import socket
import sys
rev_ip="127.0.0.1"
rev_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((rev_ip,rev_port))
s.listen(1)
conn=s.accept()
filename=input(str("Please enter the filename of the file:"))
filee=open(filename,'rb')
file_data=filee.read(1024)
conn.send(file_data)	
	
	
	
s.close()
