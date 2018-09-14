# Dollars to Yen

dollars = float(input("Dollars: "))
yen = dollars * 111.61  # * is only for floating numbers and integers
# print(type(dollars))

print("Yen: " + str(yen))  # print("Yen:", yen) - the comma creates a space

x = '5.5'

# int(x) - error

# float(x) = 5.5

x = '5'

# int(x) = 5
# float(x) = 5.

x = 3.7

# int(x) = 3

farenheit = float(input("Farenheit: "))
celcius = (farenheit - 32) * 5 / 9
print("Celcius:", celcius)
if celcius > 25:
	print("You should wear lightly today!")
else:
	print("You should wear warm clothes today!")