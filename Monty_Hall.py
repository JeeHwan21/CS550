# It would be wiser to switch because initially, there is a much higher chance of choosing a penny than choosing a car (2/3 vs 1/3).
# This means that there is a 2/3 chance that the uneliminated item is a car, which is higher than that of the alternative.

import random as r

#switch

cars = []
pennies = []

print("SWITCH")

for i in range(1000):

	choices = [1, 2, 3]
	choicesEliminate = [1, 2, 3]

	car = r.randint(1, 3)
	initChoice = r.randint(1, 3)

	if car == initChoice:
		choicesEliminate.remove(car)
	else:
		choicesEliminate.remove(car)
		choicesEliminate.remove(initChoice)

	choices.remove(r.choice(choicesEliminate))
	choices.remove(initChoice)

	finalChoice = choices[0]

	if finalChoice == car:
		cars.append(1)
	else:
		pennies.append(1)

print("CAR: " + str(len(cars)))
print("PENNY: " + str(len(pennies)))

#not switch

cars = []
pennies = []

print("\nNOT SWITCH")

for i in range(1000):
	car = r.randint(1, 3)
	initAndFinalChoice = r.randint(1, 3)

	if initAndFinalChoice == car:
		cars.append(1)
	else:
		pennies.append(1)

print("CAR: " + str(len(cars)))
print("PENNY: " + str(len(pennies)))

# Exactly what I predicted happened in the simluation. On average, there was a 2/3 chance that I would win the car if I switched and a 1/3 chance that I would win the car if I did not switch.
# This is because there is a 1/3 chance of choosing the car in the beginning, which means if I switch, the chance automatically becomes 2/3 because I'm choosing whatever I did not choose in the first place.







