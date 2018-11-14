def oddsum(n):
	"""function to print oddsum"""
	s=0
	for j in range(1,n):
		if(j%2!=0):
			print(j)
		s=s+j
	print("the sum is %d"%s)
	return
oddsum(50)
