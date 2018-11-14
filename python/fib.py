#function to print fibanacci series
def fibnacci(a):
	n1=0
	n2=1
	count=0
	print("the fibnacci sequence is%d %d"%(n1,n2))
	for i in range(0,a):
		s=n1+n2
		n1=n2
		n2=s
		print("the fibnacci sequence is %d",s)
fibnacci(100)
