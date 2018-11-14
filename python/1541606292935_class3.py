class Radius:
	def __init__(self,radius):
		self.radius=input("enter the radius")
	def Area(self):
		area=self.radius**2*3.14
		print("area of circle is%d"%area)
obj = Radius(4)
obj.Area
