# JeeHwan Kim
# 11.15.18

# For my project, I decided to make randomized mazes with dimensions ranging from 5 x 5 to 25 x 25 (can be rectangles).
# I used lists, recursive functions, and the random module to produce the mazes.

# http://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm
# https://en.wikipedia.org/wiki/Box-drawing_character
# https://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value
# https://stackoverflow.com/questions/14895599/insert-an-element-at-specific-index-in-a-list-and-return-updated-list

# On my honor, I have neither given nor received unauthorized aid.

import random as r

def parentontop(i, j):

# how to erase the border between the frontier and the parent for the four different situations (parent on top, bottom, left or right)

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

	# check for frontiers around a "D" (Done) square and append its coordinates to the "left" (frontiers that are left) list if it isn't already in there

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

	# check for "D" (Done) squares around the chosen frontier and gather the different options (parent on top, bottom, left or right)

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

	# randomly choose one of the available options and erase the border between the frontier and the "D" square of the chosen parent direction

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

# randomly generate dimensions for the maze (5 <= dx, dy <= 25)

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

# make the openings at the top and the bottom with arrows to indicate the start and the end

a = agrid[0][2]

if a == "┬":
	agrid[0][2] = "┤"
else:
	agrid[0][2] = "┘"

agrid[0][3] = " "

b = agrid[0][4]

if b == "┬":
	agrid[0][4] = "├"
else:
	agrid[0][4] = "└"

c = agrid[-1][-3]

if c == "┴":
	agrid[-1][-3] = "├"
else:
	agrid[-1][-3] = "┌"

agrid[-1][-4] = " "

d = agrid[-1][-5]

if d == "┴":
	agrid[-1][-5] = "┤"
else:
	agrid[-1][-5] = "┐"

agrid.insert(0, [" " * 2, "╷", "↓", "╷", " " * (dx * 2 - 4)])
# https://stackoverflow.com/questions/14895599/insert-an-element-at-specific-index-in-a-list-and-return-updated-list

agrid.append([" " * (dx * 2 - 4), "╵", "↓", "╵", " " * 2])

# print the final result neatly

for i in agrid:
	for j in i:
		print(j, end = "")
	print()

# print the dimensions

print("\n" + "Width:" + str(dx), "Height:" + str(dy) + "\n")


