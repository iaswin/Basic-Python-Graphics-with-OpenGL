from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
Y=0
WINDOW_SIZE=500
FPS = 60
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
 
def drawBucket():
    global Y
    x=20
    y=10
    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x,y)
    glVertex2f(x+100,y)
    glVertex2f(x+100,y+40)
    glVertex2f(x,y+40)
    glEnd()
    glFlush()
    
    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x+100,y)
    glVertex2f(x+120,y)
    glVertex2f(x+120,y+200)
    glVertex2f(x+100,y+200)
    glEnd()
    glFlush()
    
    
    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x,y)
    glVertex2f(x+20,y)
    glVertex2f(x+20,y+200)
    glVertex2f(x,y+200)
    glEnd()
    glFlush()
    
    glBegin(GL_QUADS)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(x,y)
    glVertex2f(x+20,y)
    glVertex2f(x+20,y+200)
    glVertex2f(x,y+200)
    glEnd()
    glFlush()
    
    glBegin(GL_QUADS)
    glColor3f(1.0,0.0,1.0)
    glVertex2f(x+20,y+40)
    glVertex2f(x+100,y+40)
    glVertex2f(x+100,Y+41)
    glVertex2f(x+20,Y+41)
    glEnd()
    glFlush()
    
    
    glutSwapBuffers()
    
def animate(temp):
    global Y
   
    
    
    
    if(Y<180):
        Y=Y+1
    else:
        Y=0
    glutPostRedisplay()
    glutTimerFunc(int(100/FPS),animate,int(0))


def main():
    glutInit(sys.argv)
    glutInitWindowSize(-500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("circle")
    glutDisplayFunc(drawBucket)
    glutIdleFunc(drawBucket)
    glutTimerFunc(0,animate,0)
   
    init()
    glutMainLoop()
main()