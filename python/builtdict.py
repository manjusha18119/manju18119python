d={}
n=raw_input("Enter the key :")
while n!="":
	a=raw_input("Enter the value")
	d[n]=a
	n=raw_input("Enter the key")
print("dictionary")
print(d)
l=len(d)
print("The length of the dictionary is %d"%l)

print("Enter 2nd dictionary")
d2={}
n=raw_input("Enter the key :")
while n!="":
	a=raw_input("Enter the value : ")
	d2[n]=a
	n=raw_input("Enter the key : ")

print("The dictionary is...")
print(d2)

print(cmp(d,d2))

print("The string representation :")
print(str(d))

n=input("Enter the key to check in dictionary 1 :")
print(d.has_key(n))

print("The list of items :")
print(d.items())

print("The list ok key : ")
print(d.keys())

print("The list ok values : ")
print(d.values())

d.clear()

