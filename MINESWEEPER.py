import random as r, sys as s

w = int(s.argv[1])
h = int(s.argv[2])
b = int(s.argv[3])

if w < 1 or h < 1:
	print("Please enter first two values over 0.")

else:
	mf = [[0] * w for x in range(h)]

	for i in range(b):
		bh = r.randint(0, h - 1)
		bw = r.randint(0, w - 1)
		mf[bh][bw] = "*"  # same spot could be chosen twice...

	for a in range(h):
		for b in range(w):

			# Bombs

			if mf[a][b] == "*":
				continue

			# Vertex

			elif a == 0 and b == 0:
				sum = 0
				for i in range(2):
					for j in range(2):
						if mf[i][j] == "*":
							sum += 1
						else:
							continue
				mf[a][b] = sum

			elif a == 0 and b == w - 1:
				sum = 0
				for i in range(2):
					for j in range(2):
						if mf[i][w - 1 - j] == "*":
							sum += 1
						else:
							continue
				mf[a][b] = sum

			elif a == h - 1 and b == 0:
				sum = 0
				for i in range(2):
					for j in range(2):
						if mf[h - 1 - i][j] == "*":
							sum += 1
						else:
							continue
				mf[a][b] = sum

			elif a == h - 1 and b == w - 1:
				sum = 0
				for i in range(2):
					for j in range(2):
						if mf[h - 1 - i][w - 1 - j] == "*":
							sum += 1
						else:
							continue
				mf[a][b] = sum

			# Edges

			elif a == 0:
				sum = 0
				for i in range(2):
					for j in range(3):
						if mf[i][b - 1 + j] == "*":
							sum += 1
						else:
							continue
				mf[a][b] = sum

			elif a == h - 1:
				sum = 0
				for i in range(2):
					for j in range(3):
						if mf[h - 1 - i][b - 1 + j] == "*":
							sum += 1
						else:
							continue
				mf[a][b] = sum

			elif b == 0:
				sum = 0
				for i in range(3):
					for j in range(2):
						if mf[a - 1 + i][j] == "*":
							sum += 1
						else:
							continue
				mf[a][b] = sum

			elif b == w - 1:
				sum = 0
				for i in range(3):
					for j in range(2):
						if mf[a - 1 + i][w - 1 - j] == "*":
							sum += 1
						else:
							continue
				mf[a][b] = sum

			# Middle

			else:
				sum = 0
				for i in range(3):
					for j in range(3):
						if mf[a - 1 + i][b - 1 + j] == "*":
							sum += 1
					else:
						continue
				mf[a][b] = sum

	for x in mf:
		print(*x)
