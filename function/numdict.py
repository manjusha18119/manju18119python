count=0
number=0
s=[]
n=raw_input("Enter the string : ")
while n!="":
	s.append(n)
	n=raw_input()
a=s[0]
for i in a:
	if i.isalpha():
		count=count+1
	elif i.isdigit():
		number=number+1
print("The number of letters : %d  \nThe number of digits : %d"%(count,number))
	
	
