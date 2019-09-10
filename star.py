from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500
def star():
    gluLookAt (0.0,0.0,0.5,0.0,0.0,0.0,0.0,1.0,0.0)
    glBegin(GL_LINE_LOOP)
    glVertex3f (0, 0.5, 0)
    glVertex3f (-0.2, 0.2, 0)
    glVertex3f (-0.5, 0.1, 0)
    glVertex3f (-0.2, -0.1, 0)
    glVertex3f (-0.3, -0.5, 0)
    glVertex3f (0, -0.2, 0)
    glVertex3f (0.3, -0.5, 0)
    glVertex3f (0.2, -0.1, 0)
    glVertex3f (0.5, 0.1, 0)
    glVertex3f (0.2, 0.2, 0)
    glVertex3f (0, 0.5, 0)
    glEnd()
    glFlush()

def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0,1.0,-1.0,1.0,-1.0,1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    star()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("2110171018 Oktavia Citra")
glClearColor(1.0, 1.0, 1.0, 0.0)
glutDisplayFunc(screen)
glutIdleFunc(screen)
glutMainLoop()