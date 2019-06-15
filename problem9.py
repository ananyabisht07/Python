from collections import Counter
input_str =input("Please provide some info:")
if len(input_str) > 500:
	print("Error only 500 characters are allowed")
else:
	print(input_str)
print("Duplicate characters=")
dd=Counter(input_str)
for i in dd: 
	if dd[i]>1:
		print(i,dd[i])	
		

list1=[]
list1=list(input_str.split(" "))

count_word=Counter(list1)

dup_word=[i for i in count_word if count_word[i]>1]
dup_word.sort()
print("Duplicate words-")
for i in dup_word:
	print(i)
list2=[]
list3=[]
list2=[i for i in count_word if count_word[i]>5]
list3=[i for i in count_word if count_word[i]<6]
del list2[:]
joinedlist=list2+list3
print("After removing words coming for more then 5 times=")
for i in joinedlist:
	print(i)
print(count_word)
for i in count_word:
	if count_word[i]==1:
		new_list=[]
print(new_list)

 
