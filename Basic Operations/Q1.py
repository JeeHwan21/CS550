import sys as s
import math as m

t = float(s.argv[1])
v = float(s.argv[2])

w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * m.pow(v, 0.16)

print(w)