import sys as s

Q1. FACTORIAL - MAX: 998

def fac(a):
	try:
		b = int(a)
		if b == 1:
			return 1
		elif b == 0:
			return 1
		elif b < 0:
			print("NEED A POSITIVE INTEGER")
		elif b > 1:
			return b * fac(b - 1)
	except ValueError:
		print("NEED A POSITIVE INTEGER")

print(fac(s.argv[1]))
