# Partner 1: Ben
# Partner 2: JeeHwan

''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''

''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''
if grade == 'A':
	print("good work.")
 
 
''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
 
if yards < 17:
	yards = yards * 2 
 
''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''

if success:
	print("congratulations")
 
 
''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
if word[1] == 'f':
	print('fun')
 
 
''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''
 if celsius:
 	temp = 1.8 * temp + 32
 
 
''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
if not numItems == 0:
	averageCost = totalCost / numItems
else:
	print("No items")
 
 
''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''
 
 if pollution < cutoff:
 	print("safe condition")
 else:
 	print("Unsafe condition")

 
''' 8. 
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''

if score < 60:
	grade = "F"
elif score <= 69:
	grade = "D"
elif score <= 79:
	grade = "C"
elif score <= 89:
	grade = "B"
elif score <= 100:
	grade = "A"
 
 
''' 9. 
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''

if letter.isalpha():
	if letter == letter.lower():
		print("lowercase")
	else:
		print("uppercase") 
else:
	try:
		int(letter)
		print("digit")
	except ValueError:
		print("symbol")
''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''

if neighbors >= 50:
	home = "city"
elif neighbors >= 25:
	home = "suburbia"
elif neighbors >= 1:
	home = "rural"
else:
	home = "middle of nowhere" 
 
''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''
 
if doesSignificantWork and makesBreakthrough:
	if merit:
		nobelPrizeCandidate == True
	else:
		nobelPrizeCandidate == False
''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''

# taxRate = 0.065 for 6.5% tax rate
if tax:
	price = price * (1 + taxRate)
 
 
''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
if word[-1] == 's':
	print('plural')
elif word[-2:] == 'ly':
	print('adverb')
elif word[-3:] == 'ing':
	print('grrund') 
 
 
''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''

if currentNumber%2 != 0:
	currentNumber = currentNumber*3 + 1
else:
	currentNumber = currentNumber/2
 
''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''
leapYear = False
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			leapYear = True
	else:
		leapYear = True
 
 
''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
 
if a < b and a < c:
	smallestInt = int(a)
if b < c and b < a:
	smallestInt = int(b)
else:
	smallestInt = int(c)
 
''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
special = False 
if type(x) == int and x % 2 == 0 and x % 5 == 0 and -100 <= x <= 100:
	special = True:

''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
vowels = ['a', 'e', 'o', 'u', 'i']
code = 0
if letter in vowels:
	code = 1
elif letter == 'y':
	code = -1
 
 
''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
isWeekend = False
if dayOfWeek[0] == 'S':
	isWeekend = True 
 
 
''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
 
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
	numdays = 31
if month == "February":
	numdays = 28
if month == "April" or month == "June" or month == "September" or month == "November":
	numdays = 30
 
''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
validTriangle = False
if angle1 + angle2 + angle3 == 180:
	validTriangle = True 
 
 
''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
 
if electricity <= 50:
	bill = 0.50 * electricity
elif electricity <= 150:
	bill = 25 + 0.75 * (electricity - 50)
elif electricity <= 250:
	bill = 100 + 1.20 * (electricity - 150)
else:
	bill = (220 + 1.50 * (electricity - 250)) * 1.20
 
''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
if language == 'English':
	greeting = 'Hello'
elif language == 'French':
	greeting = 'Bonjour'
elif language == 'Spanish':
	greeting = 'Hola'
else:
	greeting = 'erm....' 
 
 
''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''
import random
nouns = ['human', 'dog', 'cat', 'elephant', 'home', 'cow', 'street']

num = random.randint(1,10)
num2 = random.randint(1,len(nouns)-1)
if num == 1:
	print(str(num), nouns[num2])
else:
	print(str(num), nouns[num2]+'s') 
  
 
''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''

if userInput == "bacon":
	print("Why did you type bacon?")
else:
	print("I like bacon.")
 
''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''
 
''' Task 1:
Weather is a string. If it equals sunny, print "Let's go out and play soccer." Otherwise, print "Let's watch Netflix."
'''
 
# solution
if weather == "sunny":
	print("Let's go out and play soccer.")
else:
	print("Let's watch Netflix.")
 
 
''' Task 2:
 	Variable homework is an integer between 0 and 10 representing the amount of homework on a night. If homework is below 5, hangOut is true, if homework is 0, study is false, if not study is true
'''
 
# solution

study = True
if homework < 5:
	hangOut = True
	if homework == 0:
		study = False
 
 
''' Task 3:
Variable pins represents the number of pins standing in a bowling alley. There is an equal but random chance of hitting any number of pins down. A player gets 2 throws. If he/she hits all 10 pins on the first try, print strike, if he/she knocks down all 10 pins in two tries, print spare 
'''
 
# solution
import random 
pins = 10
knock = random.randint(0,pins)
if first == pins:
	print('Strike!')
else:
	pins = 10-knock
	knock = random.randint(0,pins)
	if knock == pins:
		print('Spare!')
	else print('There are ' + str(pins-knock) + " pins left.")
 
''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''