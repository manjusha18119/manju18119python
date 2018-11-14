'''11. Write a program to find sum of all integers greater than 100 and less than 200 that are divisible by 7.'''
sum=0
for i in range(105,200,7):
	sum=sum+i
print(sum)
