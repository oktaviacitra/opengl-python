from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init2D(r,g,b):
    glClearColor(r, g, b, 0.0)    
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-320.0, 320.0, -240.0, 240.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    dot(50, 110, 5)
    dot(100, 110, 5)
    dot(50, 70, 5)
    glFlush()

def dot(x, y, size=1):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
    glPointSize(size)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("2110171018 Oktavia Citra")
init2D(1.0, 1.0 ,1.0)
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()