# For  a  list  with  random  values,  if  any  value  in  the  list  is  divisible  by  the  first  value  of  the  list,  delete  that  value  (Pearson,  Kyn,  Dominique,  and  Scott)

import sys
import random

print("\nQ2.")

a2 = []
b2 = []

for i in range(20):
	x = random.randint(1, sys.maxsize)  # https://stackoverflow.com/questions/35361811/how-to-generate-n-random-numbers-in-python-3-between-0-to-infinity (9.27.18)
	a2.append(x)

print ("Original: List:", a2)

for i in range(1, 20):
	if a2[i] % a2[0] != 0:
		b2.append(a2[i])
	else:
		continue

print("Revised List:", [a2[0]] + b2)