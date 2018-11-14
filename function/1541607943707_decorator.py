#decorator divide by 0
def divi(p):
	def inner(a,b):
		if b==0:
			print("division not posssible")
		else: p(a,b)
	return inner
@divi
def divide(a,b):
	return a/b
print(divide(20,0))
