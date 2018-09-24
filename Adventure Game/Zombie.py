def check(choice,a,b):
	while choice != a and choice != b:
		choice = input("\nPlease enter 1 or 2.\n\n>>")
	return choice

def retry():
	choice = input("\nPLAY AGAIN?\n\n1)Yes\n2)No\n\n>>")
	if check(choice,"1","2") == "1":
		start()
	else:
		quit()

def start():
	choice = input("\nIt was a hot summer evening when you and your friend went to the biggest club in the city for a wild night...\nYou told your parents you would be back before midnight, but while you were enjoying yourself, a group of zombies started attacking the club...\nThere is complete chaos and nothing but darkness and screaming...\nYou must get back home safe.\nWill you look for your friend in the crowd?\n\n1)Yes\n2)No\n\n>>")
	if check(choice,"1","2") == "1":
		friend()
	else:
		noFriend()

def friend():
	choice = input("\nFortunately, you found your friend! Your friend seems very drunk, so you carry him on your back.\nYou think you know where the exit is...Will you hide first, or go striaght to the exit?\n\n1)Hide\n2)Go straight to the exit\n\n>>")
	if check(choice,"1","2") == "1":
		friendHide()
	else:
		friendExit()

def friendExit():
	choice = input("\nWhile you were running to the exit, your friend got attacked by a zombie.\nYou survived, though, and now you are left in the middle of the club.\nWill you continue to the exit, or hide in a bathroom?\n\n1)Continue to exit\n2)Hide in a bathroom\n\n>>")
	if check(choice,"1","2") == "1":
		gotoExit()
	else:
		bathroom()

def gotoExit():
	choice = input("\nYou successfully reached the exit, but the exit is locked! There are zombies running toward you!\nOn your left is a group of people and on your right is a staircase.\nWhich way will you go?\n\n1)Group of people\n2)Staircase\n\n>>")
	if check(choice,"1","2") == "1":
		people()
	else:
		staircase()

def people():
	print("\nOh no! They actually turned out to be zombies, and they started attacking you...\nYou will not get back home.")
	retry()

def staircase():
	choice = input("\nYou can either go upstairs or downstairs. Which way will you go?\n\n1)Upstairs\n2)Downstairs\n\n>>")
	if check(choice,"1","2") == "1":
		upstairs()
	else:
		downstairs()

def downstairs():
	print("\nYou have come to the parking lot. There seem to be no zombies, and there is an exit to the street!\nYou can escape and arrive home safely.")


def upstairs():
	choice = input("\nNo one is up here, and there are only closed stores. You can hide here, but if you want to be home by midnight, you must get out.\nWill you head down to the club or the basement?\n\n1)Club\n2)Basement\n\n>>")
	if check(choice,"1","2") == "1":
		backtoClub()
	else:
		downstairs()

def backtoClub():
	pass

def bathroom():
	print("\nYou walked into the closest bathroom and entered an empty cubicle. You thought you were safe, but a zombie crawled in from an adjacent cubicle and attacked you.\nYou will not get back home.")
	retry()

def friendHide():
	choice = input("\nYou ran to the nearest table with your friend and hid underneath. However, a scared security guard already there thought you two were zombies and shot your friend first.\nWill you runaway or try to persaude the security guard that you are not a zombie?\n\n1)Runaway\n2)Try to persuade the security guard\n\n>>")
	if check(choice,"1","2") == "1":
		runaway()
	else:
		persuade()

def runaway():
	print("\nWhile you were running away, a zombie attacked you from behind.\nYou will not get back home.")
	retry()

def persuade():
	pass

def noFriend():
	choice = input("\nYou are on your own, and you think you know where the exit is.\nWill you hide first, or head straight to the exit?\n\n1)Hide first\n2)Head to the exit\n\n>>")
	if check(choice,"1","2") == "1":
		hideAlone()
	else:
		exitAlone()

def exitAlone():
	print("\nOn your way to the exit, a zombie attacked you from behind.\nYou will not get back home.")
	retry()

def hideAlone():
	print("\nYou ran to the nearest table and hid underneath. However, a scared security guard already there thought you were a zombie and shot you.\nYou will not get back home.")
	retry()

start()