s=[]
n=raw_input("Enter the string : ")
while n!="":
	s.append(n)
	n=raw_input()
a=len(s)
sum=0
for i in range(a):
	n=int(s[i])
	sum=sum+n
print("Sum of the list is : %d"%sum)

