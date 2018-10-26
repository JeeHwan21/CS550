import random as r

class Bank:

	def __init__(self, name):
		self.name = name
		self.number = r.randint(0, 1000)
		self.money = 0

	def add(self, add):
		self.money += add

	def take(self, take):
		if 0 <= take <= self.money:
			self.money -= take
		else:
			print("You do not have enough money in your bank account!")

	def close(self):


name1 = input("Hi, what's your name?")

func = int(input("Hi " + +name1+ + ", would you like to create a bank account?\n1) YES\n2) NO"))

if func == 1:
	Bank(name1)
else:
	print("Have a great day!")