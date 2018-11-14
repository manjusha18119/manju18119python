dic={}
k=str(raw_input("Enter the key : "))
while k != "":
	v=input("Enter the value : ")
	dic[k]=v
	k=str(raw_input("Enter the key : "))
s=dic.values()
d=dic.keys()
leng=len(s)
for i in range (leng):
	print "%s is a %s"%(d[i],s[i])
