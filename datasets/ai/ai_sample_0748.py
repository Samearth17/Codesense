import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

from math import pi, cos, sin

# Variables that will be used for the game
width = 15    #Maze width
height = 15   #Maze height
keyDistance = 3.0  #Distance between keys

# Define constants used to create the maze
MAZE_WALL = 0
MAZE_EXIT = 2
MAZE_EMPTY = 1

# Create the maze
maze = [
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0]
]
# The starting position
posX = 0.0
posY = 0.0

# The rotation angle of the camera
angle = 0.0

#Draw each maze world
def draw_maze():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    glTranslatef(-float(width)/2.0, -float(height)/2.0, -5.0)
    glRotatef(angle,0.0,1.0,0.0)
    glTranslatef(posX, posY, 0)

    # Draw each of the cubes in the maze
    for x in range(width):
        for y in range(height):
            # Select the appropriate shade for the cube
            if maze[y][x] == MAZE_WALL:
                glColor3f(0.0, 0.0, 0.0)
            elif maze[y][x] == MAZE_EXIT:
                glColor3f(1.0, 0.0, 0.0)
            elif maze[y][x] == MAZE_EMPTY:
                glColor3f(1.0, 1.0, 1.0)
            # Draw the cube
            glPushMatrix()
            glTranslatef(x, y, 0.0)
            draw_cube(1.0)
            glPopMatrix()

    glutSwapBuffers()

# Determine the position of the camera and key presses
def update(dt):
    global angle, posX, posY
    
    # Check for key presses
    keys = glutGetModifiers()
    if keys & GLUT_ACTIVE_ALT:
        # Rotate the camera
        angle += 5.0
    if keys & GLUT_ACTIVE_SHIFT:
        # Move the camera backward
        posX -= keyDistance * cos(angle * pi/180.0)
        posY -= keyDistance * sin(angle * pi/180.0)
    if keys & GLUT_ACTIVE_CTRL:
        # Move the camera forward
        posX += keyDistance * cos(angle * pi/180.0)
        posY += keyDistance * sin(angle * pi/180.0)

# Draw a cube. The cube is of size 1 and is centered around the origin
def draw_cube(size):
    halfSize = size / 2.0

    glBegin(GL_LINE_STRIP)
    glVertex3f(-halfSize,-halfSize, halfSize)
    glVertex3f( halfSize,-halfSize, halfSize)
    glVertex3f( halfSize, halfSize, halfSize)
    glVertex3f(-halfSize, halfSize, halfSize)
    glVertex3f(-halfSize,-halfSize, halfSize)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex3f(-halfSize,-halfSize,-halfSize)
    glVertex3f( halfSize,-halfSize,-halfSize)
    glVertex3f( halfSize, halfSize,-halfSize)
    glVertex3f(-halfSize, halfSize,-halfSize)
    glVertex3f(-halfSize,-halfSize,-halfSize)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-halfSize,-halfSize, halfSize)
    glVertex3f(-halfSize,-halfSize,-halfSize)

    glVertex3f( halfSize,-halfSize, halfSize)
    glVertex3f( halfSize,-halfSize,-halfSize)

    glVertex3f( halfSize, halfSize, halfSize)
    glVertex3f( halfSize, halfSize,-halfSize)

    glVertex3f(-halfSize, halfSize, halfSize)
    glVertex3f(-halfSize, halfSize,-halfSize)
    glEnd()