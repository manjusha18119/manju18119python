list1=[1,2,3,4]
print(filter=list(filter(lambda x:x%2==0,list1)))
print(mapelements=list(map(lambda x:x**2,list1)))
print(reduceelements=reduce(lambda x,y:x+y,list1))
