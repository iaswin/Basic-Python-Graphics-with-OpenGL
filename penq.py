from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
theta=315
FPS=60
x=0
y=0
flag=0
WINDOW_SIZE=500

def init():
    
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
    
    
def pendulam():
    
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(0,100)
    glVertex2f(100*math.cos(math.pi*theta/180),100*math.sin(math.pi*theta/180))
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,0)
    glVertex2f(100*math.cos(math.pi*theta/180),100*math.sin(math.pi*theta/180))
    for i in range(0,361,1):
        glVertex2f(20*math.cos(math.pi*i/180)+100*math.cos(math.pi*theta/180),20*math.sin(math.pi*i/180)+100*math.sin(math.pi*theta/180))
    glEnd()
    glFlush()
    
def animate(temp):
    global theta
    global flag
    
    if(flag==0):
            theta=theta-5
            if(theta==225):
                flag=1
    if(flag==1):
            theta=theta+5
            if(theta==315):
                flag=0
  
        
        
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,0)
       

    
    
    





def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,-500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("bird")
    glutDisplayFunc(pendulam)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()
    