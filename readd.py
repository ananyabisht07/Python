import webbrowser
from googlesearch import search
f=open("glinks",'w')
web =input("ENTER TOPIC TO SEARCH ON GOOGLE :")
topic=search(web,stop=3)
for i in topic:
	f.write(i + "\n")
webbrowser.open("https://www.google.com/search?q="+web)
s=open("glinks",'r')
data=s.read()
print(data)
