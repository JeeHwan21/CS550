# http://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm
# https://en.wikipedia.org/wiki/Box-drawing_character
# https://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value

import random as r

# how to erase the border between the frontier and the parent for the four different situations (top, bottom, left, right)

def parentontop(i, j):

	agrid[i - 1][j * 2 - 1] = " "

	a = agrid[i - 1][j * 2 - 2]

	if a == "├":
		agrid[i - 1][j * 2 - 2] = "│"
	elif a == "┬":
		agrid[i - 1][j * 2 - 2] = "┐"
	elif a == "┼":
		agrid[i - 1][j * 2 - 2] = "┤"	
	elif a == "└":
		agrid[i - 1][j * 2 - 2] = "╵"
	elif a == "┴":
		agrid[i - 1][j * 2 - 2] = "┘"
	elif a == "┌":
		agrid[i - 1][j * 2 - 2] = "╷"
	elif a == "╶":
		agrid[i - 1][j * 2 - 2] = " "

	b = agrid[i - 1][j * 2]

	if b == "┤":
		agrid[i - 1][j * 2] = "│"
	elif b == "┬":
		agrid[i - 1][j * 2] = "┌"
	elif b == "┴":
		agrid[i - 1][j * 2] = "└"
	elif b == "┼":
		agrid[i - 1][j * 2] = "├"	
	elif b == "┘":
		agrid[i - 1][j * 2] = "╵"
	elif b == "┐":
		agrid[i - 1][j * 2] = "╷"
	elif b == "╴":
		agrid[i - 1][j * 2] = " "

def parentonbottom(i, j):

	agrid[i][j * 2 - 1] = " "

	a = agrid[i][j * 2 - 2]

	if a == "├":
		agrid[i][j * 2 - 2] = "│"
	elif a == "┬":
		agrid[i][j * 2 - 2] = "┐"
	elif a == "┼":
		agrid[i][j * 2 - 2] = "┤"	
	elif a == "└":
		agrid[i][j * 2 - 2] = "╵"
	elif a == "┴":
		agrid[i][j * 2 - 2] = "┘"
	elif a == "┌":
		agrid[i][j * 2 - 2] = "╷"
	elif a == "╶":
		agrid[i][j * 2 - 2] = " "

	b = agrid[i][j * 2]

	if b == "┤":
		agrid[i][j * 2] = "│"
	elif b == "┬":
		agrid[i][j * 2] = "┌"
	elif b == "┴":
		agrid[i][j * 2] = "└"
	elif b == "┼":
		agrid[i][j * 2] = "├"		
	elif b == "┘":
		agrid[i][j * 2] = "╵"
	elif b == "┐":
		agrid[i][j * 2] = "╷"
	elif b == "╴":
		agrid[i][j * 2] = " "

def parentonleft(i, j):

	a = agrid[i - 1][j * 2 - 2]

	if a == "├":
		agrid[i - 1][j * 2 - 2] = "└"
	elif a == "┼":
		agrid[i - 1][j * 2 - 2] = "┴"
	elif a == "┤":
		agrid[i - 1][j * 2 - 2] = "┘"
	elif a == "┌":
		agrid[i - 1][j * 2 - 2] = "╶"
	elif a == "┬":
		agrid[i - 1][j * 2 - 2] = "─"
	elif a == "┐":
		agrid[i - 1][j * 2 - 2] = "╴"
	elif a == "╷":
		agrid[i - 1][j * 2 - 2] = " "

	b = agrid[i][j * 2 - 2]

	if b == "├":
		agrid[i][j * 2 - 2] = "┌"
	elif b == "┼":
		agrid[i][j * 2 - 2] = "┬"
	elif b == "┤":
		agrid[i][j * 2 - 2] = "┐"
	elif b == "└":
		agrid[i][j * 2 - 2] = "╶"
	elif b == "┴":
		agrid[i][j * 2 - 2] = "─"
	elif b == "┘":
		agrid[i][j * 2 - 2] = "╴"
	elif b == "╵":
		agrid[i][j * 2 - 2] = " "

def parentonright(i, j):

	a = agrid[i - 1][j * 2]

	if a == "├":
		agrid[i - 1][j * 2] = "└"
	elif a == "┼":
		agrid[i - 1][j * 2] = "┴"
	elif a == "┤":
		agrid[i - 1][j * 2] = "┘"
	elif a == "┌":
		agrid[i - 1][j * 2] = "╶"
	elif a == "┬":
		agrid[i - 1][j * 2] = "─"
	elif a == "┐":
		agrid[i - 1][j * 2] = "╴"
	elif a == "╷":
		agrid[i - 1][j * 2] = " "

	b = agrid[i][j * 2]

	if b == "├":
		agrid[i][j * 2] = "┌"
	elif b == "┼":
		agrid[i][j * 2] = "┬"
	elif b == "┤":
		agrid[i][j * 2] = "┐"
	elif b == "└":
		agrid[i][j * 2] = "╶"
	elif b == "┴":
		agrid[i][j * 2] = "─"
	elif b == "┘":
		agrid[i][j * 2] = "╴"
	elif b == "╵":
		agrid[i][j * 2] = " "

