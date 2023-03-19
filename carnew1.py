from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
GLOBAL_X=0
GLOBAL_Y=0
WINDOW_SIZE=500
FPS=60



def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)


    
    
def circle(x,y,s):
    i=0
    if(s==0):
        y=y-100-50
        x=x-50
    else:
        y=y-100-50
        x=x+50
        
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,360,1):
        glVertex2f(35*math.cos(math.pi*i/180.0)+x,35*math.sin(math.pi*i/180.0)+y)
    glEnd()
    
def rectangle(x,y):
    glBegin(GL_QUADS)
    glVertex2f(x-100,y+50)
    glVertex2f(x+100,y+50)
    glVertex2f(x+100,y-100)
    glVertex2f(x-100,y-100)
    glEnd()
    


def drawcar():
    global GLOBAL_X
    global GLOBAL_Y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    rectangle(GLOBAL_X,GLOBAL_Y)
    circle(GLOBAL_X,GLOBAL_Y,0)
    circle(GLOBAL_X,GLOBAL_Y,1)
    glutSwapBuffers()


def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global WINDOW_SIZE
    
    
    
    if(GLOBAL_X+100<WINDOW_SIZE):
        GLOBAL_X=GLOBAL_X+1
    else:
        GLOBAL_X=-490
        
    glutPostRedisplay()
    glutTimerFunc(int(100/FPS),animate,int(0))


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Car")
    glutDisplayFunc(drawcar)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()

main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    