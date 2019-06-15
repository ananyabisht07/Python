#!/usr/bin/python2

import socket
import sys
rec_ip="127.0.0.1"
rec_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((rec_ip,rec_port))

while 4 > 2:
	data=s.recvfrom(150)
	if data[0]=="exit":
		sys.exit(0)
	else:
		print("Message from sender:",data[0])
		print("IP and Port Number:",data[1])
	reply=raw_input("Reply:")
	if len(reply) > 15:
		print("Error:Length recieved of data must be smaller then 150")
		reply=raw_input("Reply:")
	elif reply=="exit":
		sys.exit(0)
	else: 
		s.sendto(reply,data[1])
s.close()
