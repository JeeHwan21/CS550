def start():
	choice = input("/n/n/n/n/n/nGreetings! /n/n You are heading to the dining hall one day when there's a bear walking with a dinosaur on campus!! Do you /n/n1) stay inside, or /n2) head on over to walk with them? /n/n>> ")
	if choice == "1":
		choice = input("Lame!... 1)... 2)...")
		if choice == "1":
			# something
		elif choice == "2":
			# something
	elif choice == "2":  # crazy indentation...

# So...
def inside():
	pass

def walkWithDinoBear():
	pass

def start():
	choice = input("/n/n/n/n/n/nGreetings! /n/n You are heading to the dining hall one day when there's a bear walking with a dinosaur on campus!! Do you /n/n1) stay inside, or /n2) head on over to walk with them? /n/n>> ")
	if choice == "1":
		inside()
	elif choice == "2":
		walkWithDinoBear()
	else:  # typed in something that is not "1" or "2"
		print("Please enter a 1 or 2. Thank you!")
		start()  # recursive function
	print("hi!")


# exit() - end the entire game