# Functions: reusability, less error checking, self-explanatory name

def hi():  # need parentheses because functions can take inputs
	# code
	print("Hello!")

hi()  # this will run the code; no special characters except "_"

# def super(): - not a great idea because super is a reserved word

# def hELLO(): - not wrong but hard to type
# def Hi(): - not proper convention to start with a capital

def hi():
	print("Greetings!") # overwrites the function

def hi(something):
	print("Greetings!", str(something) + "!")  # concatenation requires the same type of variable

# hi() - error because hi() is overwritten
hi("How are you?")

# def start():
# 	pass, break, continue - something must be in here