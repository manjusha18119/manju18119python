#iterate over dictionaries using a loop
dict1 = {2:3,4:6}
dict2 = {3:5,8:9}

x= iter(dict_one.item())
y= iter(dict_two.item())

for i in range(3):
x.__next__(),y.__next__()
print(dict1.next())
print(dict2.next())
