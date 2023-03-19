from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import *
import sys
import math
gx=100
gy=100
i=0
WINDOW_SIZE=500
FPS=100000000
gx1=0
gy1=0

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
    
def triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,1,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(gx-100,gy-100)
    glVertex2f(-(gx-gy),gx1+gy1)
    glVertex2f(gx-gy,gx1+gy1)
    glEnd()
    glutSwapBuffers()
    
    
def animate(temp):
    global gx
    global gy
    global i
    global gx1
    global gy1
    i= 1
    gx=gx*math.cos(math.radians(i))
    gy=gy*math.sin(math.radians(i))
    gx1=gx1*math.sin(math.radians(i))
    gy1=gy1*math.cos(math.radians(i))
    i=i+50
    
    if(i>=360):
        i=0
        
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))
    
    


def main():
    glutInit(sys.argv)
    glutInitWindowSize(-500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("TRIANGLE")
    glutDisplayFunc(triangle)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(triangle)
    init()
    glutMainLoop()
main()
    
    