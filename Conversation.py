name = input("Hi, what's your name? ")
print("Nice to meet you, "+name+"!")
place = input("Where are you from? ")
print("I've never been to "+place+", but I hope to travel there one day.")
grade = input("What form are you in? ")
if grade == "third":
	print("Really? Hope you make the most out of your freshman year!")
elif grade == "fourth":
	print("Really? Hope you make the most out of your sophomore year!")
elif grade == "fifth":
	print("Really? Hope you make the most out of your junior year!")
elif grade == "sixth":
	print("Really? Hope you make the most out of your final year at Choate!")
food = input("What's your favorite food? ")
if food == "pizza":
	pizza = input("Same! What's your favorite kind? ")
	hobby = input("I also love "+pizza+" pizza!\nWhat's your favorite hobby? ")
else:
	print("Nice! My favorite food is pizza, but I also love "+food+"!")
	hobby = input("What's your favorite hobby? ")
reason = input("Why do you like "+hobby+"? ")
print("Well, I'm glad you enjoy "+hobby+"!\nIt was nice talking to you! We should eat "+food+" together some time!")