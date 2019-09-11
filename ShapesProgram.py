import time #Used for sleep commands
import math #Used for the sqrt (square root) command

def choice():
    choice = int(input("Menu:\nPress 1 to calculate the perimeter and area of a rectangle.\nPress\
 2 to calculate the perimeter and area of a triangle.\nPress 3 to quit.\n"))
    return choice

def rectangle():
    sside = float(input("Please enter the short side of the rectangle: "))
    lside = float(input("Please enter the long side of the rectangle: "))
    perimeter = sside * 2 + lside * 2
    area = sside * lside
    print("The perimiter of the rectangle is", perimeter, "and the area is", str(area)+".")
    time.sleep(2)
    start() #As long as all functions have already been defined once, we can move forward.
    
def triangle1():
    t1 = float(input("Please enter the first side of the triangle: "))
    t2 = float(input("Please enter the second side of the triangle: "))
    t3 = float(input("Please enter third side of the triangle: "))
    height = float(input("Please enter the height of the triangle: "))
    width = float(input("Please enter the base width of the triangle: "))
    tperi = t1 + t2 +t3
    tarea = (height * width) / 2
    print("The perimiter of the triangle is", tperi, "and the area is", str(tarea)+".")
    time.sleep(2)
    start()

def triangle2():
    t1 = float(input("Please enter the first side of the triangle: "))
    t2 = float(input("Please enter the second side of the triangle: "))
    t3 = float(input("Please enter third side of the triangle: "))
    tperi = t1 + t2 +t3
    s = tperi / 2
    tarea = math.sqrt(s * (s - t1) * (s - t2) * (s - t3)) #* signs were needed before the brackets as that is the only way Python knows to multiply
    print("The perimiter of the triangle is", tperi, "and the area is", str(tarea)+".")
    time.sleep(2)
    start()
    
def choice2():
    choice2 = int(input("Please choose your method:\nPress 1 for Basic.\n\
Press 2 for Heron's Forumla (Hint: This is quicker and relies on less info).\nPress 3 to go back.\n"))
    return choice2
    
def start():
    answer1 = choice()
    if answer1 == 1: #Parameters are used for functions, not variables 
        rectangle()  #Have to remember this!
    elif answer1 == 2:
        start2()
    elif answer1 == 3:
        print("Goodbye!")
        time.sleep(1)
        quit()
    else:
        print("Please enter a valid option.")
        time.sleep(1)
        start()

def start2():
    answer2 = choice2() #Had to make variables here for the 
    if answer2 == 1:    #choices to stop them repeating
        triangle1()
    elif answer2 == 2:
        triangle2()
    elif answer2 == 3:
        start()
    else:
        print("Please enter a valid option.")
        time.sleep(1)
        start2()

start() #Must have start command here after all functions defined
