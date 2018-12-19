# # # # b = ""

# # # # for i in range(1,10):
# # # #   a = str(i) * i
# # # #   b = b + a

# # # # print(b)

# # # # for i in range (1, 111):
# # # # 	if i % 11 != 0:
# # # # 	  if i % 3 == 0 and i % 5 == 0:
# # # # 	    print("CozaLoza", end=" ")
# # # # 	  elif i % 7 == 0:
# # # # 	    print("Woza", end=" ")
# # # # 	  elif i % 5 == 0:
# # # # 	    print("Loza", end=" ")
# # # # 	  elif i % 3 == 0:
# # # # 	    print("Coza", end=" ")
# # # # 	  else:
# # # # 	    print(i, end=" ")
# # # # 	else:
# # # # 	  if i % 3 == 0 and i % 5 == 0:
# # # # 	    print("CozaLoza")
# # # # 	  elif i % 7 == 0:
# # # # 	    print("Woza")
# # # # 	  elif i % 5 == 0:
# # # # 	    print("Loza")
# # # # 	  elif i % 3 == 0:
# # # # 	    print("Coza")
# # # # 	  else:
# # # # 	    print(i)

# # # # tt = [[" "] * 30 for x in range(11)]

# # # # tt[0][0], tt[0][2] = "*", "|"
# # # # for i in range(1, 10):
# # # #   tt[0][5 + 3 * (i - 1)] = i

# # # # tt[1] = "-" * 30

# # # # for i in range(2, 11):
# # # #   tt[i][0] = i - 1
# # # #   tt[i][2] = "|"
# # # #   for j in range(1, 10):
# # # #   	tt[i][5 + 3 * (j - 1)] = j * (i - 1)
# # # #   	if j * (i - 1) > 9:
# # # #   		tt[i][4 + 3 * (j - 1)] = ""

# # # # for x in tt:
# # # # 	print(*x)

# # # # a = [["#"] * 7 for x in range(7)]

# # # # for i in range(1, 6):
# # # #   for j in range(1, 6):
# # # #     a[i][j] = " "

# # # # for x in a:
# # # # 	print(*x)

# # # # b = [[" "] * 7 for x in range(7)]

# # # # b[0] = "#" * 7
# # # # b[-1] = "#" * 7

# # # # for i in range(1, 6):
# # # #   b[i][i] = "#"
# # # #   b[i][-i-1] = "#"

# # # # for x in b:
# # # #   print(*x)

# # # # c = [[" "] * 7 for x in range(7)]

# # # # c[0] = "#" * 7
# # # # c[-1] = "#" * 7

# # # # for i in range(1, 6):
# # # #   c[i][i] = "#"
# # # #   c[i][-i-1] = "#"

# # # # for i in range(1, 6):
# # # #   c[i][0] = "#"
# # # #   c[i][-1] = "#"

# # # # for x in c:
# # # #   print(*x)

# # # # num = 13245384795208579085723049857390847

# # # # for i in range(len(str(num))):
# # # # 	print(str(num)[-(i + 1)], end=" ")

# # # # for i in range(25,49,2):
# # # #   print(i)

# # # # for i in range(12, 25):
# # # #   print(i*2 + 1)

# # # # sum = -5
# # # # while sum < 6:
# # # #   print(sum)
# # # #   sum += 1

# # # days = 4
# # # sum = 0
# # # while True:
# # #   days += 1
# # #   sum += 1
# # #   if days == 57:
# # #     break
# # # print(sum)

# # # day = 14
# # # firstDayOfVacation = 24
# # # while day < firstDayOfVacation:
# # #   if firstDayOfVacation - day == 1:
# # #     print("1 day until vacation!")
# # #   else:
# # #     print(str(firstDayOfVacation - day)+ " days until vacation")
# # #   day += 1
# # # print("Vacation has arrived!")

# # # n = 3
# # # sum = n
# # # while n > 1:
# # #   sum = sum*(n-1)
# # #   n -= 1
# # # print(sum)

# # distance = 125
# # hour = 0.00
# # while True:
# #   distance -= 24.00
# #   hour +=0.25
# #   if distance < 7.50:
# #     break

# # print(hour)

# # b = 3
# # n = 4
# # exponent = 1
# # while b > 0:
# #   exponent = exponent*n
# #   b -= 1

# # print(exponent)

# # for i in range(26):
# #   print(chr(97+i))

 
# # for i in range(97, 122):
# #   if chr(i) == "a" or chr(i) == "e" or chr(i) == "i" or chr(i) == "o" or chr(i) == "u": 
# #     print(chr(i) + " is a vowel.")
# #   else:
# #     print(chr(i) + " is a consonant.")

# b = ""

# for i in range(1,10):
#   a = str(i) * i
#   b = b + a

# print(b)

# for i in range(2,21):
#   num = 1/i
#   print("1/"+str(i)," = ",str(num))