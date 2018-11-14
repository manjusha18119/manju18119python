def bubblesort(a):
	n = len(a)
	for i in range(n):
		for j in range(n-i-1):
			if a[j] > a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]
a = list(input("enter the array"))
bubblesort(a)
print("sorted array is:")
for i in range(len(a)):
	print(a[i])
 
                                                                                                                                                           
