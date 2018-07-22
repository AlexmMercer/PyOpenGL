from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

vertices = [0,0.5,0,
            -0.5,-0.5,0,
            0.5,-0.5,0]

def render():
	glClear(GL_COLOR_BUFFER_BIT)
	glEnableClientState(GL_VERTEX_ARRAY)
	glVertexPointer(3, GL_FLOAT, 0, vertices)
	glDrawArrays(GL_TRIANGLES, 0, 3)
	glDisableClientState(GL_VERTEX_ARRAY)
	glutSwapBuffers()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(1334,720)
	glutCreateWindow("Tetris")
	glutInitWindowPosition(500,500)
	glClearColor(0,0,1,1)
	glutDisplayFunc(render)
	glutMainLoop()

main()
