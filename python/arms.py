n=input("enter the value")
t=n
sum=0
while t>0:
	digit=t%10
        print(t)
	sum=(sum+digit**3)
	t//=10
if n==sum:
	print(n,"is an armstrong number")
else:
	print(n,"not an armstrong number")
