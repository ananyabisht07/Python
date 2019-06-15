import webbrowser
from googlesearch import search
import pyqrcode
from pyqrcode import QRCode

f=open("glinks",'w')
web =input("ENTER TOPIC TO SEARCH ON GOOGLE :")
url_list=[]
for i in search(web,tld="co.in",lang="eng",num=3,start=0,stop=3,pause=2):
	url_list.append(i)
	print(i)
	url=pyqrcode.create(i)
	url.svg("myqr{}.svg",scale=8)
webbrowser.open("https://www.google.com/search?q="+web)

