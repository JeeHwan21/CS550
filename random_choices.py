import random as r

duration = []

for i in range(20):
	duration.append(2.6 + 0.1 * len(duration))

	# increment of 0.1 - i.e) 2.6, 2.7, 2.8, 2.9...

probability = []

for i in range(20):
	if 5 <= i <= 14:
		probability.append(0.06)

		# probability of 0.06 for songs that last from 3.1 to 4.0 minutes

	else:
		probability.append(0.04)

		# probability of 0.04 for songs that last under 3.1 or over 4.0 minutes

for i in range(1, 20):
	probability[i] = probability[i] + probability[i - 1]

week_total = 0

for i in range(7):
	week_total += sum(r.choices(duration, cum_weights = probability, k = r.randint(7, 20)))

	# number of songs listened to per day - 7 to 20 - everyday is different!