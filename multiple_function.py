def name(name ,age=22):
	print "welcome", name, "My age is ", age

def user_input():
	a = raw_input("Enter your name: ")
	return a

b = user_input()

name(b)