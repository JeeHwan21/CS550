# Lists Practice
# Partner 1: Esther
# Partner 2: JeeHwan

'''
    On this assignment, you should work with a partner. You must submit what you have completed at the end of the class period, but you do not need to complete any leftover problems for homework. 
 
    For some of these problems you will need to create a class; for others, you will need to use a library. 
    You do NOT need to put all your solutions in this file, however you should keep all your solutions together, clearly labeled with descriptive file names, in one folder. 
'''

### IMPORTS
import turtle


''' 1.
    Create a class, Point, that keeps track of two properties: x and y
    When a point is created, values for x and y should be provided.
 
    The methods for this class are as follows:
    rotate90: rotate the point 90° about the origin
    rotate180: rotate the point 180° about the origin
    rotaten90: rotate -90° about the origin
    translate: given 2 values, translate the point by the given amount.
    flip_horizontally: flip the point on the x-axis
    flip_vertically: flip the point on the y-axis
'''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def rotate90(self):
        self.x = self.y
        self.y = self.

    def rotate180(self):
        self.x = -self.x
        self.y = -self.y

    def rotaten90(self):
        self.x = -self.y
        self.y = self.x

    def translate(self):
    
    def flip_horizontally(self):
        self.x = self.x
        self.y = -self.y

    def flip_vertically(self):
        self.x = -self.x
        self.y = self.y



''' 2.
    Create a class, Bicycle, that keeps track of three properties: cadence, gear, speed. 
    When a Bicycle is created, cadence, gear, and speed are accepted as arguments.
 
    The methods for this class are as follows:
    set_gear: given a value, set the gear to that value
    set_cadence: given a value, set the cadence to that value
    apply_brake: given a value, decrease the speed of the bike by that value
    speed_up: given a value, increase the speed of the bike by that value
'''
class Bicyle:

    def __init__(self, cadence, gear, speed):
        self.cadence = cadence
        self.gear = gear
        self.speed = speed

    def set_gear(self, gear):
        self.gear = gear

    def set_cadence(self, cadence):
        self.cadence = cadence

    def apply_brake(self, decrease):
        self.speed -= decrease

    def speed_up(self, increase):
        self.speed += increase



''' 3.
    Create a class, student, that keeps track of four properties: energy, hunger, stress, and hours.
    These properties have a range from 0-100, except hours, which has a range from 0-24. 100 energy means they are energetic; 100 hunger means they are very hungry; 100 stress means 
    they are extremely stressed. When you create a new student, assume they have moderate hunger, low stress, a lot of energy, and 24 hours.
 
    The methods for the student class are as follows:
    study: Given a value (to adjust hours), study for that given length of time. Studying decreases energy and increases hunger based on the length of the study.
    sports: Given a value (to adjust hours), play sports for that given length of time. This decreases energy, increases hunger, and decreases stress based on the length of the sports.
    class: Given a value (to adjust hours), attend classes for a given length of time. This decreases energy, increases hunger, and increases stress based on the length of the class.
    take_test: Given a value (to adjust hours), this increases stress. 
    submit_paper: this decreases stress.
    eat_meal: Given a value (to adjust hours), this decreases stress, decreases hunger, and increases energy.
    sleep: Given a time (to adjust hours), this decreases stress, increases energy, and increases hunger.
    new_day: resets the hours in a day.
 
    You may not let a student do more than 24 hours worth of activities in a given day. 
'''

class Student:

    def __init__(self, name):
        self.hunger = 50
        self.energy = 50
        self.stress = 50
        self.name = name
        self.hours = 24

    def eat_meal(self, time):
        if time > self.hours:
            print("One cannot spend more than 24 hours a day... Choose another duration.")
        else:
            if self.hunger - time * 2 >= 0 and self.stress - time * 2 >= 0 and self.energy + time * 2 <= 100:
                self.hunger -= time * 2
                self.stress -= time * 2
                self.energy += time * 2
            else:
                print("One of " + str(self.name) + "'s values is out of range! Enter a different duration.")

            if self.hours - time == 0:
                print("You must reset the day! There are no hours left!")    
            else:
                self.hours -= time
                print("You have " + str(self.hours) + " hours left!")

    def study(self, time):
        if time > self.hours:
            print("One cannot spend more than 24 hours a day... Choose another duration.")
        else:
            if self.hunger + time * 2 <= 100 and self.stress + time * 2 <= 100 and self.energy - time * 2 >= 0:
                self.hunger += time * 2
                self.stress += time * 2
                self.energy -= time * 2
            else:
                print("One of " + str(self.name) + "'s values is out of range! Enter a different duration.")
        
            if self.hours - time == 0:
                print("You must reset the day! There are no hours left!")     
            else:
                self.hours -= time
                print("You have " + str(self.hours) + " hours left!")

    def class_(self, time):
        if time > self.hours:
            print("One cannot spend more than 24 hours a day... Choose another duration.")
        else:
            if self.hunger + time * 2 <= 100 and self.stress + time * 2 <= 100 and self.energy - time * 2 >= 0:
                self.hunger += time * 2
                self.stress += time * 2
                self.energy -= time * 2
            else:
                print("One of " + str(self.name) + "'s values is out of range! Enter a different duration.")
        
            if self.hours - time == 0:
                print("You must reset the day! There are no hours left!")     
            else:
                self.hours -= time
                print("You have " + str(self.hours) + " hours left!")




''' 4. 
    Use numpy to create an array of numbers going from 20 to 100 by increments of .25
    Then, multiply all the values in the array by 4. 
    Then. find the sum of all the values.
'''
 
 
 
 
 
''' 5.
    Use turtle to draw a star.
'''
a = 200
turtle.pd()
for i in range(5):
    turtle.fd(100)
    turtle.rt(144)
turtle.exitonclick()
 
 
 
''' 6.
    Use SymPy to determine the area of a triangle given points a, b and c.
'''
 
 
 
 
 
''' 7. 
    Use VPython to build a 3D snowman.
'''
 
 
 
 
''' Sources:
    https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html
'''