from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import*
import sys
import math
x=0
y=0
theta=0
FPS=60
WINDOW_SIZE=500
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def line():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,1)
    glVertex2f(25*math.cos(math.pi*theta/180),25*math.sin(math.pi*theta/180))
    for i in range(0,361,1):
        glVertex2f(25*math.cos(math.pi*i/180)+25*math.cos(math.pi*theta/180),25*math.sin(math.pi*i/180)+25*math.sin(math.pi*theta/180))
    glEnd()
    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex2f(x,y)
    glVertex2f(25*math.cos(math.pi*theta/180)+x,25*math.sin(math.pi*theta/180)+y)
    glEnd()
    glFlush()
def animate(temp):
    global x
    global y
    global theta
    if(x<500):
        theta=theta-10
    else:
        x=-400
    
    
    
    
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))
    



def main():
    glutInit(sys.argv)
    glutInitWindowPosition(-500,500)
    glutInitWindowSize(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Line")
    glutDisplayFunc(line)
    glutIdleFunc(line)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()