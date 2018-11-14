# Python's program to iterating over dictionaries using 'for' loops
 
x = {'z': 10, 'l': 50, 'c': 74, 'm': 12, 'f': 44, 'g': 19}
 
for key, val in x.items():
    print(key, "=>", val)
 
print("\n------------------------\n")
 
for key in x:
    print(key, "=>", x[key])
 
print("\n------------------------\n")
for key in x.keys():
    print(key, "=>", x[key])
 
print("\n------------------------\n")
for val in x.values():
    print(val)
