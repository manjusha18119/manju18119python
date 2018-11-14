#5.Write a program to print the fibonocci series.
ra=int(input("Enter the range of fibanocci series:"))
a=0	# assign first value
b=1	`# assign second value
for i in range(ra):
	if i<=1:
		c=i
	else:
		c=a+b
		a=b
		b=c
	print(c)
	
