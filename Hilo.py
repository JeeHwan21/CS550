import random

num = int(input("Choose a number between 0 and 100 inclusive - if you guess the right number right, you win!\nIf not, I will tell you whether it is too high or too low and you can take another shot.\nYou get three chances. Good luck!\n\n>> "))

answer = random.randint(0, 100)

def hilo():
	if num > answer:
		input("HIGH\n>>")
	elif num < answer:
		input("LOW\n>>")
	elif num == answer:
		print("You win! Congratulations!")
	else:
		print("I'm sorry, but please enter an integer!")
		hilo()

hilo()

hilo()

if input("HIGH\n>>") == answer or input("LOW\n>>") == answer:
	print("You win! Congratulations!")
else:
	print("I'm sorry, but you could not guess the right number.")

