# 10.Write a program to Check if the given string  is Palindrome or not.
string=input("Enter a string:")
restring=string[::-1]
if string==restring:
	print("string is palindrome")
else:
	print("string is not palindrome ")
