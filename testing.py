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

#this is to access the background/screen for the game
background = playerTurtle.getscreen()
background.bgcolor('peru')  #background colour
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
playerTurtle.forward(305)

############################################
## 2. spawn the main character to move   ###
##    from left, center or right lane    ###
############################################

def inLeftLane():   #function: turtle goes to left lane
  playerTurtle.goto(-85,-180)

def inRightLane():   #function: turtle goes to right lane
  playerTurtle.goto(65,-180)

def inCenterLane():  #function: turtle goes to center lane
  playerTurtle.goto(200,-180)

playerTurtle.turtlesize(10)  #turtle is bigger
playerTurtle.up() #turtle will not leave a trail/drawing
inCenterLane()  #turtle will start in center lane

playerTurtle.showturtle() #show player on screen
playerTurtle.speed(0)  #turtle will move instantly from lane to lane without waiting

##############################################
## 3. spawn obstacles at random starting   ### 
##    at the horizon line                  ###
##############################################

#####################################################
## 4. objects should move from top to bottom and  ###
##    grow in size until it leaves the screen     ###
##    and returns to the top of the screen        ###
#####################################################

######################################################
## 5. when the car is of a certain size(would be   ###
##    touchingthe obstacle) and the player's car   ###
##    is in the same lane == game over             ###
######################################################

################################################
## 6. add HCC logo as bonus that will change  ##
##    the player's car in some way            ##
################################################

##################################################
## 7. add a timer of some sort to record the   ###
##    players score maybe add 3 lives          ###
##################################################

## optional stuff

## 8. make props that will travel alongside the road to
##    make it look like its moving
