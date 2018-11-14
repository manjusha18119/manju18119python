#14. Write a program to find the sum of n' Natural Numbers.
n=int(input("Enter the range of natural number:"))
sum=0
for i in range(0,n+1):
	sum=sum+i
print("sum of n' Natural Numbers:",sum)
