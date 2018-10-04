import random as r, sys as s

def userinput():  # checking for errors for inputs
	while True:
		try:
			global func  # https://stackoverflow.com/questions/423379/using-global-variables-in-a-function (10.3.18)
			a, b, func = input("\nCOLUMN, ROW and r FOR REVEAL or f FOR FLAG WITH SPACES IN BETWEEN:\n>>").split()  # https://stackoverflow.com/questions/961263/two-values-from-one-input-in-python (10.3.18)
			break
		except ValueError:
			print("\nPLEASE ENTER THREE SEPEARATE VALUES.")
	while True:
		try:
			global col
			col = int(a)
			global row
			row = int(b)
			break
		except ValueError:
			print("\nCOLUMN AND ROW MUST BE INTERGERS.")
			userinput()
	if col < 1 or col > h or row < 1 or row > w:
		print("\nCOLUMN AND/OR ROW OUT OF RANGE.")
		userinput()
	elif func != "r" and func != "f":
		print("\nLAST VALUE MUST BE r or f.")
		userinput()

def ptbd():
	for x in board:
		print(*x)

def rf(a, b, c):
	if c == "r":
		board[a - 1][b - 1] = ans[a - 1][b - 1]
	ptbd()


w, h, b = [int(s.argv[1]), int(s.argv[2]), int(s.argv[3])]

# === ANSWER ===

if w < 1 or h < 1:
	print("UNABLE TO PRODUCE BOARD; PLEASE ENTER VALUES ABOVE ZERO.")

else:
	ans = [[0] * (w + 2) for x in range(h + 2)]

	for i in range(b):
		bh = r.randint(1, h)
		bw = r.randint(1, w)
		ans[bh][bw] = "*"

	for a in range(1, h + 1):
		for b in range(1, w + 1):
			if ans[a][b] == "*":  # Bombs
				continue
			else:  # Others
				sum = 0
				for i in range(3):
					for j in range(3):
						if ans[a - 1 + i][b - 1 + j] == "*":
							sum += 1
						else:
							continue
					ans[a][b] = sum

	for x in ans:
		del x[0], x[-1]
	del ans[0], ans[-1]

# === UNSOLVED ===

board = [["?"] * (w) for x in range(h)]

ptbd()

for x in ans:
	print(*x)

userinput()
print(col)
