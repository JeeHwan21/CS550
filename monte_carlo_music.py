import random as r
import matplotlib.pyplot as m

# JeeHwan Kim
# https://docs.python.org/3/library/random.html (1.16.19)
# On my honor, I have neither given nor received unauthorized aid.

# SONGS (IN A DAY)
# Duration: 2.6 - 4.5 (WEIGHTED RANDOMNESS)
# Frequency (per day): 10 - 20

# MIXES (IN A WEEK)
# Duration: 40 - 100 (WEIGHTED RANDOMNESS)
# Frequency (per week): 1 - 2 (WEIGHTED RANDOMNESS)


# SONGS

sduration = []

for i in range(20):
	sduration.append(2.6 + 0.1 * len(sduration))

	# increment of 0.1

sprobability = []

for i in range(20):
	if 5 <= i <= 14:
		sprobability.append(0.06)

		# probability of 0.06 for songs that last from 3.1 to 4.0 minutes

	else:
		sprobability.append(0.04)

		# probability of 0.04 for songs that last under 3.1 or over 4.0 minutes

for i in range(1, 20):
	sprobability[i] = sprobability[i] + sprobability[i - 1]

# MIXES

mduration = [40, 50, 60, 70, 80, 90, 100]

# increment of 10

mprobability = [0.15, 0.17, 0.17, 0.16, 0.14, 0.11, 0.1]

# probabilities that I selected based on experience

for i in range(1, 7):
	mprobability[i] = mprobability[i] + mprobability[i - 1]

mfrequency = r.choice([1, 1, 1, 1, 2])

# I would do two mixes in a week maybe about every five weeks.

mpw = []  # minutes per week

for i in range(1000):  # million trials
	
	week_songs = 0

	for i in range(7):
		week_songs += sum(r.choices(sduration, cum_weights = sprobability, k = r.randint(10, 20)))
		# https://docs.python.org/3/library/random.html (1.16.19)

		# number of songs listened to per day - 10 to 20 - everyday is different!

	week_mixes = sum(r.choices(mduration, cum_weights = mprobability, k = mfrequency))

	week_total = week_songs + week_mixes

	mpw.append(week_total)

# GRAPH

display = [0 for i in range(222, 831)]
for i in range(len(mpw)):
	display[int(mpw[i] + 1)] += 1

m.plot(display)
m.xlabel("Minutes per Week")
m.ylabel("Number of Weeks")
m.show()