def frontier(i, j):

	# check for frontiers around a "D" (Done) square and append its coordinates to the "left" list if it isn't already in there

	if igrid[i][j] == "D" and igrid[i - 1][j] != "D" and igrid[i - 1][j] != "B":
		igrid[i - 1][j] = "F"

		if [i - 1, j] not in left:
			left.append([i - 1, j])

	if igrid[i][j] == "D" and igrid[i + 1][j] != "D" and igrid[i + 1][j] != "B":
		igrid[i + 1][j] = "F"

		if [i + 1, j] not in left:
			left.append([i + 1, j])

	if igrid[i][j] == "D" and igrid[i][j + 1] != "D" and igrid[i][j + 1] != "B":
		igrid[i][j + 1] = "F"

		if [i, j + 1] not in left:
			left.append([i, j + 1])

	if igrid[i][j] == "D" and igrid[i][j - 1] != "D" and igrid[i][j - 1] != "B":
		igrid[i][j - 1] = "F"

		if [i, j - 1] not in left:
			left.append([i, j - 1])

	# randomly choose an available frontier from the "left" list

	randleftover = r.randint(0, len(left) - 1)

	temp = left[randleftover]

	# check for "D" (Done) squares around the chosen frontier and gather the different options (top, bottom, left & right)

	parentoptions = []

	if igrid[temp[0] - 1][temp[1]] == "D":
		parentoptions.append(1)

	if igrid[temp[0] + 1][temp[1]] == "D":
		parentoptions.append(2)

	if igrid[temp[0]][temp[1] - 1] == "D":
		parentoptions.append(3)

	if igrid[temp[0]][temp[1] + 1] == "D":
		parentoptions.append(4)

	ran = r.randint(0, len(parentoptions) - 1)

	# randomly choose one of the available options and erase the border between the frontier and the "D" square of the chosen direction

	if parentoptions[ran] == 1:
		parentontop(temp[0], temp[1])

	elif parentoptions[ran] == 2:
		parentonbottom(temp[0], temp[1])

	elif parentoptions[ran] == 3:
		parentonleft(temp[0], temp[1])

	elif parentoptions[ran] == 4:
		parentonright(temp[0], temp[1])

	# now that the frontier is done, make it a "D" square

	igrid[temp[0]][temp[1]] = "D"

	# and remove it from the "left" list since it is not a frontier anymore

	left.remove(left[randleftover])  # https://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value

	# if there are still frontiers left to be sorted, run this function again

	if len(left) > 0:

		frontier(temp[0], temp[1])

# ├, ┼, ┤, ┌, ┬, ┐, └, ┴, ┘, ─, ╷, ╵, │, ╴, ╶
# https://en.wikipedia.org/wiki/Box-drawing_character

# randomly generate dimensions for the maze (unfortunately cannot go crazy with the numbers because the frontier function is recursive)

dx = r.randint(5, 25)
dy = r.randint(5, 25)

# form the "agrid" (actual grid) which will be displayed as the final result

agrid = []

for i in range(dy + 1):
	agrid.append([])

agrid[0].append("┌")

for i in range(dx):
	agrid[0].append("─")
	agrid[0].append("┬")
agrid[0][-1] = "┐"

for i in range(1, dy):
	agrid[i].append("├")
	for j in range(dx):
		agrid[i].append("─")
		agrid[i].append("┼")
	agrid[i][-1] = "┤"

agrid[dy].append("└")

for i in range(dx):
	agrid[dy].append("─")
	agrid[dy].append("┴")
agrid[dy][-1] = "┘"

# form the "left" list to be used in the frontier function

left = []

# form the "igrid" (invisible grid) to which the "agrid" (actual grid) will refer in order to make decisions

igrid = [["B"] * (dx + 2) for x in range(dy + 2)]

for i in range(1, dy + 1):
	for j in range(1, dx + 1):
		igrid[i][j] = 0

# randomly choose the starting "D" square and turn it from 0 to "D"

x = r.randint(1, dy)
y = r.randint(1, dx)

igrid[x][y] = "D"

# run the recursive frontier function using its coordinates as the starting point

frontier(x, y)

# print the final result neatly

for i in agrid:
	for j in i:
		print(j, end = "")
	print()