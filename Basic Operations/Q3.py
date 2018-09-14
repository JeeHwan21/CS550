import sys as s

m = int(s.argv[1])
d = int(s.argv[2])
y = int(s.argv[3])

a = y - (14 - m) // 12
x = a + a // 4 - a // 100 + a // 400
b = m + 12 * ((14 - m) // 12) - 2
c = (d + x + (31 * b) // 12) % 7

print(c)