import pyttsx3
import datetime
def fun1(name):
	now = datetime.datetime.now()	
	t=now.strftime("%Y-%m-%d %H:%M:%S")	
	hr=t[11:13]
	if hr>='20':
		speech=pyttsx3.init()
		speech.say(name + "Good Night")	
		speech.runAndWait()	
	elif '15'<hr<'21':
		speech=pyttsx3.init()
		speech.say("Good evening" + name)
		speech.runAndWait()		
	elif '11'<hr<'16':
		speech=pyttsx3.init()
		speech.say("Good Afternoon")
		speech.runAndWait()
	else:
		speech=pyttsx3.init()		
		speech.say("Good Morning")
		speech.runAndWait()
def add():
	input_string=[int(x) for x in input("Enter Numbers:").split()]
	sum=0	
	for i in input_string:
		sum=sum+i
	print("sum=",sum)
def sort():
	input_string=[int(x) for x in input("Enter Numbers:").split()]
	input_string.sort()
	for i in input_string:
		print(i)
def mod():
	print(help("modules"))

name=input("Enter name=")
fun1(name)
print("1-Add Numbers")
print("2-Sort Numbers")
print("3-Print number of modules installed")
choice=input("Enter your choice=")
if choice=='1':
	add()
elif choice=='2':
	sort()
else:
	mod()	









