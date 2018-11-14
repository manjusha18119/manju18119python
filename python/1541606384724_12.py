#generator to print the even numbers between 0 and n in comma 
def even(n):
	i=1
	for i in range(0,n):
		if(i%2==0):
			yield i
		i=i+1
n=input("enter the range")
a=even(n)
for j in range(0,n):
	print(a.next())
