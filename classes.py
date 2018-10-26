# PROPERTIES, METHODS
# No printing out, No asking for input
#self is just within the class

class Dog:

# Singular, Upper Case

	# constructor
	# initializes properties and sets up the dog object

	def __init__(self, name, hunger):
		self.hunger = hunger
		# 1 very hungry, 10 very full
		self.energy = 5
		# 1 very tired, 10 full of energy
		self.name = name

	# methods / functions

	def eat(self):
			if self.hunger < 10:
				self.hunger += 1
				self.energy += 1
				status = self.name+" just ate a delicious meal!"
			else:
				status = self.name+" refused to eat because he is full!"
			return status

	# def walk(self):


	def stats(self):
		return "Name: "+self.name+"\nEnergy: "+str(self.energy)+"\nHunger: "+str(self.hunger)+""

dogname1 = input("What do you want to name you dog? ")

dog1 = Dog(dogname1, 6)
dog2 = Dog("Coco", 2)

while True:
	print(dog1.stats())
	print(dog2.stats())

	choice = input("What do you want to do?")

	if choice == "eat":
		print(dog1.eat())
		print(dog2.eat())
	else:
		print("Can't do that.")