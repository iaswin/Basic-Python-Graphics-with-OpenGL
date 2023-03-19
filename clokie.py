from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
x=0
y=0
theta=0
the=0
FPS=20
WINDOW_SIZE=500
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def line():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global y
    global theta
    glBegin(GL_LINE_LOOP)
    glColor3f(1,0.5,0.5)
    for i in range (0,361,1):
        glVertex2f(200*math.cos(math.pi*i/180)+x,200*math.sin(math.pi*i/180)+y)
    glEnd()
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(60*math.cos(math.pi*theta/180),60*math.sin(math.pi*theta/180))
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(90*math.cos(math.pi*the/180),90*math.sin(math.pi*the/180))
    glEnd()
    glFlush()
    



    


def animate(temp):
    global x
    global y
    global theta
    if(x<5):
        theta=theta-10


    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))

def animate1(temp):
    global x
    global y
    global the
    if(x<5):
        the=the-20


    glutPostRedisplay()
    glutTimerFunc(int(50000/FPS),animate1,int(0))




def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("clock")
    glutDisplayFunc(line)
    glutIdleFunc(line)
    glutTimerFunc(0,animate,0)
    glutTimerFunc(0,animate1,0)
    
    init()
    glutMainLoop()
    
main()