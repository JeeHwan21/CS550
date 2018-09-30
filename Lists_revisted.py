# Two-dimensional Lists

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(a[1][0])

i = []

for i in range(10):
	i.append(0)

print(i)

i = [0] * 10

print(i)

i = [[0] * 10 for x in range(10)]

# i = []
# for x in range(10):
# 	k = [0] * 10
# 	i.append(k)

for x in i:
	print(*x)

