import sys
import math

def fib(a):
	if a == 1:
		return 1
	elif a == 2:
		return 1
	else:
		return fib(a-1) + fib(a-2)

print(fib(int(sys.argv[1])))

def bin(a):
	sum = 0
	for x in range(len(str(a))):
		# print(sum, x, a[-x-1])
		sum = sum + math.pow(2, x) * int(a[-x-1])
	return sum

print(int(bin(sys.argv[2])))