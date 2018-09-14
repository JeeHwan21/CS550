# https://stackoverflow.com/questions/13263951/what-is-argv-and-what-does-it-do

import sys

print("Hello, " + sys.argv[1] + " and " + sys.argv[2] + "!")

x = 5
y = 2

print(y // x)  # divide and round down
print(x % y)  # x mod y
print(x ** y)  # exponents

x = x ** y  # replacement (right gets stored in left); cannot replace an expression with a variable

