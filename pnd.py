from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
window=500
theta=270
flag=1


def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-500,500,-500,500)
    
def pend():
    x=100*math.cos(math.radians(theta))
    y=100*math.sin(math.radians(theta))
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,1)
    glBegin(GL_LINES)
    glVertex2f(0,100)
    glVertex2f(x,y)
    glEnd()
    
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,360,1):
        glVertex2f(25*math.cos(math.pi*i/180)+x,25*math.sin(math.pi*i/180)+y)
    glEnd()
    glutSwapBuffers()
    
def animate(temp):
    global flag
    global theta
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if(flag==1):
        theta=theta+2
        if(theta==350):
            flag=0
    if(flag==0):
        theta=theta-2
          
        if(theta==190):
            flag=1  
    
def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("pendulum")
    glutDisplayFunc(pend)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(pend)
    init()
    glutMainLoop()
main()