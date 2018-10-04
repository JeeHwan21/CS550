import random as r, sys as s

w = int(s.argv[1])
h = int(s.argv[2])
b = int(s.argv[3])

if w < 1 or h < 1:
	print("UNABLE TO PRODUCE BOARD; PLEASE ENTER VALUES ABOVE ZERO.")

else:
	mf = [[0] * (w + 2) for x in range(h + 2)]

	for i in range(b):
		bh = r.randint(1, h)
		bw = r.randint(1, w)
		mf[bh][bw] = "*"

	for a in range(1, h + 1):
		for b in range(1, w + 1):
			if mf[a][b] == "*":  # Bombs
				continue
			else:  # Others
				sum = 0
				for i in range(3):
					for j in range(3):
						if mf[a - 1 + i][b - 1 + j] == "*":
							sum += 1
						else:
							continue
					mf[a][b] = sum

	for x in mf:
		del x[0], x[-1]
	del mf[0], mf[-1]

	for x in mf:
		print(*x)