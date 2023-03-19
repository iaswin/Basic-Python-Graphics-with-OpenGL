from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import*
import math
import sys

WINDOW_SIZE=500
x=0
y=0
z=120
w=120
FPS=100



def init():
    
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
    
def drawball():
    global z
    global w
    glClear(GL_COLOR_BUFFER_BIT)
    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex2f(x,y)
    glVertex2f(120,125)
    glEnd()
    
    
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,1,0)
    glVertex2f(z,w)
    for i in range(360,-1,-1):
        glVertex2f(10*math.cos(math.pi*i/180)+z,10*math.sin(math.pi*i/180)+w)
    glEnd()
    glutSwapBuffers()
    

    
def animate(temp):
    global z
    global w
    dx=120
    dy=120
    m=dy/dx
    if(dx>dy):
        if(z>0):
            z=z-1
            w=w-m
        else:
            z=120
            w=120
    else:
        if(z>0):
            z=z-1/m
            w=w-1
        else:
            z=120
            w=120
                   
        
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("ball")
    glutDisplayFunc(drawball)
    glutIdleFunc(drawball)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()