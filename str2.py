from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import *
import sys
import math
a=0
b=0
WINDOW_SIZE=500
scale=20
FPS=0.2
i=0

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)


def star():
    global a
    global b 
    global scale
    x=a
    y=b
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,1,0)
    glBegin(GL_LINES)
    glVertex2f(x+0,y+80+scale)
    glVertex2f(x+scale,y+scale)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x+scale,y+scale)
    glVertex2f(x+scale+80,y+0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x+scale+80,y+0)
    glVertex2f(x+scale,y-(scale))
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x+scale,y-(scale))
    glVertex2f(x+0,y-(scale+80))
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x+0,y-(scale+80))
    glVertex2f(x-(scale),y-(scale))
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x-(scale),y-(scale))
    glVertex2f(x-(scale+80),y+0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x-(scale+80),y+0)
    glVertex2f(x-(scale),y+scale)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x-(scale),y+scale)
    glVertex2f(x+0,y+scale+80)
    
    
    glEnd()
    glutSwapBuffers()
    glFlush()
    
    

    
    
    

def main():
    glutInit(sys.argv)
    glutInitWindowSize(-500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("star")
    glutDisplayFunc(star)

    init()
    glutMainLoop()
main()
    
    
    