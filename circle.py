import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500
def square():
    glBegin(GL_LINE_LOOP)
    for i in range(0, 360):
        angle = math.pi * float(i) / 180
        x = math.cos(i)
        y = math.sin(i)
        glVertex2f(250+150*x, 250+150*y)
    glEnd()
    glFlush()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def screen():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    square()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("2110171018 Oktavia Citra")
glClearColor(1.0, 1.0, 1.0, 0.0)
glutDisplayFunc(screen)
glutIdleFunc(screen)
glutMainLoop()