class Shape:
	def area(self,a):
		area=0
		print("shape area is %d",area)
class Square(Shape):
	def __init__(self,length):
		self.length=input("enter the length")
	def area(self,a):
		a=self.length**2
		print("area of square is %d"%a)
obj=Square(3)
obj.area(1)
obj=Shape(2)
obj.area1(2)
