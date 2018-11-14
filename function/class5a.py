class Shape:
	def area1(self,a):
		area=0
		print("shapes area is %d"%area)

class Square(Shape):
	def __init__(self,length):
		self.length=input("enter the length")
	def area(self,a):
		a=self.length**2
		print("area of the square is %d"%a)
obj=Square(3)
obj.area(1)
obj=Shape()
obj.area1(0)
		
