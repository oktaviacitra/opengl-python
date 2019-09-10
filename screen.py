from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h= 500, 500

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("2110171018 Oktavia Citra")
glClearColor(1.0, 1.0, 1.0, 0.0)
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()