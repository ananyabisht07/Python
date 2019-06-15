import os
import sys
from shutil import which
command=input("Enter command=")	
while(command):
	f=open("comm.txt",'a+')
	f.write(command +"\n")
	for i in f:	
		if command==i:
			print("Dont do this again")
			command=input("Enter command=")
		elif(which(command)):
			os.system(command)
			command=input("Enter command=")
		elif(command=="exit"):
			sys.exit(0)
		else:
			print("Command Not Found....")
			command=input("Enter command=")
	
	

	
	
		

 
