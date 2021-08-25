# Hey team!

### I'm going to list the things we need to code here
### and feel free to add a comment to put something we
### need to do as well!

import turtle
import time
import random
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
L3.hideturtle()
C1.hideturtle()
C2.hideturtle()
C3.hideturtle()
R1.hideturtle()
R2.hideturtle()
R3.hideturtle()
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

    # phase = 30 ----> finish path ---> reset
    #phase = [110, 0, 110, 0, 110, 0, 105, 0, 105, 0, 105, 0, 100, 0, 100, 0, 100, 0]

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
      def obstacleMovement(turtle):
        
        #read obstacle name to understand which lane it resides
        obstacleName = nameof(turtle) 
        print(turtle.isvisible)

        if(turtle.isvisible == False):  #when object not yet spawned
          chanceOfSpawn = 3
          randomroll = random.randint(0,chanceOfSpawn) #spawn at random
          print(randomroll)
          if(randomroll == 1):   
            turtle.showTurtle()  #spawn object

          else:  #if obstacle already spawned = move certain pixels

            #all moving objects move 5 pixels toward the player at a time
            y = turtle.ycor() - 5  
            collisionSpotY = -150  #spot where player meets obstacle

            #left obstacle directions
            if('L' in obstacleName):  
              collisionSpotX = -50
              if(turtle.ycor < -275):  #if finished path, reset
                turtle.hideTurtle()
                x = 110
                y = 0
              else:   #if path not finished, move 5 pixel left
                x = turtle.xcor() - 5  

            #center obstacle directions
            elif('C' in obstacleName): 
              collisionSpotX = 45
              if(turtle.ycor < -275):  #if path finished, reset
                turtle.hideTurtle()
                x = 105
                y = 0
              else:  #if path not finished, move 2 pixel left
                x = turtle.xcor() - 2   
                
            #right obstacle directions
            elif('R' in obstacleName): 
              collisionSpotX = 140
              if(turtle.ycor < -275):  #if path finished, reset
                turtle.hideTurtle()
                x = 100
                y = 0
              else: #if path not finished, move 1 pixel right
                x = turtle.xcor() + 1  
            
            turtle.goto(x,y) #go to new adjustment

            distance = turtle.distance(collisionSpotX, collisionSpotY)

            if(5 >= distance >= 15 and whichLane == 1):
              global lives
              lives -= 1  #car + obstacle in same spot = life lost  

      #perform every obstacle for movement and collisions
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
