import datetime
name=input('Enter your name=')
now = datetime.datetime.now()
t=now.strftime("%Y-%m-%d %H:%M:%S")
hr=t[11:13]
if hr>='20':
	print("Gud night")
elif '15'<hr<'21':
	print("Good Evening")
elif '11'<hr<'16':
	print("Good afternoon")
else:
	print("Good Morning!!")





