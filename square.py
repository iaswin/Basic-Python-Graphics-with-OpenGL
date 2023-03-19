from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


FPS=20000000
WINDOW_SIZE=500
theta=90

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
    

def square():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)
    glVertex2f(50*math.cos(math.pi*theta/180),50*math.sin(math.pi*theta/180))
    glVertex2f(50*math.cos(math.pi*(theta+120)/180),50*math.sin(math.pi*(theta+120)/180))
    glVertex2f(50*math.cos(math.pi*(theta+240)/180),50*math.sin(math.pi*(theta+240)/180))
  
    glEnd()
    glFlush()
    
def animate(temp):
    global x
    global theta
    
    theta=theta+10
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,0)
        
    






def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,-500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("bird")
    glutDisplayFunc(square)
    glutIdleFunc(square)
    glutTimerFunc(0,animate,0)

    init()
    glutMainLoop()
main()
    