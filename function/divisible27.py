upper=int(input("Enter the range:"))
lower=int(input("Enter the range:"))
for i in range (upper,lower+1):
    if(i%2==0 and i%5==0):
        print(i)
