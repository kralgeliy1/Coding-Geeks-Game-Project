# Hey team!

### I'm going to list the things we need to code here
### and feel free to add a comment to put something we
### need to do as well!

import turtle
import time
import random

### list all turtles here! ###

#this will be the main player
playerTurtle = turtle.Turtle()
playerTurtle.speed(2)  #it will move a bit slowly

#this turtle will be used to print text on the screen
textTurtle = turtle.Turtle()
textTurtle.speed(0)

#this is to access the background/screen for the game
background = playerTurtle.getscreen()
background.bgcolor('peru')  # background colour
background.setup(width=500, height=500)  # height + width

#these are the obstacles
L1 = turtle.Turtle()  #left lane obstacles
L1.up()    #will not leave a trail
L2 = turtle.Turtle()
L2.up()

C1 = turtle.Turtle()  #center lane obstacles
C1.up()
C2 = turtle.Turtle()
C2.up()

R1 = turtle.Turtle() #right lane obstacles
R1.up()
R2 = turtle.Turtle()
R2.up()

#here are the obstacle positions 
#left positions
#Lspot1 = 
#center positions
#right positions

#hide all turtle shapes for now
playerTurtle.hideturtle()
L1.hideturtle()
L2.hideturtle()
C1.hideturtle()
C2.hideturtle()
R1.hideturtle()
R2.hideturtle()
textTurtle.hideturtle()

#bring obstacles to starting position
L1.goto(102, 0)
L2.goto(102, 0)
C1.goto(110, 0)
C2.goto(110, 0)
R1.goto(117, 0)
R2.goto(117, 0)

#importing car designs
turtle.register_shape('leftcar.gif')
turtle.register_shape('rightcar.gif')
turtle.register_shape('centercar.gif')

##############################
## 1. draw the background  ###
##############################

#left edge
playerTurtle.pensize(5)
playerTurtle.up()
playerTurtle.goto(-250, -250)
playerTurtle.left(35)
playerTurtle.down()
playerTurtle.forward(425)

#horizon line
playerTurtle.right(35)
playerTurtle.backward(335)
playerTurtle.forward(470)
playerTurtle.backward(120)

#right edge
playerTurtle.right(65)
playerTurtle.forward(300)

# middle lane
playerTurtle.up()
playerTurtle.goto(87, -250)
playerTurtle.left(150)
playerTurtle.down()
playerTurtle.forward(245)

playerTurtle.up()
playerTurtle.goto(-80, -250)
playerTurtle.right(32)
playerTurtle.down()
playerTurtle.forward(306)
playerTurtle.up()

##### MAYBE ADD INSTRUCTIONS WHILE THE GAME 
##### IS LOADING/DRAWING OR SOME SORT OF INTRO  

############################################
## 2. spawn the main character to move   ###
##    from left, center or right lane    ###
############################################

#function: turtle goes to left lane
def moveToLeftLane():
    playerTurtle.goto(-5, 0)
    playerTurtle.shape('leftcar.gif')
    #variable to keep track of which lane the car is in
    global whichLane
    whichLane = 1
    #1 = left lane
    #2 = center lane
    #3 = right lane
    print(whichLane)
    #used to check the lane the car is in

#function: turtle goes to center lane
def moveToCenterLane():
    playerTurtle.goto(-3, 0)
    playerTurtle.shape('centercar.gif')
    global whichLane
    whichLane = 2
    print(whichLane)

#function: turtle goes to right lane
def moveToRightLane():
    playerTurtle.goto(0, 0)
    playerTurtle.shape('rightcar.gif')
    global whichLane
    whichLane = 3
    print(whichLane)

#turtle starts in center lane
moveToCenterLane()

#turtle will move instantly from lane to lane without waiting
playerTurtle.speed(0)
playerTurtle.showturtle()  #player now on screen

### COUNTDOWN BEFORE THE PLAYER STARTS ####
# countdown 3
textTurtle.write("3", 
                  move=False, 
                  align='center', 
                  font=('Arial', 16, 'normal'))
time.sleep(1)  # wait a second
textTurtle.clear()

