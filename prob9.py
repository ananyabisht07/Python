from collections import Counter
input_str = input("Please provide some info:")
if len(input_str) > 15:
	print("Error only 5 characters are allowed")
	sys.exit()
else:
	print(input_str)

dup_li=[y for y in input_str]
dup_li.sort()
unique=[]
dlist=[]
print(dup_li)
for ele in dup_li:
	if ele not in unique:
		unique.append(ele)
	else:
		dlist.append(ele)
print(dlist)
print(Counter(dup_li))

