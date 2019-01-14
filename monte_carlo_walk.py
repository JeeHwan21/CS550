import random as r

walkBack = []
bus = []

for i in range(1000):
	x = []
	y = []
	for i in range(10):
		walk = r.randint(0, 1)
		direction = r.randint(0, 1)

		if direction == 0:
			if walk == 0:
				x.append(-1)
			else:
				x.append(1)
		else:
			if walk == 0:
				y.append(-1)
			else:
				y.append(1)

	xFinal = sum(x)
	yFinal = sum(y)

	if abs(xFinal) + abs(yFinal) <= 4:
		walkBack.append(1)
	else:
		bus.append(1)

print("WALK: " + str(len(walkBack)))
print("BUS: " + str(len(bus)))