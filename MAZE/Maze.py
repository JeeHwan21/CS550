import random as r

# http://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm

# ├, ┼, ┤, ┌, ┬, ┐, └, ┴, ┘, ─, ╷, ╵, │, ╴, ╶
# https://en.wikipedia.org/wiki/Box-drawing_character

agrid = [["┌", "─", "┬", "─", "┬", "─", "┐"], ["├", "─", "┼", "─", "┼", "─", "┤"], ["├", "─", "┼", "─", "┼", "─", "┤"], ["└", "─", "┴", "─", "┴", "─", "┘"]]

for i in agrid:
	for j in i:
		print(j, end = "")
	print()

for i in agrid:
	print(*i)

left = []

igrid = [["B"] * (3 + 2) for x in range(3 + 2)]

for i in range(1, 3 + 1):
	for j in range(1, 3 + 1):
		igrid[i][j] = 0

def parentontop(i, j):
	agrid[i - 1][j * 2 - 1] = " "

	if agrid[i - 1][j * 2 - 2] == "├":
		agrid[i - 1][j * 2 - 2] = "│"
	elif agrid[i - 1][j * 2 - 2] == "┬":
		agrid[i - 1][j * 2 - 2] = "┐"
	elif agrid[i - 1][j * 2 - 2] == "┼":
		agrid[i - 1][j * 2 - 2] = "┤"	
	elif agrid[i - 1][j * 2 - 2] == "└":
		agrid[i - 1][j * 2 - 2] = "╵"
	elif agrid[i - 1][j * 2 - 2] == "┴":
		agrid[i - 1][j * 2 - 2] = "┘"
	elif agrid[i - 1][j * 2 - 2] == "┌":
		agrid[i - 1][j * 2 - 2] = "╷"
	elif agrid[i - 1][j * 2 - 2] == "╶":
		agrid[i - 1][j * 2 - 2] = " "

	if agrid[i - 1][j * 2] == "┤":
		agrid[i - 1][j * 2] = "│"
	elif agrid[i - 1][j * 2] == "┬":
		agrid[i - 1][j * 2] = "┌"
	elif agrid[i - 1][j * 2] == "┴":
		agrid[i - 1][j * 2] = "└"
	elif agrid[i - 1][j * 2] == "┼":
		agrid[i - 1][j * 2] = "├"	
	elif agrid[i - 1][j * 2] == "┘":
		agrid[i - 1][j * 2] = "╵"
	elif agrid[i - 1][j * 2] == "┐":
		agrid[i - 1][j * 2] = "╷"
	elif agrid[i - 1][j * 2] == "╴":
		agrid[i - 1][j * 2] = " "

def parentonbottom(i, j):
	agrid[i][j * 2 - 1] = " "

	if agrid[i][j * 2 - 2] == "├":
		agrid[i][j * 2 - 2] = "│"
	elif agrid[i][j * 2 - 2] == "┬":
		agrid[i][j * 2 - 2] = "┐"
	elif agrid[i][j * 2 - 2] == "┼":
		agrid[i][j * 2 - 2] = "┤"	
	elif agrid[i][j * 2 - 2] == "└":
		agrid[i][j * 2 - 2] = "╵"
	elif agrid[i][j * 2 - 2] == "┴":
		agrid[i][j * 2 - 2] = "┘"
	elif agrid[i][j * 2 - 2] == "┌":
		agrid[i][j * 2 - 2] = "╷"
	elif agrid[i][j * 2 - 2] == "╶":
		agrid[i][j * 2 - 2] = " "

	if agrid[i][j * 2] == "┤":
		agrid[i][j * 2] = "│"
	elif agrid[i][j * 2] == "┬":
		agrid[i][j * 2] = "┌"
	elif agrid[i][j * 2] == "┴":
		agrid[i][j * 2] = "└"
	elif agrid[i][j * 2] == "┼":
		agrid[i][j * 2] = "├"		
	elif agrid[i][j * 2] == "┘":
		agrid[i][j * 2] = "╵"
	elif agrid[i][j * 2] == "┐":
		agrid[i][j * 2] = "╷"
	elif agrid[i][j * 2] == "╴":
		agrid[i][j * 2] = " "

# ├, ┼, ┤, ┌, ┬, ┐, └, ┴, ┘, ─, ╷, ╵, │, ╴, ╶

