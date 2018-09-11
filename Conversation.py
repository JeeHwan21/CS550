# 9.10.18 / Computer Conversations
# ================================
# https://stackoverflow.com/questions/11497376/how-would-i-specify-a-new-line-in-python

name = input("Hi, what's your name? ")
print("Nice to meet you, "+name+"!")

place = input("Where are you from? ")
print("I've never been to "+place+", but I hope to travel there one day.")

grade = input("What form are you in? ")
if grade == "third":
	print("Awesome, I hope you make the most out of your freshman year!")
elif grade == "fourth":
	print("Awesome, I hope you make the most out of your sophomore year!")
elif grade == "fifth":
	print("Awesome, I hope you make the most out of your junior year!")
elif grade == "sixth":
	print("Awesome, I hope you make the most out of your final year at Choate!")

food = input("What's your favorite food? ")
if food == "pizza":
	pizza = input("Same! What's your favorite kind? ")
	hobby = input("I also love "+pizza+" pizza!\nWhat's your favorite hobby? ")
else:
	print("Nice! My favorite food is pizza, but I also love "+food+"!")
	hobby = input("What's your favorite hobby? ")
year = input("Really? "+hobby+" sounds fun! For how many years have you enjoyed "+hobby+"? ")
if int(year) < 4:
	print("Wow, I hope you pursue "+hobby+"! I'm really sorry, but I have to go.\nIt was really nice talking to you! We should eat "+food+" together some time!")
else:
	print("Wow, "+year+" years? That's a long time! I'm really sorry, but I have to go\nIt was really nice talking to you! We should eat "+food+" together some time!")