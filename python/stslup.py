string="hello python"
print(string)

print(string[0:3].upper()+string[3:7]+string[7:9].upper()+string[9:10]+string[10:11].upper()+string[11:12])
print(len(string))	#Retruns length of the given string.
print(string.upper())	#Converts string to uppercase.
print(string.lower())
print(string.startswith('he'))	#Returns True if string starts with given substring.
print(string.startswith('on'))
print(string.endswith('he'))	#Returns True if string endswith given substring.
print(string.endswith('on'))
result=string.count('o')	#Returns the count of given substring.
print(result)
print(string.capitalize())	#Capitalize the first letter of the string.
print(string.title())		#Capitalizefirst letter of each word in the given string.
print(string.strip('h'))	#Removes any character from both ends of the string.
print(string.strip('n'))
print(string.lstrip('h'))	#Removes any character from the left end of the string.
print(string.rstrip('n'))	#Removes any character from the right end of the string.
print(string.split('o'))	#To split the string
print(string.replace('h','e'))	#To replace a string with given substring.
print(string)
# print(del string[0])	
