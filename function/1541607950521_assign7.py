def dictionay(n1,n2):
	if len(n1)==len(n2):
		dictionary=dict(zip(n1,n2))
		print("dictionary")
	else:
		print("list not in same length")
n1=list(input("enter the list"))
n2=list(input("enter the list"))
dictionary(n1,n2)
