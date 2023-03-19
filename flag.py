from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
WINDOW_SIZE=500
FPS=40
x=0
y=0




def init():
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
    glClearColor(1,1,1,1)



def flag():
    global x
    global y
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1,0,1)
    glVertex2f(0,0)
    glVertex2f(0,100)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex2f(x,y)
    glVertex2f(x+60,y)
    glVertex2f(x+60,y+30)
    glVertex2f(x+0,y+30)
    glEnd()
    
    glFlush()
    
    
def animate(temp):
    global y
    if(y<60):
        y=y+1
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,0)
def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("flag")
    glutDisplayFunc(flag)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()