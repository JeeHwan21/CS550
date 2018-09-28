# Generate  a  list  of  10  random  numbers  between  0  and  100.  Get  them  inorder  from  largest  to  smallest,  removing  numbers  divisible  by  3.  (Ms.  Healey)

import random

print("Q1.")

a1 = []
b1 = []

for i in range(10):
	x = random.randint(1, 99)
	a1.append(x)

print("Original List:", a1)

for i in range(10):
	if a1[i] % 3 != 0:
		b1.append(a1[i])
	else:
		continue

b1.sort()
b1.reverse()

print("Revised List:", b1)