from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
WINDOW_SIZE=500
FPS=20
x=0
y=0
theta=0
def init():
   
    glClearColor(1,1,1,1)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def pendulam():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global y
    
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1,1,0)
    glVertex2f(x,y)
    glVertex2f(20*math.cos(math.pi*theta/180)-0,20*math.sin(math.pi*theta/180)-80)
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(40*math.cos(math.pi*theta/180)-0,40*math.sin(math.pi*theta/180)-80)
    for i in range(0,361,1):
        glVertex2f(20*math.cos(math.pi*i/180)+40*math.cos(math.pi*theta/180),20*math.sin(math.pi*i/180)+40*math.sin(math.pi*theta/180)-80)
    glEnd()
    glutSwapBuffers()

def animate(temp):
    global x
    global y
    global theta
    if(x<500):
        theta=theta-10
        
    

    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0)) 
    
    
    
    

 
    













def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("drawpendulam")
    glutDisplayFunc(pendulam)
    glutIdleFunc(pendulam)
    glutTimerFunc(0,animate,0)
    
    init()
    glutMainLoop()
    
main()