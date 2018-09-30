import random as r, sys as s

w = int(s.argv[1])
h = int(s.argv[2])
b = int(s.argv[3])

if w < 1 or h < 1:
	print("Please enter first two volues over 0.")

else:
	mf = [[0] * w for x in range(h)]

	for i in range(b):
		bx = r.randint(0, w - 1)
		by = r.randint(0, h - 1)
		mf[bx][by] = "*"  # same spot could be chosen twice...

	print(mf[0][2])
	for i in range(h):
		for j in range(w):
			if mf[h]












	for x in mf:
		print(*x)
