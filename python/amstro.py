# 15.Write a program to find whether given no. is Armstrong or not.
num = int(input("Enter a number:"))
order = len(str(num))

sum = 0

temp = num 		# find the sum of the cube of each digit
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   
   temp //= 10
   #print(sum,temp)

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
