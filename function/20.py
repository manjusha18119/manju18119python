dict1 = {}
dict2 = {}
c=1
sum=0
while c:
	a=input("enter the keys:")
	b=input("enter the values:")
	dict1[a]=[b]
	c=input("enter 1:continue to 0:exit")
	dict2=dict1.values()
print(reduce(lambda x,y:x+y,dict1))

