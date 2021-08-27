import turtle
import random
import time
from varname import nameof

#main turtle
t = turtle.Turtle()
t.shape('circle')

#this turtle will be used to print text on the screen
text = turtle.Turtle()
text.ht()
text.color('white')
text.speed(0)

#this is to access the background/screen for the game
background = t.getscreen()
background.setup(width=500, height=500)  # height + width

#import car designs + backgrounds
turtle.register_shape('centerlane.gif')
turtle.register_shape('rightlane.gif')
turtle.register_shape('leftlane.gif')

turtle.colormode(255)

#obstacle turtles
L1 = turtle.Turtle()
L2 = turtle.Turtle()
L3 = turtle.Turtle()
C1 = turtle.Turtle()
C2 = turtle.Turtle()
C3 = turtle.Turtle()
R1 = turtle.Turtle()
R2 = turtle.Turtle()
R3 = turtle.Turtle()

#hide turtles for now
L1.ht()
L2.ht()
L3.ht()
C1.ht()
C2.ht()
C3.ht()
R1.ht()
R2.ht()
R3.ht()

#turtles should not leave trails
L1.up()
L2.up()
L3.up()
C1.up()
C2.up()
C3.up()
R1.up()
R2.up()
R3.up()

#obstacles go to starting position
L1.goto(100, 0)
L2.goto(100, 0)
L3.goto(100, 0)
C1.goto(105, 0)
C2.goto(105, 0)
C3.goto(105, 0)
R1.goto(110, 0)
R2.goto(110, 0)
R3.goto(110, 0)

#variables tracking iterations
chance = 300  #chance of obstacle spawning
counter = 0  #counts each iteration
threshold = 500  #amount of iterations until change
speed = 1  #speed of obstacles
lives = 3  #lives to count
obstacle_count = 0

#random default variables to change later
#tracks collision spot
CollisionY = -150
CollisionX = -150

#tracks obstacle names/ which lane to pass
obstacleName = L1

#starting speed for turtles
L1.speed(speed)
L2.speed(speed)
L3.speed(speed)
C1.speed(speed)
C2.speed(speed)
C3.speed(speed)
R1.speed(speed)
R2.speed(speed)
R3.speed(speed)


# function: moving to left lane
def moveToLeftLane():
    t.goto(-5, 0)
    t.shape('leftlane.gif')

    #variable to keep track of which lane the car is in
    global whichLane
    whichLane = 1
    #1 = left lane
    #2 = center lane
    #3 = right lane


# function: moving to center lane
def moveToCenterLane():
    t.goto(-3, 0)
    t.shape('centerlane.gif')
    global whichLane
    whichLane = 2
    #1 = left lane
    #2 = center lane
    #3 = right lane


# function: moving to right lane
def moveToRightLane():
    t.goto(0, 0)
    t.shape('rightlane.gif')
    global whichLane
    whichLane = 3
    #1 = left lane
    #2 = center lane
    #3 = right lane


# function: what to do when left key pressed
def left():
    if (whichLane == 2):  #center -> left lane
        moveToLeftLane()
    elif (whichLane == 3):  #right -> center lane
        moveToCenterLane()


# function: what to do when right key pressed
def right():
    if (whichLane == 2):  #center => right lane
        moveToRightLane()
    elif (whichLane == 1):  #left -> center lane
        moveToCenterLane()


##############################
## 1. draw the background  ###
##############################

#left edge
t.pensize(5)
t.up()
t.goto(-250, -250)
t.left(35)
t.down()
t.forward(425)

#horizon line
t.right(35)
t.backward(335)
t.forward(470)
t.backward(120)

#right edge
t.right(65)
t.forward(300)

# middle lane
t.up()
t.goto(87, -250)
t.left(150)
t.down()
t.forward(245)

t.up()
t.goto(-80, -250)
t.right(32)
t.down()
t.forward(306)
t.up()

### COUNTDOWN BEFORE THE PLAYER STARTS ####
# countdown 3
text.write("3", move=False, align='center', font=('Arial', 16, 'normal'))
time.sleep(1)  # wait a second
text.clear()

# countdown 2
text.write("2", move=False, align='center', font=('Arial', 16, 'normal'))
time.sleep(1)  # wait a second
text.clear()

# countdown 1
text.write("1", move=False, align='center', font=('Arial', 16, 'normal'))
time.sleep(1)
text.clear()

sizeL = 1
sizeW = 1

