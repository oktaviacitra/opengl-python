from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500
def triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(100, 100)
    glVertex2f(200, 150)
    glVertex2f(300, 50)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    triangle()
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