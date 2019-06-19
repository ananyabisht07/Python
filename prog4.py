
#!usr/bin/python3
import os
import crypt
count=0
a=input("Enter the input=")
abc=list(a)
for i in abc:
	if i.isdigit():
		count=1
if count==0:
	par="hello"+a
	encPass=crypt.crypt(par,"22")
	os.system("useradd -m -p" + encPass +" "+a)
