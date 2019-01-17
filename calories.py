import random as r
import matplotlib.pyplot as plot

# Parties: 1 - 5
# Desserts: 1 - 3
# Calories: 40 - 300

calories = []

trials = 10000000

for i in range(trials):
	p = r.randint(1, 5)
	d = r.randint(1, 3)
	c = r.randint(40, 300)

	total = p * d * c

	calories.append(total)

display = [0 for i in range(4502)]
for i in range(len(calories)):
	display[calories[i] + 1] += 1

plot.plot(display)
plot.ylabel("Holidays")
plot.xlabel("Calories")
plot.show()