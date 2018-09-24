while True:
	try:
		x = int(input("Pick a number from 1 to 5.\n\n>>"))
		if x < 1 or x > 5:
			print("I'm sorry, but that's not from 1 to 5.")  # only print! The loop will make it return to the start.
		else:
			break
	except ValueError:
		print("I'm sorry, but that's not a number.")  # only print! The loop will make it return to the start.

print("Success!")