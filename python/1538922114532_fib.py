a=int(input("\nplease enter the range number:"))
first=0
second=1
for i in range(int(a)):
	if(i>=1):
		next=i
else:
	next=first+second
	first=second
	second=next
	print(next)
	i+1