def parentonleft(i, j):

	if agrid[i - 1][j * 2 - 2] == "├":
		agrid[i - 1][j * 2 - 2] = "└"
	elif agrid[i - 1][j * 2 - 2] == "┼":
		agrid[i - 1][j * 2 - 2] = "┴"
	elif agrid[i - 1][j * 2 - 2] == "┤":
		agrid[i - 1][j * 2 - 2] = "┘"
	elif agrid[i - 1][j * 2 - 2] == "┌":
		agrid[i - 1][j * 2 - 2] = "╶"
	elif agrid[i - 1][j * 2 - 2] == "┬":
		agrid[i - 1][j * 2 - 2] = "─"
	elif agrid[i - 1][j * 2 - 2] == "┐":
		agrid[i - 1][j * 2 - 2] = "╴"
	elif agrid[i - 1][j * 2 - 2] == "╷":
		agrid[i - 1][j * 2 - 2] = " "

	if agrid[i][j * 2 - 2] == "├":
		agrid[i][j * 2 - 2] = "┌"
	elif agrid[i][j * 2 - 2] == "┼":
		agrid[i][j * 2 - 2] = "┬"
	elif agrid[i][j * 2 - 2] == "┤":
		agrid[i][j * 2 - 2] = "┐"
	elif agrid[i][j * 2 - 2] == "└":
		agrid[i][j * 2 - 2] = "╶"
	elif agrid[i][j * 2 - 2] == "┴":
		agrid[i][j * 2 - 2] = "─"
	elif agrid[i][j * 2 - 2] == "┘":
		agrid[i][j * 2 - 2] = "╴"
	elif agrid[i][j * 2 - 2] == "╵":
		agrid[i][j * 2 - 2] = " "

def parentonright(i, j):

	if agrid[i - 1][j * 2] == "├":
		agrid[i - 1][j * 2] = "└"
	elif agrid[i - 1][j * 2] == "┼":
		agrid[i - 1][j * 2] = "┴"
	elif agrid[i - 1][j * 2] == "┤":
		agrid[i - 1][j * 2] = "┘"
	elif agrid[i - 1][j * 2] == "┌":
		agrid[i - 1][j * 2] = "╶"
	elif agrid[i - 1][j * 2] == "┬":
		agrid[i - 1][j * 2] = "─"
	elif agrid[i - 1][j * 2] == "┐":
		agrid[i - 1][j * 2] = "╴"
	elif agrid[i - 1][j * 2] == "╷":
		agrid[i - 1][j * 2] = " "

	if agrid[i][j * 2] == "├":
		agrid[i][j * 2] = "┌"
	elif agrid[i][j * 2] == "┼":
		agrid[i][j * 2] = "┬"
	elif agrid[i][j * 2] == "┤":
		agrid[i][j * 2] = "┐"
	elif agrid[i][j * 2] == "└":
		agrid[i][j * 2] = "╶"
	elif agrid[i][j * 2] == "┴":
		agrid[i][j * 2] = "─"
	elif agrid[i][j * 2] == "┘":
		agrid[i][j * 2] = "╴"
	elif agrid[i][j * 2] == "╵":
		agrid[i][j * 2] = " "


def frontier(i, j):

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

	print(left)

	randleftover = r.randint(0, len(left) - 1)

	temp = left[randleftover]

	left.remove(left[randleftover])  # https://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value

	print(left)

	for x in igrid:
		print(*x)

	if len(left) > 0:

		parentoptions = []

		if igrid[temp[0] - 1][temp[1]] == "D":
			parentoptions.append(1)

		if igrid[temp[0] + 1][temp[1]] == "D":
			parentoptions.append(2)

		if igrid[temp[0]][temp[1] - 1] == "D":
			parentoptions.append(3)

		if igrid[temp[0]][temp[1] + 1] == "D":
			parentoptions.append(4)

		print(parentoptions)

		ran = r.randint(0, len(parentoptions) - 1)

		if parentoptions[ran] == 1:
			parentontop(temp[0], temp[1])

		elif parentoptions[ran] == 2:
			parentonbottom(temp[0], temp[1])

		elif parentoptions[ran] == 3:
			parentonleft(temp[0], temp[1])

		elif parentoptions[ran] == 4:
			parentonright(temp[0], temp[1])

		for i in agrid:
			for j in i:
				print(j, end = "")
			print()

		igrid[temp[0]][temp[1]] = "D"

		frontier(temp[0], temp[1])

for x in igrid:
	print(*x)

x = r.randint(1, 3)
y = r.randint(1, 3)

print(x, y)

igrid[x][y] = "D"

frontier(x, y)

for i in range(1, 3 + 1):
	for j in range(1, 3 + 1):
		if igrid[i][j] == "F":
			
			parentoptions = []

			if igrid[i - 1][j] == "D":
				parentoptions.append(1)

			if igrid[i + 1][j] == "D":
				parentoptions.append(2)

			if igrid[i][j - 1] == "D":
				parentoptions.append(3)

			if igrid[i][j + 1] == "D":
				parentoptions.append(4)

			print(parentoptions)

			ran = r.randint(0, len(parentoptions) - 1)

			if parentoptions[ran] == 1:
				parentontop(i, j)

			elif parentoptions[ran] == 2:
				parentonbottom(i, j)

			elif parentoptions[ran] == 3:
				parentonleft(i, j)

			elif parentoptions[ran] == 4:
				parentonright(i, j)

for i in agrid:
	for j in i:
		print(j, end = "")
	print()