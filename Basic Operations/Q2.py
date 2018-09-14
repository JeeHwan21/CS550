import sys as s

x = float(s.argv[1])
y = float(s.argv[2])
z = float(s.argv[3])

if x < y < z or x > y > z:
	print(True)
else:
	print(False)