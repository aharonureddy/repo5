class Employee:
	_count=0 # class variable
	def __init__(self, name, eid):
		self.name=name
		self.eid=eid
		Employee._count+=1
	def get_id(self):
		print(self.eid)
	@classmethod
	def get_emp_count(cls):
		print(cls._count)
	@staticmethod	
	def compute_tax(basic):
		print(basic * 0.3)


Employee.get_emp_count()
ramesh = Employee("Ramesh S",223)
ravi = Employee("Ravi S",224)
ramesh.get_id()
Employee.get_emp_count()

Employee.compute_tax(20000)
ramesh.compute_tax(20000)

