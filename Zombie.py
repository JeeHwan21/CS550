def mistake():
	print("Please enter 1 or 2.")

def retry():
	choice = input("Would you like to try again?\n1)Yes\n2)No\n\n>>")
	if choice == "1":
		start()
	elif choice == "2":
		quit()
	else:
		mistake()
		retry()

def start():
	choice = input("\nIt was a hot summer night when you and your friend went to the biggest club in the city for a fun night...\nYou told your parents you would be back before midnight, but while you were enjoying yourself, a group of zombies started attacking the club...\nThere is complete chaos and nothing but darkness and screaming...\n\nWill you look for your friend in the crowd?\n1)Yes\n2)No\n\n>>")
	if choice == "1":
		friend()
	elif choice == "2":
		noFriend()
	else:
		mistake()
		start()

def friend():
	choice = input("\nFortunately, you found your friend! Your friend seems very drunk, so you carry him on your back. You think you know where the exit is...\n\nShould you hide first, or go striaght to the exit?\n1)Hide\n2)Go straight to the exit\n\n>>")
	if choice == "1":
		friendExit()
	elif choice == "2":
		friendHide()
	else:
		mistake()
		friend()

def friendExit():
	pass

def friendHide():
	pass

def noFriend():
	pass

start()