# Hey team! 

### I'm going to list the things we need to code here
### and feel free to add a comment to put something we 
### need to do as well! 

import turtle
import time 

### list all turtles here! ###

#this will be the main player
playerTurtle = turtle.Turtle()
playerTurtle.speed(2) #it will move a bit slowly

#this turtle will print text on the screen
textTurtle = turtle.Turtle()
textTurtle.speed(0)

#this is to access the background/screen for the game
background = playerTurtle.getscreen()
background.bgcolor('peru')  #background colour
background.setup(width=500, height=500) #height + width

screen_width = background.window_width()
screen_height = background.window_height()
#can get rid of this if we dont use it(at the end)

background.setup(width=500, height=500)

screen_width = background.window_width()
screen_height = background.window_height()

#these are the obstacles
obstacle1 = turtle.Turtle()
obstacle2 = turtle.Turtle()
obstacle3 = turtle.Turtle()
obstacle4 = turtle.Turtle()
obstacle5 = turtle.Turtle()

#hide all turtles for now
playerTurtle.hideturtle()
obstacle1.hideturtle()
obstacle2.hideturtle()
obstacle3.hideturtle()
obstacle4.hideturtle()
obstacle5.hideturtle() 
textTurtle.hideturtle()

#boolean to test whether game is still going
gameOver = False

###############################
## 1. draw the background   ###  
###############################

#left edge
playerTurtle.pensize(5)
playerTurtle.up()
playerTurtle.goto(-250,-250)
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
playerTurtle.goto(87,-250)
playerTurtle.left(150)
playerTurtle.down()
playerTurtle.forward(245)

playerTurtle.up()
playerTurtle.goto(-80,-250)
playerTurtle.right(32)
playerTurtle.down()
playerTurtle.forward(306)

###################################################
##### MAYBE ADD INSTRUCTIONS WHILE THE GAME IS ####
##### LOADING/DRAWING OR SOME SORT OF INTRO    ####
###################################################

############################################
## 2. spawn the main character to move   ###
##    from left, center or right lane    ###
############################################

def inLeftLane():   #function: turtle goes to left lane
  playerTurtle.goto(-85,-180)

def inRightLane():   #function: turtle goes to right lane
  playerTurtle.goto(200,-180)

def inCenterLane():  #function: turtle goes to center lane
  playerTurtle.goto(65,-180)

playerTurtle.turtlesize(10)  #turtle is bigger
playerTurtle.up() #turtle will not leave a trail/drawing
inCenterLane()  #turtle will start in center lane

playerTurtle.showturtle() #show player on screen
playerTurtle.speed(0)  #turtle will move instantly from lane to lane without waiting

########################################################

#### MAYBE ADD A COUNTDOWN BEFORE THE PLAYER STARTS ####

# countdown 3
# wait a second 
# countdown 2
# wait a second
# countdown 1
# start shown for one second (maybe more)

#########################################################

# allocate left key to moving left
# if in left lane, cannot move left
#   do not do anything
# if in center lane move to left  
#   centerlane == false
#   left lane == true
# if in right lane move to center
#   centerlane == true
#   right lane == false

# allocate right key to right lane
# if in left lane, move to center
#   centerlane == true
#   left lane == false
# if in center lane move to right
#   centerlane == false
#   right lane == true
# if in right lane, cannot move right

##############################################
## 3. spawn obstacles at random starting   ### 
##    at the horizon line                  ###
##############################################

# randomly every 1-5 seconds,
# obstacle appears at x,y

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


# game over screen
gameOver = True
while gameOver == True:
  textTurtle.write("GAME OVER!",
                  move=False,   
                  align='center',
                  font=('Arial', 12, 'normal'))

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
