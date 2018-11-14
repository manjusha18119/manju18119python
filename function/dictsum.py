dic={}
k=str(raw_input("Enter the key : "))
while k != "":
	v=input("Enter the value : ")
	dic[k]=v
	k=str(raw_input("Enter the key : "))
s=dic.values()
leng=len(s)
sum=0
for i in s:
	sum=sum+i

print sum
