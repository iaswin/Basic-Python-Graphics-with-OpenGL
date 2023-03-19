from OpenGL.GL import*
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x=0
y=0
dx=0
dy=0

FPS=90
WINDOW_SIZE=500

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
    
    
def waterfall():
    glClear(GL_COLOR_BUFFER_BIT)
    global x 
    global y 
    glBegin(GL_TRIANGLES)
    glColor3f(1,1,0)
    glVertex2f(-40,0)
    glVertex2f(-20,0)
    glVertex2f(-30,30)
    glEnd()
    
    glBegin(GL_TRIANGLES)
    glColor3f(1,1,0)
    glVertex2f(40,0)
    glVertex2f(20,0)
    glVertex2f(30,30)
    glEnd()
    
    
    glBegin(GL_QUADS)
    glColor3f(0,0,1)
    glVertex2f(-30,30)
    glVertex2f(30,30)
    glVertex2f(x+30,y+30)
    glVertex2f(x-30,y+30)
    glEnd()
    
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex2f(dx+0,dy+40)
    glVertex2f(dx+0,dy+30)
    glEnd()
    
    
    glFlush()
    
def animate(temp):
    global dx
    global dy
    global x
    global y
    if(y>-500):
        y=y-1
        
    if(dy>-500):
        dy=dy-1
    else:
        dy=40
            
    
        
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,0)




def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,-500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("bird")
    glutDisplayFunc(waterfall)
    glutIdleFunc(waterfall)
    glutTimerFunc(0,animate,0)
    

    init()
    glutMainLoop()
main()
    