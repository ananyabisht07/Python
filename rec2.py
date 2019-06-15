#!/usr/bin/python3

import socket
import sys
rec_ip="127.0.0.1"
rec_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect((rec_ip,rec_port))
filename=input(str("Please enter the filename for the incoming file:"))
filee=open(filename,'wb')
file_data=s.recv(1024)
filee.write(file_data)
filee.close()
s.close()
