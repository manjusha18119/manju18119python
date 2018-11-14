my_list = []
my_list
my_list = [4,5,6,7,8]
my_list
my_list = [4,5,6,"hello",'world']
my_list
list1
['physics', 'chemistry', 1997, 2000]

# delete element on the 2nd position
>>> del list1[2]
>>> list1
['physics', 'chemistry', 2000]

#delete the entire list
>>> del list1
>>> list1
# updating the 2nd  element 
>>> list1 = [12,34,56,90]
>>>list1
[12,34,56,90]
>>>list1[1] = 24
>>>list1
[12,24,56,90]

# add new element to the list
>>>list1[4] = 84
>>>list1
[12,24,56,90,84]
>>> list1 = ["python","java","c#","android","ios"]
>>> list1
['python', 'java', 'c#', 'android', 'ios']

# Assignment operator =

>>> list1[2] = '.NET'
>>> list1
['python', 'java', '.NET', 'android', 'ios']

#Eg: in and not in operator
>>> 'c++' not in list1
True
>>> 'c++' in list1
False
>>> 

#Concatenation opertaor
>>> my_list
['python', 123]
>>> my_list+my_list
['python', 123, 'python', 123]
>>> 

#Repetition opertaor
>>> my_list*2
['python', 123, 'python', 123]
