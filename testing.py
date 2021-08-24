# Hey team!

### I'm going to list the things we need to code here
### and feel free to add a comment to put something we
### need to do as well!

import turtle
import time
import random
import numpy
from varname import nameof

### list all turtles here! ###

#this will be the main player
playerTurtle = turtle.Turtle()
playerTurtle.speed(0)  #it will move a bit slowly

#this turtle will be used to print text on the screen
textTurtle = turtle.Turtle()
textTurtle.speed(0)

#this is to access the background/screen for the game
background = playerTurtle.getscreen()
background.bgcolor('peru')  # background colour
background.setup(width=500, height=500)  # height + width

#these are the obstacles
L1 = turtle.Turtle()  #left lane obstacles
L2 = turtle.Turtle()
L3 = turtle.Turtle()
C1 = turtle.Turtle()  #center lane obstacles
C2 = turtle.Turtle()
C3 = turtle.Turtle()
R1 = turtle.Turtle()  #right lane obstacles
R2 = turtle.Turtle()
R3 = turtle.Turtle()

#obstacles should not leave a trail
L1.up()  
L2.up()  
L3.up()
C1.up()
C2.up()
C3.up()
R1.up()
R2.up()
R3.up()

L1.speed(0)

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
L1.goto(100, 0)
L2.goto(100, 0)
C1.goto(105, 0)
C2.goto(105, 0)
R1.goto(110, 0)
R2.goto(110, 0)

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

# function: what to do when left key pressed      
def left():
  if(whichLane == 2):  #center -> left lane
    moveToLeftLane()
  elif(whichLane == 3):  #right -> center lane
    moveToCenterLane()

# function: what to do when right key pressed
def right():
  if(whichLane == 2):   #center => right lane
    moveToRightLane()
  elif(whichLane == 1):   #left -> center lane
    moveToCenterLane()

gameOver = False  #we tell the system that the game is in play

#starting the game
def rungame(gameOver):

    #coordinates for all obstacles
    coordinateList = [110, 0, 110, 0, 110, 0, 105, 0, 105, 0, 105, 0, 100, 0, 100, 0, 100, 0]

    lives = 3  # 3 lives

    #while game is still playing
    while(gameOver == False):
      # check for button press
      background.listen()
      # allocate left key to moving left
      background.onkey(left, 'Left')
      # allocate right key to moving right
      background.onkey(right, 'Right')

      ##############################################
      ## 3. spawn obstacles at random starting   ###
      ##    at the horizon line                  ###
      ##############################################
        
      #check to move or place obstacle onto game
      def obstacleMovement(obstacle):
        #which obstacle to use in current iteration of function
        global lives, gameOver, coordinateList
        
        obj = obstacle 

        obstacleName = nameof(obj)  #read obstacle name

        if(obj.isvisible == False): 
          randomroll = random.randint(0,3) 
          if(randomroll == 0):   #25% chance 
            obj.showTurtle()  #spawn object

          else:  #if obstacle already spawned

          #######################################
          # decide which obstacle to adjust for #
          #######################################

            if('L1' in obstacleName):  
              xcoorInList = coordinateList[0]
              ycoorInList = coordinateList[1]
            if('L2' in obstacleName):
              xcoorInList = coordinateList[2]
              ycoorInList = coordinateList[3]
            if('L3' in obstacleName):
              xcoorInList = coordinateList[4]
              ycoorInList = coordinateList[5]
            if('C1' in obstacleName):
              xcoorInList = coordinateList[6]
              ycoorInList = coordinateList[7]
            if('C2' in obstacleName):
              xcoorInList = coordinateList[8]
              ycoorInList = coordinateList[9]
            if('C3' in obstacleName):
              xcoorInList = coordinateList[10]
              ycoorInList = coordinateList[11]
            if('R1' in obstacleName):
              xcoorInList = coordinateList[12]
              ycoorInList = coordinateList[13]
            if('R2' in obstacleName):
              xcoorInList = coordinateList[14]
              ycoorInList = coordinateList[15]
            if('R3' in obstacleName):
              xcoorInList = coordinateList[16]
              ycoorInList = coordinateList[17]

            #####################################################
            ## 4. objects should move from top to bottom and  ###
            ##    grow in size until it leaves the screen     ###
            ##    and returns to the top of the screen        ###
            #####################################################

            #all moving objects move 5 pixels toward the player
            ycoorInList - 5  
            xcoorInList - 5  #default left positioning, will adjust for center and right lanes 

            #left obstacle moves toward left lane
            if('L' in obstacleName):  
              if(obj.ycor < -275):  #if finished path, reset
                xcoorInList = 110
                ycoorInList = 0

            #center obstacle moves toward center lane
            elif('C' in obstacleName): 
              if(obj.ycor < -275):
                xcoorInList = 105
                ycoorInList = 0
              else:
                xcoorInList + 3
                
            #right obstacle moves toward right lane
            elif('R' in obstacleName): 
              if(obj.ycor < -275):
                xcoorInList = 100
                ycoorInList = 0
              else:
                xcoorInList + 6
            
            obj.goto(ycoorInList,xcoorInList) #go to new adjustment

            ######################################################
            ## 5. when the car is of a certain size(would be   ###
            ##    touching the obstacle) and the player's car   ###
            ##    is in the same lane == game over             ###
            ######################################################

            # while obstacle == collision size &&
            #         player == same lane as obstacle:
            #                life lost!
        
            collisionSpotY = -150

            if('L' in obstacleName):  
              collisionSpotX = -50

            elif('C' in obstacleName):
              collisionSpotX = -50

            elif('R' in obstacleName): 
              collisionSpotX = -50

            distance = obj.distance(collisionSpotX, collisionSpotY)

            if('L' in obstacleName):  
              if(250 >= distance >= 150 and whichLane == 1):
                global lives
                lives -=1

            elif('C' in obstacleName):
              if(250 >= distance >= 150 and whichLane == 2):
                lives -=1

            elif('R' in obstacleName):
              if(250 >= distance >= 150 and whichLane == 1):
                lives -=1
          

        #check every obstacle for movement and collisions
        obstacleMovement(L1)
        #obstacleMovement(L2)
        #obstacleMovement(L3)
        #obstacleMovement(R1)
        #obstacleMovement(R2)
        #obstacleMovement(R3)
        #obstacleMovement(C1)
        #obstacleMovement(C2)
        #obstacleMovement(C3)

        #check lives
        if lives == 0:
            gameOver = True  # no lives = game over

        turtle.mainloop()  #continue checking the code

rungame(False)  #run the game 

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
