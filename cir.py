from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
window=500
theta=0


def Init():
        glClearColor(0,0,0,0)
        gluOrtho2D(-500,500,-500,500)
        
def circle():
        global theta
        x=100*math.cos(math.radians(theta))
        y=100*math.sin(math.radians(theta))
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1,0,0)    
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(100*math.cos(math.radians(theta)),100*math.sin(math.radians(theta)))
        for i in range(0,360,1):
             glVertex2f(50*math.cos(math.pi*i/180)+x,50*math.sin(math.pi*i/180)+y)
        glEnd()
        glutSwapBuffers()
        
def animate(temp):
        global theta
        glutPostRedisplay()
        glutTimerFunc(int(1000/60),animate,int(0))
        if(theta<361):
            theta=theta-1
        else:
            theta=0
        
def main():
        glutInit(sys.argv)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutInitDisplayMode(GLUT_RGB)
        glutCreateWindow("circle")
        glutDisplayFunc(circle)
        glutTimerFunc(0,animate,0)
        glutIdleFunc(circle)
        Init()
        glutMainLoop()
main()