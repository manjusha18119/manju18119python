a=input("enter a string")
b=":;,.[]{}()!@#$%^&*?_"
c=""
for char in a:
 if char not in b:
  c=c+char
print(c)


