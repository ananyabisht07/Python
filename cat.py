input1=input()
count=0
f=open("a",'r')
#Checking for correct command 
if input1[:3] == "rid" :			
 	if "-" == input1[4] :
#FOR NUMBER AT STARTING OF EVERY LINE			
		if 'n' == input1[5] :
			for i in f :	
				count+=1
				print(count,i)
#FOR $ AT END OF EVERY LINE
		if 'e' == input1[5] :
			for i in f :	
				print(i,"$")
#APPENDING ONE FILE TO OTHER FILE
	elif input1[4:6] == '>>' :
		for i in f :
			b=open("b",'a')
			b.write(i)
#REDIRECT OUTPUT OF A FILE TO OTHER FILE
	elif input1[4] == '>' 				
		print("a")
		b=open("b",'w')
		print("b")
		for i in f :	
			b.write(i)
	else :
		for i in f :	
			print(i)

else : 
	print("INCORRECT COMMAND")
