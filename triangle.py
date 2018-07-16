from OpenGL.GLUT import *
from OpenGL.GL import *
def render():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glBegin(GL_TRIANGLES)
	glColor3f(1,0,0)
	glVertex2f(-0.5, -0.5)
	glColor3f(0,1,0)
	glVertex2f(0.5, 0.0)
	glColor3f(0,0,1)
	glVertex2f(0.0, 0.0)
	glEnd()
	glutSwapBuffers()
	
def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(800,600)
	glutInitWindowPosition(200,200)
	glutCreateWindow("Tetris in future")
	glutDisplayFunc(render)
	glClearColor(0,0,0,0)
	glutMainLoop()

main()
