#This code uses Python Turtle library to create Fractal Design
import turtle

#define the base fractal
baseFractal="FX"

#variable lookup table
lookupTable={"X":"X+YF+", "Y":"-FX-Y"}

#define the number of levels of recursion
levelsOfRecursion=7

#this function recursively creates the fractal
def drawFractal(cmd, levelsOfRecursion):
    for command in cmd:
        #check if its a F,X or Y command
        if(command=="F"):
            turtle.forward(100/(levelsOfRecursion))
        elif command=="X" or command=="Y":
            #create newCommand by looking up the lookup table
            newCmd=lookupTable[command]
            #draw the replacement
            drawFractal(newCmd, levelsOfRecursion-1)
        elif command=="+":
            #turn left
            turtle.left(90)
        elif command=="-":
            #turn right
            turtle.right(90)

#initialize the Turtle
turtle.setup(500,500)
turtle.penup()
turtle.goto(-150,150)
turtle.pendown() 
turtle.speed(100)

#call the fractal drawing function
drawFractal(baseFractal, levelsOfRecursion)
    
#hold the screen
turtle.exitonclick()