# function: moving obstacles
def allObstacle(turtle):
    global lives, whichLane, obstacleName, obstacle_count, sizeL, sizeW  #get lives and lane travelling

    #variables establishing x-coordinates, y-coordinates and visibility of turtle
    x = turtle.xcor()  
    y = turtle.ycor()
    visible = turtle.isvisible()

    #set collision spot
    collisionY = -150

    #set next move for all obstacles in the y-direction
    y -= 5

    #if object not yet spawned
    if (visible == False):
        index = random.randint(0, chance)  #roll dice
        if (index == 0):
            turtle.st()  #if dice is 0, spawn
            visible = True  #ensure visibility is true

    #if object already spawned
    else:
        shape_list = ['triangle', 'square', 'circle', 'arrow']
        Rvalue = random.randint(0,255)
        Gvalue = random.randint(0,255)
        Bvalue = random.randint(0,255)

        if ('L' in obstacleName):  #left obstacles
            if (y == -5):
                random_shape = random.randint(0, 3)
                print(random_shape)
                turtle.shape(shape_list[random_shape])

                turtle.color((0, 0, 0), (Rvalue, Gvalue, Bvalue))

            if (y == -275):
                turtle.ht()  #if finished path, reset
                x = 110
                y = 0
                visible = False
                obstacle_count = 1
                sizeL = 0.3
                sizeW = 0.3
            else:
                x -= 5
                sizeL += 0.02
                sizeW += 0.02
            ##### COLLISION CHECK ######

            collisionX = -50

            #distance of obstacle to collision point
            distance = turtle.distance(collisionX, collisionY)

            if (0 < distance < 15):
                if (whichLane == 1):
                    lives -= 1
                    print('LIFE LOST')
                    turtle.ht()
                    visible = False

        elif ('C' in obstacleName):  #center obstacles
            if (y == -5):
                random_shape = random.randint(0, 2)
                print(random_shape)
                turtle.shape(shape_list[random_shape])
                turtle.color((0, 0, 0), (Rvalue, Gvalue, Bvalue))
            if (y == -275):
                turtle.ht()  #if finished path, reset
                x = 105
                y = 0
                visible = False
                obstacle_count += 1
                sizeL = 0.3
                sizeW = 0.3
            else:
                x -= 2
                sizeL += 0.02
                sizeW += 0.02
                

            ##### COLLISION CHECK ######

            collisionX = 45

            #obstacle to 45, -150
            distance = turtle.distance(collisionX, collisionY)

            if (5 < distance < 15):
                if (whichLane == 2):
                    lives -= 1
                    print('LIFE LOST')
                    turtle.ht()
                    visible = False

        elif ('R' in obstacleName):  #right obstacles
            if (y == -5):
                random_shape = random.randint(0, 2)
                print(random_shape)
                turtle.shape(shape_list[random_shape])

                turtle.color((0, 0, 0), (Rvalue, Gvalue, Bvalue))
            if (y == -275):
                turtle.ht()  #if finished path, reset
                x = 110
                y = 0
                visible = False
                obstacle_count += 1
                sizeL = 0.3
                sizeW = 0.3
            else:
                x += 1
                sizeL += 0.02
                sizeW += 0.02
            ##### COLLISION CHECK ######

            collisionX = 140  # horizontal collision coordinate

            #check distance of player to collision
            distance = turtle.distance(collisionX, collisionY)
            #print("Distance of right obstacle:{}".format(distance))

            if (5 < distance < 15):
                if (whichLane == 3):
                    lives -= 1
                    print('LIFE LOST')
                    turtle.ht()
                    visible = False

        turtle.goto(x, y) 
        turtle.shapesize(sizeL,sizeW)

moveToCenterLane()

def play():
    global lives, whichLane, counter, chance, threshold, speed, obstacleName

    while (lives > 0): 
        background.listen()         
        background.onkey(right, 'Left')
        background.onkey(left, 'Right')

        for i in range(9):
            #passes name to determine course of action
            #using the same function for moving an object
            if (i == 1):
                obstacleName = nameof(L1)
                allObstacle(L1)
            elif (i == 2):
                obstacleName = nameof(L2)
                allObstacle(L2)
            elif (i == 3):
                obstacleName = nameof(L3)
                allObstacle(L3)
            elif (i == 4):
                obstacleName = nameof(C1)
                allObstacle(C1)
            elif (i == 5):
                obstacleName = nameof(C2)
                allObstacle(C2)
            elif (i == 6):
                obstacleName = nameof(C3)
                allObstacle(C3)
            elif (i == 7):
                obstacleName = nameof(R1)
                allObstacle(R1)
            elif (i == 8):
                obstacleName = nameof(R2)
                allObstacle(R2)
            elif (i == 9):
                obstacleName = nameof(R3)
                allObstacle(R3)
        
        counter += 1
        if (counter == threshold):
            chance -= 20
            threshold += 1000
            speed += 1

            L1.speed(speed)  
            L2.speed(speed)  
            L3.speed(speed)
            C1.speed(speed)
            C2.speed(speed)
            C3.speed(speed)
            R1.speed(speed)
            R2.speed(speed)
            R3.speed(speed)


    gameOverScreen()
    print("Obstacles passed:", obstacle_count)
    print("Score:", counter)
    turtle.mainloop()


def gameOverScreen():
    background.onkey(None, 'Left')
    background.onkey(None, 'Right')
    text.write("GAME OVER!\n",
               move=False,
               align='center',
               font=('Arial', 14, 'normal'))


play()
