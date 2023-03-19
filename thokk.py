from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
z=115
w=115
a=10
WINDOW_SIZE=500
FPS=60
def init():
    glClearColor(1,1,1,0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)


def drawthokk():
    x=0
    y=0
    global z
    global w
    global a
    global b
    glClear(GL_COLOR_BUFFER_BIT)
   
    glBegin(GL_QUADS)
    glVertex2f(x,y)
    glVertex2f(x+10,y)
    glVertex2f(x+10,y+100)
    glVertex2f(x,y+100)
    glEnd()
    
    
    glBegin(GL_QUADS)
    glVertex2f(x,y+100)
    glVertex2f(x,y+120)
    glVertex2f(x+100,y+120)
    glVertex2f(x+100,y+100)
    glEnd()

    
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1,0,1)
    glVertex2f(x+10,y+100)
    glVertex2f(a+1,y+50)
    glEnd()
   
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1,0,0)
    glVertex2f(z,w)
    for i in range(360,-1,-1):
        glVertex2f(10*math.cos(math.pi*i/180)+z,10*math.sin(math.pi*i/180)+w)
    glEnd()
    glutSwapBuffers()

    
def animate(temp):
    global z
    global w
    if(z<500):
        z=z+1
    else:
        z=115
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,0)
    
def animate1(temp):
    global a
    if(a<30):
        a=a+1
    else:
        a=10
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate1,0)
    









def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("thokkk")
    glutDisplayFunc(drawthokk)
    glutIdleFunc(drawthokk)
    glutTimerFunc(0,animate,0)
    glutTimerFunc(0,animate1,0) 
    init()
    glutMainLoop()
main()