def insertionsort(a):
	for j in range(1,len(A)):
		key = A[j]
		i = j-1
		while i>-1 & key<A[j]:
			A[i+1] - A[i]
			i = i-1
			A[i+1] = key
	return
A = list(input("enter the list"))
insertionsort(A)
print(A)
