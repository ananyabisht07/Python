import os
import sys
from shutil import which
command=input("Enter command=")
f=open("comm.txt",'a+')
f.write(command +"\n")
print("1")	
while(command):
	for i in f:
		print("2")	
		if(which(command)):
			os.system(command)
			command=input("Enter command=")
		elif(command=="exit"):
			sys.exit(0)
			command=input("Enter command=")
		elif command==i:
			print("Dont do this again")	
			command=input("Enter command=")
		else:
			print("Command Not Found....")
			command=input("Enter command=")
	
	

	
	
		

