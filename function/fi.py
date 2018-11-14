d=input("Enter the limit:")
a=0
b=1
if d==1:
	print("0")
elif d==2:
	print("0")
	print("1")
elif d>2:
	print("0")
	print("1")
	for i in range(d-2):
		c=a+b
		print("%d"%c)
		a=b
		b=c
else:
	print("Enter a valid number")
