import random as r, sys as s

def checkInput():  # checking for errors for inputs
	while True:
		try:
			global col, row, func  # https://stackoverflow.com/questions/423379/using-global-variables-in-a-function (10.3.18)
			a, b, func = input("\nCOLUMN, ROW and r FOR REVEAL or f FOR FLAG WITH SPACES IN BETWEEN (ex: 1 1 r)\n>>").split()  # https://stackoverflow.com/questions/961263/two-values-from-one-input-in-python (10.3.18)
			break
		except ValueError:
			print("\nPLEASE ENTER THREE SEPEARATE VALUES.")
	while True:
		try:
			col = int(a)
			row = int(b)
			break
		except ValueError:
			print("\nCOLUMN AND ROW MUST BE INTEGERS.")
			checkInput()
	if col < 1 or col > h or row < 1 or row > w:
		print("\nCOLUMN AND/OR ROW OUT OF RANGE.")
		checkInput()
	elif func != "r" and func != "f":
		print("\nLAST VALUE MUST BE r or f.")
		checkInput()

def printBoard():
	print()
	for x in board:
		print(*x)

def lose():
	x = input("\nTRY AGAIN? (1: YES 2: NO)\n>>")
	if x == "1":
		game()
	elif x == "2":
		quit()
	else:
		print("\nPLEASE ENTER 1 OR 2.")
		lose()


def revealFlag(a, b, c):
	if c == "r":
		board[a - 1][b - 1] = ans[a - 1][b - 1]
		printBoard()
		if board[a - 1][b - 1] == "*":
			lose()
		else:
			checkInput()
			revealFlag(col, row, func)
	elif c == "f":
		board[a - 1][b - 1] = "F"
		printBoard()
		checkInput()
		revealFlag(col, row, func)

def game():
	start()
	answer()
	reset()
	printBoard()
	checkInput()
	revealFlag()

print("\n=======================\nWELCOME TO MINESWEEPER!\n=======================")

def start():
	while True:
		try:
			global w, h, b
			x, y, z = input("\nWIDTH, HEIGHT AND NUMBER OF BOMBS WITH SPACES IN BETWEEN (ex: 5 6 4)\n>>").split()
			w = int(x)
			h = int(y)
			b = int(z)
			break
		except ValueError:
			print("\nPLEASE ENTER THREE INTEGERS.")

# === ANSWER ===

def answer():
	global ans
	ans = [[0] * (w + 2) for x in range(h + 2)]

	for i in range(b):
		bh = r.randint(1, h)
		bw = r.randint(1, w)
		ans[bh][bw] = "*"

	for e in range(1, h + 1):
		for f in range(1, w + 1):
			if ans[e][f] == "*":
				continue
			else:
				sum = 0
				for i in range(3):
					for j in range(3):
						if ans[e - 1 + i][f - 1 + j] == "*":
							sum += 1
						else:
							continue
					ans[e][f] = sum

	for x in ans:
		del x[0], x[-1]
	del ans[0], ans[-1]

def reset():
	global board
	board = [["?"] * (w) for x in range(h)]

# === UNSOLVED ===

start()
answer()
reset()
printBoard()
checkInput()
revealFlag(col, row, func)

