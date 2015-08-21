def add(a, b):
	return a+b

def sub(a,b):
	return a-b

def mul(a, b):
	return a*b

def div(a, b):
	return a/b

def pow(a, b):
	return a**b

def calc():
	a = int(raw_input("Enter first number: "))
	b = int(raw_input("Entee second number: "))

	print 'power: '+str(pow(a, b))
	print 'sumation: '+ str(add(a, b))
	print 'substraction: '+ str(sub(a,b))
	print 'multiplication: '+str(mul(a, b))
	print 'division: '+ str(div(a,b))

calc()
