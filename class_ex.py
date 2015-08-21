class Employee(object):
	'Common class for all Employees'
	EmpTotal = 0

	def __init__(self, name, post):
		self.name = name
		self.post = post
		Employee.EmpTotal += 1

	def GetEmpDetail(self):
		return (self.name, self.post)