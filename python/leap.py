#3.Write a program to  Determine If Year Is Leap Year
year=int(input("Please Enter the Year: "))
if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)
