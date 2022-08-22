# multiple inheritance

class Cat:
	def speak(self):
		print("meau..meau")
	def likes(self):
		print("milk")

class Dog:
	def speak(self):
		print("bhou..bhou")
	def likes(self):
		print("bones")



class Doat(Cat, Dog):
	def speak(self):
		print("bhou..meau")

ginger = Doat()

ginger.speak()
ginger.likes()