from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL import shaders
import sys
import numpy as np
xR = float(input())
yR = float(input())
VERTEX_SHADER = """
attribute vec2 pos;
uniform float moveTime;
uniform float scaleTime;
uniform float angle;
uniform float xR;
uniform float yR;
vec2 rotate(vec2 pos) {
	float x = ((pos.x-xR)*cos(angle)-sin(angle)*(pos.y-yR)+xR);
	float y = ((pos.x-xR)*sin(angle)+cos(angle)*(pos.y-yR)+yR);
	return vec2(x,y);
}
void move(vec2 pos) {
	
}
void main() {
	gl_Position = vec4(rotate(pos),0,1);
}
"""
FRAGMENT_SHADER = """
uniform float time;
void main() {
	gl_FragColor = vec4(sin(2.0*time),cos(2.0*time),0,1);
}
"""
shaderProgram = None

def init():
	global VERTEX_SHADER
	global FRAGMENT_SHADER
	global shaderProgram

	vertex_shader = shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
	fragment_shader = shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)

	shaderProgram = shaders.compileProgram(vertex_shader, fragment_shader)
	buffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, buffer)
	x1 = -0.5
	y1 = -0.5
	vertices = [0.0,-0.5,
	            0.0,0.5,
	            -0.5,0.0,
    ]

	vertices = np.array(vertices, dtype = 'float32')

	buffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, buffer)
	glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

	pos = glGetAttribLocation(shaderProgram, "pos")
	glVertexAttribPointer(pos, 3, GL_FLOAT, GL_FALSE, 0, None)
	glEnableVertexAttribArray(pos)

	global ANGLE
	global TIME1
	global scaleTime
	global XR 
	global YR
	ANGLE = glGetUniformLocation(shaderProgram, "angle")
	TIME1 = glGetUniformLocation(shaderProgram,"time")
	scaleTime = glGetUniformLocation(shaderProgram,"scaleTime")
	moveTime = glGetUniformLocation(shaderProgram,"moveTime")
	XR = glGetUniformLocation(shaderProgram,"xR")
	YR = glGetUniformLocation(shaderProgram,"yR")
TIME = 0.0

def timer(x):
	global TIME
	TIME += 1/50
	glutPostRedisplay()
	glutTimerFunc(25, timer, 0)


def render():
	glClearColor(TIME % 1,1,1,1)
	glClear(GL_COLOR_BUFFER_BIT)

	glUseProgram(shaderProgram)

	glUniform1f(ANGLE, TIME)
	glUniform1f(TIME1,TIME)
	glUniform1f(scaleTime,TIME)
	glUniform1f(XR, xR)
	glUniform1f(YR, yR)
	glDrawArrays(GL_TRIANGLES, 0, 3)

	glUseProgram(0)
	glutSwapBuffers()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(640,640)
	glutInitWindowPosition(200,200)
	glutCreateWindow("Triangle")
	init()
	glutDisplayFunc(render)
	glutTimerFunc(25, timer, 0)
	glutMainLoop()

if __name__ == "__main__":
	main()