# countdown 2
textTurtle.write("2",
                  move=False, 
                  align='center', 
                  font=('Arial', 16, 'normal'))
time.sleep(1)  # wait a second
textTurtle.clear()

# countdown 1
textTurtle.write("1", 
                  move=False, 
                  align='center', 
                  font=('Arial', 16, 'normal'))
time.sleep(1)
textTurtle.clear()

# function: what to do when left key pressed      moveToLeftLane()
    elif(whichLane == 3):
        # if in right lane, move to center
        moveToCenterLane()

# function: what to do when right key pressed
def right():
    if(whichLane == 2):
        # if in center lane move to right
        moveToRightLane()
    elif(whichLane == 1):
        # if in left lane move to center
        moveToCenterLane()

gameOver = False  #we tell the system that the game is in play

#starting the game
def rungame(gameOver):
    lives = 3   # 3 lives
    while(gameOver == False):
        #check for button press
        background.listen()
        # allocate left key to moving left
        background.onkey(left, 'Left')
        # allocate right key to right lane
        background.onkey(right, 'Right')

        ##############################################
        ## 3. spawn obstacles at random starting   ###
        ##    at the horizon line                  ###
        ##############################################

        # randomly every 1-5 seconds,
        # obstacle appears at x,y

        #def placeObstacle(obstacle):
        #  obj = obstacle
        #  if(obj.isvisible == False):  #object not spawned
        #    randomroll = randInt(0,3)   #25% chance car will spawn
        #   if(randomroll == 0):
        #      obj.isvisible = True
        #  else:
        #    if(#inleftlane):
              
        #    if(#inrightlane):

        #    if(#incenterlane):            

        #####################################################
        ## 4. objects should move from top to bottom and  ###
        ##    grow in size until it leaves the screen     ###
        ##    and returns to the top of the screen        ###
        #####################################################

        # obstacle function:
        # obstacle moves one pixel
        # obstacle grows one pixel

        # while game is still playing:
        #   obstacle function keeps running

        ######################################################
        ## 5. when the car is of a certain size(would be   ###
        ##    touchingthe obstacle) and the player's car   ###
        ##    is in the same lane == game over             ###
        ######################################################

        # while obstacle == collision size &&
        #         player == same lane as obstacle:
        #                life lost!

        #def hit(obstacle):
        #  obj = obstacle #assign obstacle to usable variable
        #  if(whichLane == 1):
        #    if(obj == #collision size && whichLane == objLane):
        #      global lives
        #      lives -= 1
        #  if(whichLane == 2):
        #    if(obj == #collision size && whichLane == objLane):
        #      global lives
        #      lives -= 1
        #  if(whichLane == 3):
       #     if(obj == #collision size && whichLane == objLane):
        #      global lives
        #      lives -= 1

        #check every obstacle for create or hit
        #placeObstacle(obstacleL1)
        #hit(obstacleL1)
        #placeObstacle(obstacleL2)
        #hit(obstacleL2)
        #placeObstacle(obstacleC1)
        #hit(obstacleC2)
        #placeObstacle(obstacleR1)
        #hit(obstacleR2)

        #check if game can still be played
        if lives == 0:
            gameOver = True  # no lives = game over

        turtle.mainloop()  #continue checking the code

rungame(False)  #run the entire function above while game is not over

#present game over screen
while gameOver == True:
    textTurtle.write("GAME OVER!",
                     move=False,
                     align='center',
                     font=('Arial', 12, 'normal'))
    turtle.exitonclick()  #

##################################################
## 6. add a timer of some sort to record the   ###
##    players score maybe add 3 lives          ###
##################################################

# every millisecond = 1 point recorded
# while life lost < 0:
#     game over!

####### optional stuff ######

##################################################
## 7. make props that will travel alongside    ###
##    the road to make it look like its moving ###
##################################################

# same code as obstacle but located
# on the side of the screen without any penalties

################################################
## 8. add HCC logo as bonus that will change  ##
##    the player's car in some way            ##
################################################

# HCC spawn at random 30-60 sec interval

# special change! function:
# player changes color/design

# while HCC logo == collision size &&
#         player == same lane as HCC logo:
#                special change!
