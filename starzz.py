from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x=1
y=1
WINDOW_SIZE=500
FPS=120
def init():
   
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def line():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global y
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(x*30,0)
    glVertex2f(x*10,y*10)
    glEnd()
    
    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(x*10,y*10)
    glVertex2f(0,y*30)
    glEnd()
    
    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(0,y*30)
    glVertex2f(x*-10,y*10)
    glEnd()
    
    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(x*-10,y*10)
    glVertex2f(x*-30,0)
    glEnd()
    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(x*-30,0)
    glVertex2f(x*-10,y*-10)
    glEnd()
    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(x*-10,y*-10)
    glVertex2f(0,y*-30)
    glEnd()
    
    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(0,y*-30)
    glVertex2f(x*10,y*-10)
    glEnd()
    
    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(x*10,y*-10)
    glVertex2f(x*30,0)
    glEnd()
    
    glFlush()



def animate(temp):
    global x
    global y
    if(x<15):
        x=x+1
        y=y+1
    else:
        x=1
        y=1
    
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,0)
    
    

    
    
    
    





def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("drawcar")
    glutDisplayFunc(line)
    glutIdleFunc(line)
    glutTimerFunc(0,animate,0)
    
    
    init()
    glutMainLoop()
    
main()