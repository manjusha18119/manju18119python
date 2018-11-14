def input1(string):
	
	len1=[i for i in string if i not in vowel]
	
	print(" ".join(len1))	
string=input("enter the string")
vowel="aeiou"
input1(string)

