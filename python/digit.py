s = input("Input a string")
d=l=0
for a in s:
if a.isdigit():
d=d+1
	elif a.isalpha():
 	l=l+1
	   	 else:
	       	 pass
		  print("Letters", l)
		  print("Digits", d)
