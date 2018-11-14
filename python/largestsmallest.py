b=list(input("Enter the elements : "))
n=len(b)
#a=list(b)
small=b[0]
for i in range(n):
	small=b[i]
	for j in range(i,n):
		if(b[j]<small):
			temp=small
			small=b[j]
			b[j]=temp
	b[i]=small
print ("The smallest element is : %d\nThe largest element is : %d "%(b[0],b[n-1]))
				




