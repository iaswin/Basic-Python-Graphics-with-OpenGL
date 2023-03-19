from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math


WINDOW_SIZE=500
GLOBAL_X=0
GLOBAL_Y=0
FPS=60
j=4320
k=360
def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def circle():
    global j
    global k
    global GLOBAL_X
    global GLOBAL_Y
    x=GLOBAL_X
    y=GLOBAL_Y
    i=0
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,361,1):
        glVertex2f(300*math.cos(math.pi*i/180)+x,300*math.sin(math.pi*i/180)+y)
    
    glEnd()
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,1,1)
    glVertex2f(x,y)
    glVertex2f(100*math.cos(math.pi*j/180)+x,100*math.sin(math.pi*j/180)+y)
    glEnd()
    
    
    
    glLineWidth(10)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(x,y)
    glVertex2f(150*math.cos(math.pi*k/180)+x,150*math.sin(math.pi*k/180)+y)
    glEnd()
    glutSwapBuffers()
    
def animate(temp):
    global j,k
    if(j<0 or k<0):
            j=4320
            k=360
    else:
            j=j-1
            k=k-1/12
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))
        
        
    
    
    
    
def main():
    glutInit(sys.argv)
    glutInitWindowSize(-500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("circle")
    glutDisplayFunc(circle)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(circle)
    init()
    glutMainLoop()
main()