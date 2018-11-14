print("student details")
id=input("enter the id")
name=input("enter the name")
d1={"id":id,"name":name}
print(d1)
gender=input("gender")
age=input("age")
d2={"gender":gender,"age":age}
print(d2)
d2.update(d1)
print(d2)

