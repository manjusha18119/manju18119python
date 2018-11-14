str = []
num = int(input("how many numbers:"))
for n in range(num):
	numbers = int(input("enter the number:"))
	lst.append(numbers)
print("largest number in the list is :",large(lst),"smallest element in the list is :",small(lst))
