a="string"
print(a[0:4])
print(a[0:])
print(a[0:4:2])
print(a[0:5:1])
b="STRING"
print(b[-1])
print(b[-6:-1])
print(b[-1:-6])
print(b[-6:-1:2])
print(b[-6:-1:1])
print(b[-1:-6:-2])

print(b[0:])
print(b[0::])
print(b[::])
print(b[::-1])

# string concatenation
str1="Hello"
str2="python"
print(str1+' '+str2)
print(str1+str2)
# repeating operation
print(str1*2)
print(3*str2)
#member checking operator
print('y' in str1)
print('y' in str2)
print('y' not in str1)
print('y' not in str2)
