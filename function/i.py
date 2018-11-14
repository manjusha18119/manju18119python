def even(n):
	for i in range(0,n):
		if(i%2==0):
			#yield i
			#i=i+1
			l=[]
			l.append(i)
			#print(l)
			a=iter(l)


n=input("enter the range")


a=even(n)


for j in range(0,n):
	print(a.next())
