import random  # import random as r

print(random.random())  # random number [0,1)
print(random.random() * 8 + 7)  # random number [7,15)

print(random.randint(5,10) * 10)
print(random.randrange(50, 101, 10))

import math as m
print(m.sqrt(9))
print(m.fabs(-10.3))

print(m.pow(m.sin(random.random() * 2 * m.pi), 2) + m.pow(m.cos(random.random() * 2 * m.pi), 2))