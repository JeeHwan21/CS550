import random

# empty list
a = []

# print list
print(a)

# add to list
a.append(5)
a.append(3)
a.append(8)
a.append(8)

print(a)

a += [1, 2, 3, 4, 5]

print (a)

# a.insert(0, [1, 2, 3, 4, 5]) : list inside a list

a = [1, 2, 3, 4, 5] + a

print(a)

# a[9]: error

# remove from list
del a[5] # deleted the 6th number
# del a[5:] - everything after 5
# a[x:] - everything after x
# a[:x] - everything up to just before x
# a[y:x] - everything from y to just before x

print(a.pop())  # can accept argument for location # deleted the last number

print(a.pop(4)) # deleted the 5th number

print(a)

print(len(a))

# remove random from list
x = random.randint(0, len(a) - 1)
del a[x]
# print(a[-1])

# print(a[-10]) does not work

y = 5
z = 10
temp = y
y = z
z = temp

y, z = 5, 10
y, z = z, y
print(y, z)

a[0], a[-1] = a[-1], a[0]

print(a)

for i in range(5):
	print(i)

for i in range(2, 10, 2):
	print(i)

sevens = []
for i in range(7, 701, 7):
	sevens.append(i)
print(*sevens, len(sevens))

for i in range(1, 101):
	print(7 * i)

b = []
for i in range(1, 5000):
	b.append(i)
print(b)  # great flexibility

c = [x for x in range(2, 5000, 2)]