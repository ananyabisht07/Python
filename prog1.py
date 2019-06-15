import datetime
name=input("Enter the name:")
age=input("Enter age:")
cur_date=datetime.datetime.now()
ye=cur_date.year
tot=95-int(age)
print("The year in which the person turns out 95 will be:",int(tot)+int(ye)) 
