n=input("enter no =")
if n==0:
	print 1
fact=1
if n>0:
	for i in range(n,0,-1):
		fact=fact*i
	print fact
