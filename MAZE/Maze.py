import random as r

# ├, ┼, ┤, ┌, ┬, ┐, └, ┴, ┘, ─

agrid = [["┌", "─", "┬", "─", "┬", "─", "┐"], ["├", "─", "┼", "─", "┼", "─", "┤"], ["├", "─", "┼", "─", "┼", "─", "┤"], ["└", "─", "┴", "─", "┴", "─", "┘"]]

for i in agrid:
	for j in i:
		print(j, end = "")
	print()

left = []

cgrid = [["B"] * (3 + 2) for x in range(3 + 2)]

igrid = [["B"] * (3 + 2) for x in range(3 + 2)]

for i in range(1, 3 + 1):
	for j in range(1, 3 + 1):
		igrid[i][j] = 0

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

	for x in igrid:
		print(*x)

	print(left)

	random = r.randint(0, len(left) - 1)

	temp = left[random]

	if len(left) == 1:
		for m in range(3 + 2):
			for n in range(3 + 2):
				if igrid[m][n] == "F":
					igrid[m][n] = "D"

	for x in igrid:
		print(*x)

	left.remove(left[random])

	if len(left) > 0:

		igrid[temp[0]][temp[1]] = "D"

		frontier(temp[0], temp[1])

for x in igrid:
	print(*x)

x = r.randint(1, 3)
y = r.randint(1, 3)

print(x, y)

igrid[x][y] = "D"

frontier(x, y)

# print(left)

# for x in igrid:
# 	print(*x)