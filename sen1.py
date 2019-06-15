#!/usr/bin/python2
import socket
import sys
rev_ip="127.0.0.1"
rev_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 2 > 1 :
	msg=raw_input("Enter message:")
	if len(msg) > 15:
		print("Error:Length recieved of data must be smaller then 150")
	elif msg=="exit":
		s.sendto(msg,(rev_ip,rev_port))
		sys.exit(0)
	else: 
		s.sendto(msg,(rev_ip,rev_port))
print(s.recvfrom(150))
	
s.close()
