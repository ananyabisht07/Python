#Topic: Natural Language Tool Kit 
#from nltk.corpus import stopwords
import nltk


dir(stopwords)
nltk.download('stopwords')
stopwords.words('english')


#from nltk.corpus import  stopwords
#stopwords.words()

#import requests
#dir(requests)


#accessing website from url
#webdata=requests.get('https://php.net')
#webdata #response code of http protocol
#  where 200 means url is ok
#  302 means url redirected
#  404 means url not found
#  505 means server is not permitting web scraping
# now getting actual data  of any website or url
#htmldata=webdata.text
#parser means extracting data on behalf of some tag
#htmldata
#importing bs4
#from bs4 import BeautifulSoup
#soup=BeautifulSoup(htmldata,'html5lib')
#htmldata  , parser
#type(soup)
bs4.BeautifulSoup
#finding all data
#clean_data=soup.get_text()
#type(clean_data)
str
#print(clean_data)
#saving data permanently
#with open('mywebdata.txt','w+') as f:
 # f.write(clean_data)
#reading from file
f=open('mywebdata.txt','r')
mydata=f.read()
f.close()
type(mydata)
str
#split
#mydata.split() #split all string by \n new line
import time
for i in mydata.split():
  print(i)
  time.sleep(1)
