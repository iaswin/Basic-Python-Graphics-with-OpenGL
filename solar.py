from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOW_SIZE=500
x=0
y=0
theta=0
the=0
FPS=20


def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
   


def solar():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global y
    global theta
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,0)
    glVertex2f(x,y)
    for i in range(0,361,1):
        glVertex2f(25*math.cos(math.pi*i/180)+x,25*math.sin(math.pi*i/180)+y)
    glEnd()
    
    glBegin(GL_LINE_LOOP)
    glColor3f(1,0,0)
    for i in range(0,361,1):
        glVertex2f(100*math.cos(math.pi*i/180)+x,100*math.sin(math.pi*i/180)+y)
    glEnd()
    
    
    glBegin(GL_LINE_LOOP)
    glColor3f(1,0,0)
    for i in range(0,361,1):
        glVertex2f(200*math.cos(math.pi*i/180)+x,200*math.sin(math.pi*i/180)+y)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,1,0)
    glVertex2f(100*math.cos(math.pi*theta/180),100*math.sin(math.pi*theta/180))
    for i in range(0,361,1):
        glVertex2f(25*math.cos(math.pi*i/180)+100*math.cos(math.pi*theta/180),25*math.sin(math.pi*i/180)+100*math.sin(math.pi*theta/180))
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,0)
    glVertex2f(200*math.cos(math.pi*the/180),200*math.sin(math.pi*the/180))
    for i in range(0,361,1):
        glVertex2f(25*math.cos(math.pi*i/180)+200*math.cos(math.pi*the/180),25*math.sin(math.pi*i/180)+200*math.sin(math.pi*the/180))
    glEnd()
    glFlush()

def animate(temp):
    global x
    global theta
    global the
    if(x<500):
        theta=theta-10
        the=the-20
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))
    
   
   

    
def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("solar")
    glutDisplayFunc(solar)
    glutIdleFunc(solar)
    glutTimerFunc(0,animate,0)
    
    init()
    glutMainLoop()
    
main()
    