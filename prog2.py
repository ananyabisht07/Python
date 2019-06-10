import webbrowser
from googlesearch import search
f=open("glinkss",'w')
web =input("ENTER TOPIC TO SEARCH ON GOOGLE :")
topic=search(web,stop=10)
for i in topic:
	f.write(i + "\n")
webbrowser.open("https://www.google.com/search?q="+web)
