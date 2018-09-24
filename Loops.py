# while condition:
# 	code to repeat


count = 0

while count < 5:
	print("hi!")
	count += 1

def question():
	response = input("Give me info")
	if response == "hi":
		print("a")
	elif response == "b":
		print("b")
	else:
		print("This is useless info! Try again.")
		question()

def question():
	response = input("Give me info:")
	while response != "hi" or response != "b":
		print("This is useless info! Try again.")
		response = input("Give me info: ")

	if response == "hi":
		print("a")
	elif response == "b":
		print("b")

question()

while True:

	try:
		x = int(input("Enter a number: "))
		break
	except ValueError:
		x = int(input("That's not a number! Enter a number: "))

count = 0

while count < x:
	print("Hello!")
	count += 1