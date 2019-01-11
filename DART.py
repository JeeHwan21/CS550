# PART 1 - Monte Carlo Walk Simluation

# The longest walk I can take to ensure that I walk home 50% of the time is 22.
# I kept track of the steps I took in the x axis and y axis by creating two different lists for each and appended randomly chosen 1s and -1s to those lists until I reached ten times in total.
# Then, I added the elements of the lists to find the final x coordinate and y coordinate. Adding the absolute value of these two values gave me the distance from home.
# After having done 1000 trials for 10 blocks, I realized that the percentage was around 80%, so started increasing the number of blocks until the average percentage seemd like 50%.
# My final answer after trial and error was 22.

# PART 2 - What Are Monte Carlo Simulations?

# https://www.palisade.com/risk/monte_carlo_simulation.asp

# Monte Carlo simulations are performed for risk analysis. After analyzing all the different possible outcomes, random sets of values are substitued, including the extreme ends, in order to determine the probability distribution.
# The complexity of such simulations are dependent on the number of uncertainties and the their ranges. There are several different types of probability distributions, including normal, lognormal, triangular and uniform.


# PART 3 - Dart

import random as r

inCircle = []
outCircle = []

trials = 100000

for i in range(trials):
	# x coordinate of where it lands
	xwil = r.random() * 2 - 1
	# y coordinate of where it lands
	ywil = r.random() * 2 - 1

	if xwil * xwil + ywil * ywil <= 1:  # using the equation of a circle
		inCircle.append(1)
	else:
		outCircle.append(1)

print(len(inCircle) * 4 / trials)

# The output approaches pi as the number of trials increases.