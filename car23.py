from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
x=0
y=0
theta=0
WINDOW_SIZE=500
FPS=20
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
    
def drawcar():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global y

    
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,1)
    glVertex2f(x-30,y+25)
    for i in range(0,361,1):
        glVertex2f(25*math.cos(math.pi*i/180)+x-30,25*math.sin(math.pi*i/180)+y+25)
    glEnd()
    

    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex2f(25*math.cos(math.pi*theta/180)+x-30,25*math.sin(math.pi*theta/180)+y+25)
    glVertex2f(x-30,y+25)
    glEnd()
    
   
    
    
    glutSwapBuffers()

def animate(temp):
    global x
    global y
    global theta
    if(x<500):
        x=x+1
        theta=theta-10
    else:
        x=-500
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))
    
    


    
    
    




def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("drawcar")
    glutDisplayFunc(drawcar)
    glutIdleFunc(drawcar)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
    
main()