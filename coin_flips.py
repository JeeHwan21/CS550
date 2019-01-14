import random as r
import collections as c

totalCnt = []
trials = 13

for i in range(trials):
	ht = []
	for i in range(10):
		x = r.randint(0, 1)
		ht.append(str(x))

	cnt = c.Counter(ht)
	totalCnt.append(cnt["0"])

cnt2 = c.Counter(totalCnt)

for i in range(trials):
	print(str(i) + ": " + str(cnt2[str(i)]))