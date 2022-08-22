class Dog:
	def __init__(self,color, breed):
		self.color = color
		self.breed = breed
	def speak(self):
		print("bhou..bhou")
	def guard(self):
		print("I am guarding your home")
	def fetch(self,item):
		print(f"I am fetching your {item}")
	def hi(self):
		print(f"Hello I am a {self.color} {self.breed}")

tommy = Dog("brown","lab")

print(type(tommy))
print(isinstance(tommy, Dog))

tommy.speak()
tommy.guard()
print(tommy.color)
print(tommy.breed)
tommy.fetch('ball')
tommy.hi()

lucy = Dog("black","minpin")
lucy.hi()