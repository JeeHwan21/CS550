import random as r

# ├, ┼, ┤, ┌, ┬, ┐, └, ┴, ┘, ─

agrid = [["┌", "─", "┬", "─", "┬", "─", "┐"], ["├", "─", "┼", "─", "┼", "─", "┤"], ["├", "─", "┼", "─", "┼", "─", "┤"], ["└", "─", "┴", "─", "┴", "─", "┘"]]

# for i in agrid:
# 	for j in i:
# 		print(j, end = "")
# 	print()

cgrid = [["D"] * (3 + 2) for x in range(3 + 2)]

igrid = [["D"] * (3 + 2) for x in range(3 + 2)]

for i in range(1, 3 + 1):
	for j in range(1, 3 + 1):
		igrid[i][j] = 0

for x in igrid:
	print(*x)



def frontier(i, j):
	if igrid[i][j] == "D" and igrid[i - 1][j] != "D" and igrid[i + 1][j] != "D" and igrid[i][j + 1] != "D" and igrid[i][j - 1] == "D":

	if

x = r.randint(1, 3)
y = r.randint(1, 3)

while True:
	igrid[x][y] = D