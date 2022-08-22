# Inheritance

class Employee:
	def __init__(self, name, eid):
		self.name=name
		self.eid=eid

	def get_id(self):
		print(self.eid)
	

ramesh = Employee("Ramesh S",223)
ramesh.get_id()

class Manager(Employee):
	def set_team(self,teamname):
		self.teamname = teamname

swapna = Manager("Swapna", 225)

swapna.get_id()

swapna.set_team("R & D")
