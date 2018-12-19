import random

''' Instructions:
   Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''
 faveNums = [3,4,5]
 
 
''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''

holidays = ["Hangul Day", "Children's Day", "Korean Independence DAy", "Christmas", "Easter", "New Year's Day", "Veterans Day", "Thanksgiving Day", "Diawli", "All Saints' Day", "Chinese New Year", "Islamic New Year", "Chuseok", "Hangul Day"]
 
''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''
 grades = ['A','B','C','D','E']
 
 
''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
 
funny = [True] * 18

''' 5. 
   Create a list of floats, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''

salaries = [40000, 30000, 75000, 100000, 200000, 20000]
numEmployes = len(salaries)
print(numEmployes)
 
''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''

pixels = [[random.randint(0,255), random.randint(0,255), random.randint(0,255)] for i in range(4)]

print(pixels)
 
''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''
noSiblings = 0
oneSibling = 0
twoSiblings = 0
threeSiblings = 0
students = [['Jack', 'Lexy','Eva'],['Billy','Bobby'],['Jane'],['Mary'],['Joe','John']]
for x in range(len(students)):
   if len(students[x]) == 1:
      noSiblings = noSiblings + 1
   if len(students[x]) == 2:
      oneSibling = oneSibling + 1
   if len(students[x]) == 3:
      twoSiblings = twoSiblings +1
   if len(students[x]) == 4:
      threeSiblings = threeSiblings + 1

 
 
''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''

monthsOfTheYear = ["Janurary", "February," "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
 
 
''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''
 
 days = ["Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split(" ")]

 
''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
 
boolean = [True, False, 0, 1]
 
''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
 
 dorms = "Mem Nichols Pitman Squire".split(" ")
 
''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
ranValues = []
for i in range(3):
   ranValues.append(random.randint(0, 1))

 
''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''
 
suites = ['S','H','D','C']
ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split(' ')
deck = []
for x in range(len(suites)):
   for y in range(len(ranks)):
      deck.append(str(ranks[y])+str(suites[x]))
 
''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
 
dice = []
for i in range(5):
   dice.append(random.randint(1, 6))

if dice[0] == dice[1] == dice[2] == dice[3] == dice[4] == dice[5]:
   print("Yathzee")
else:
   print("Try again.")
 
''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''
listy = [14, 9, 25, 4, 6, 7, 1, 2, 3]
for x in range(len(listy)-2):
   r = x + 1
   if listy[r-1]%2 == 0 and listy[r+1]%2 != 0 and listy[r]%3 ==0:
      print('Position ' + str(r)+ ': ' + str(listy[r-1]) +', '+ str(listy[r])+ ', '+str(listy[r+1]))

 
 
''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''
 
saddleCoords = []

values = [["!"] * 7 for i in range(7)]
for i in range(1,6):
   for j in range(1,6):
      values[i][j] = random.randint(1,20)

for i in range(1,6):
   for j in range(1,6):
      if type(values[i - 1][j]) == int and values[i - 1][j] >= values[i][j] and type(values[i + 1][j]) == int and values[i + 1][j] >= values[i][j] and type(values[i][j - 1]) == int and values[i][j - 1] <= values[i][j] and type(values[i][j + 1]) == int and values[i][j + 1] <= values[i][j]:
         saddleCoords.append([i, j])

print(saddleCoords)
 
''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''
board = [[0]*8 for i in range(8)]

queen1 = [1, 7]
queen2 = [0, 6]
board[queen1[0]][queen1[1]] = 1
board[queen2[0]][queen2[1]] = 1
for x in board:
   print(*x)
print(' ')
if queen1[0] == queen2[0] or queen1[1] == queen2[1] or (queen1[1] - queen2[1]) == (queen1[0] - queen2[0]):
   print('Can Attack')
else:
   print('Cannot Attack')

 
 
''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''

reverseList = []
for i in range(len(originalList)):
   reverseList.append(originalList[-i])
 
''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''
doorknobs = ['hi', 'goodbye', 'pizza', 'doorknobs']
doorknobs[1], doorknobs[3] = doorknobs[3], doorknobs[1]
print(doorknobs) 
 
 
''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''
 
numbers = [1, 5, 2, 2, 2, 2]

temp = max(numbers)

numbers.remove(max(numbers))
numbers.append(temp)

print(numbers)
 
''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''
w = 5
h =3
list3 = [[0]*w for i in range(h)]
for x in range(w):
   for y in range(h):
      list3[y][x] = random.randint(1,100)
for x in range(w):
   for y in range(h):
      if list3[y][x]%2 != 0:
         if list3[y][x] < 10:
            list3[y][x] = 2
         if list3[y][x] >= 10:
            list3[y][x] = 22
for x in list3:
   print(*x) 
 
 
''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''
 
image = [[0] * 3 for i in range(5)]
for i in range(5):
   for j in range(3):
      image[i][j] = random.randint(0,255)
for i in range(5):
   for j in range(3):
      image[i][j] = 256 - image[i][j]

 
''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''
 
shifters = [1,2,3,4,5,6,7,8,9,10]
r = shifters[-1]
for x in range(len(shifters)):
   shifters[x-1] = shifters[x]
   if x == len(shifters)-1:
      shifters[x-1] =r 
print(shifters) 
 
''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''

peakCount = []
geography = [[0] * N for i in range(N)]

for i in range(N):
   for j in range(N):
      geography[i][j] = random.randint(50, 200)

for i in range(1, N - 1):
   for j in range(1, N - 1):
      if geography[i - 1][j] <= geography[i][j] and geography[i + 1][j] <= geography[i][j] and geography[i][j - 1] <= geography[i][j] and geography[i][j + 1] <= geography[i][j]:
         peakCount.append(0)

print(len(peakCount))

''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''

rankings = [1, 2, 3, 4, 5, 6, 7, 8]
above = 0
for x in range(len(rankings)):
   if (rankings[x]/len(rankings)) > .50:
      above += 1
print(above/len(rankings)) 
 
''' 26. 
   Given a 9-by-9 list (called sudoku) of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''

validity = []
row = []
for i in range(9):
   for j in range(9):
      if sudoku[i][j] not in row:
         row.append(sudoku[i][j])
   if len(row) == 9:
      validity.append("row" + str(i))
   row = []

column = []
for j in range(9):
   for i in range(9):
      if sudoku[i][j] not in column:
         row.append(sudoku[i][j])
   if len(column) == 9:
      validity.append("column" + str(j))
   column = []

block = []
for i in range(2):
   a = i * 3
   for j in range(0 + a, 3 + a):
      for k in range(2):
         b = k * 3
         for l in range(0 + b, 3 + b):
            if sudoku[l][j] not in block:
               block.append(sudoku[j][l])
      if len(block) == 9:
         valditiy.append("block")
      block = []

if len(validity) == 27:
   print("VALID")
else:
   print("WRONG SOLUTION")
 
'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''
for x in range(100):
   lista = []
   for x in range(100):
      lista.append(random.randint(1,10))
   for x in range(len(lista)):
      for y in range(10):
         if lista[x] == y+1:
            listb[y] = listb[y] + 1
for x in range(len(listb)):
   listb[x] = listb[x]/100

totav = 0
for x in range(len(listb)):
   totav += listb[x]
totav = totav/10
print(totav) 
 
 
''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''