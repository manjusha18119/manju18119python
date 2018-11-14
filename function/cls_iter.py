class my_class:

	#def
	def gen(self):
	
		for i in self.my_list:
			yield i
		

	def ite(self):

		iter_ele=iter(self.my_list)
		for i in range(len(self.my_list)):
			print(iter_ele.__next__())


	def read_val(self):
		a=int(input("Enter range of element:"))
		self.my_list=[input("Enter element:") for i in range(a)]

obj=my_class()
obj.read_val()
print("***generator***")
gen_obj=obj.gen()

for i in range(len(obj.my_list)):
	print(gen_obj.__next__())
print("***iterator***")
obj.ite()
