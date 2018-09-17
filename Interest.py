import math as m
import sys as s

t = float(s.argv[1])
P = float(s.argv[2])
r = float(s.argv[3])

output = str(round(P * m.pow(m.e, r * t), 2))

print(output + "$")