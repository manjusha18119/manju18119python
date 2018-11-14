def divisible(n):
	"""function to print number divisible by five and seven"""
	for i in range(0,n):
		if(i%5==0):
			if(i%7==0):
				yield i
				i=i+1
n=input("enter the range")
a=divisible(n)
for j in range(0,n):
	print(a.next())



