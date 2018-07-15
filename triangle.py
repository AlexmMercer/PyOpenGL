from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GL import shaders
import numpy as np


VERTEX_SHADER = """
#version 330

in vec4 position;

void main(){

gl_Position = position;
}
"""

FRAGMENT_SHADER = """
#version 330

void main(){

gl_FragColor = vec4(1.0,0.0,0.0,1.0);
}

"""

shaderProgram = None

def Initialize():
	global VERTEX_SHADER
	global FRAGMENT_SHADER
	global shaderProgram
	
	vertexshader = shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
	fragmentshader = shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
	shaderProgram = shaders.compileShader(vertexshader, fragmentshader)
	
	triangles = [-0.5,-0.5,0.0,
	             0.5,-0.5,0.0,
	             0.0,0.5,0.0]
	triangles = np.array(triangles, dtype = np.float32)
	VBO = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, VBO)
	glBufferData(GL_ARRAY_BUFFER, triangles.nbytes, triangles, GL_STATIC_DRAW)
	
	position = glGetAttribLocation(shaderProgram, "position")
	glVertexAttribPointer(position, 3,GL_FLOAT, GL_FALSE, 0,None)
	glEnableVertexAttribArray(position)


def render():
	glClearColor(0,0,0,1)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	glUseProgram(shaderProgram)
	glDrawArrays(GL_TRIANGLES,0,3)
	glUseProgram(0)
	
	glutSwapBuffers()
	
def main():
	glutInit()
	glutInitWindowSize(800,600)
	glutInitWindowPosition(200,200)
	glutCreateWindow("Tetris")
	Initialize()
	glutDisplayFunc(render())
	glutMainLoop()
	
	
if __name__ == "__main__":
	main()
	
