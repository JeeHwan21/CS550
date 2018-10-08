import random as r, sys as s

# === UNSOLVED ===

def reset():  # make a board of question marks
	global board
	board = [["?"] * (w + 2) for x in range(h + 2)]
	for x in board:
		x[0], x[-1] = "|", "|"
	board[0] = "┌" + "-" * w + "┐"
	board[-1] = "└" + "-" * w + "┘"

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

def printBoard():  # print the current board
	print()
	for x in board:
		print(*x)

def lose():
	x = input("\nYOU LOSE! TRY AGAIN? (1: YES 2: NO)\n>>")
	if x == "1":
		game()
	elif x == "2":
		quit()
	else:
		print("\nPLEASE ENTER 1 OR 2.")
		lose()

# === ANSWER ===

def answer():  # make the answer board
	global ans
	ans = [["|"] * (w + 2) for x in range(h + 2)]

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

	ans[0] = "-" * (w + 2)
	ans[-1] = "-" * (h + 2)

def zero(a, b):  # reveal all of the contiguous zeroes
	for i in range(-1, 2):
		for j in range(-1, 2):
			if ans[b + i][a + j] == 0 and board[b + i][a + j] == "?":
				board[b + i][a + j] = ans[b + i][a + j]
				zero(a + j, b + i)
			elif ans[b + i][a + j] == "|" or ans[b + i][a + j] == "-":
				continue
			else:
				board[b + i][a + j] = ans[b + i][a + j]

def win():
	x = input("\nYOU WIN! TRY AGAIN? (1: YES 2: NO)\n>>")
	if x == "1":
		game()
	elif x == "2":
		quit()
	else:
		print("\nPLEASE ENTER 1 OR 2.")
		win()

def winCheck():  # check if the board is complete with correct answers
	sum = 0
	for i in range(1, h + 1):
		for j in range(1, w + 1):
			if board[i][j] == ans[i][j]:
				sum += 1
			elif board[i][j] == "F" and ans[i][j] == "*":
				sum += 1
	if sum == w * h:
		win()

def revealFlag(a, b, c):  # reveal characters and numbers depending on function (r or f)
	if c == "r":
		if ans[b][a] == "*":  # lose
			board[b][a] = ans[b][a]
			printBoard()
			lose()
		elif ans[b][a] == 0:  # reveal contiguous zeroes
			zero(a, b)
			printBoard()
			winCheck()
			checkInput()
			revealFlag(col, row, func)
		else:  # reveal number
			board[b][a] = ans[b][a]
			printBoard()
			winCheck()
			checkInput()
			revealFlag(col, row, func)
	elif c == "f":  # flag
		board[b][a] = "F"
		printBoard()
		checkInput()
		revealFlag(col, row, func)

def game():  # for restarting the game after winning or losing
	start()
	answer()
	reset()
	printBoard()
	checkInput()
	revealFlag(col, row, func)

def start():  # selecting the dimensions of the minesweeper board
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


print("\n=======================\nWELCOME TO MINESWEEPER!\n=======================")
start()
answer()
reset()
printBoard()
checkInput()
revealFlag(col, row, func)
