from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL import shaders
import sys
import numpy as np
xR = float(input())
yR = float(input())
xL = 0.9
yL = 0.9
zL = 0.9
iL = 2.0
VERTEX_SHADER = """
attribute vec2 pos;
uniform float moveTime;
uniform float scaleTime;
uniform float angle;
uniform float xR;
uniform float yR;
varying vec3 position;
vec2 rotate(vec2 pos) {
	float x = ((pos.x-xR)*cos(-2.0*angle)-sin(-2.0*angle)*(pos.y-yR)+xR);
	float y = ((pos.x-xR)*sin(-2.0*angle)+cos(-2.0*angle)*(pos.y-yR)+yR);
	return vec2(x,y);
}
vec2 move(vec2 pos) {
	pos.x+=angle;
	return vec2(pos.x,pos.y);
}
vec2 scale(vec2 pos) {
     return vec2(pos.x*angle/10.0,pos.y*angle/10.0);
}
vec2 unScale(vec2 pos) {
     if(pos.x<=0.6 || pos.y <= -0.6){
     return vec2(pos.x*angle/10.0,pos.y*angle/10.0);
     }
}
void main() {
	gl_Position = vec4(scale(pos),0,1);
	position = vec3(pos,1);
}
"""
FRAGMENT_SHADER = """
uniform float time;
varying vec3 position;
uniform vec4 lightPos;
void main() {
	vec4 color = vec4(0.0,0.0,0.0,1.0);
	if(pow(position.x,2.0) + pow(position.y,2.0) + pow(position.z-1.0,2.0) <= 0.2) {
	color.b = (1.0/pow(distance(position.xyz,lightPos.xyz),2.0))*(dot(position.xyz-vec3(0,0,1),lightPos.xyz)/(sqrt(0.2)*length(lightPos.xyz)));
	color.r = (1.0/pow(distance(position.xyz,lightPos.xyz),2.0));
	}
	gl_FragColor = color;
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
	vertices = [-0.5,-0.5,-0.5,0.5,0.5,0.5,0.5,0.5,0.5,-0.5,-0.5,-0.5]

    

	vertices = np.array(vertices, dtype = 'float32')

	buffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, buffer)
	glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

	pos = glGetAttribLocation(shaderProgram, "pos")
	glVertexAttribPointer(pos, 2, GL_FLOAT, GL_FALSE, 0, None)
	glEnableVertexAttribArray(pos)

	global ANGLE
	global TIME1
	global scaleTime
	global XR 
	global YR
	global POSITION
	global LP
	LP = glGetUniformLocation(shaderProgram, "lightPos")
	POSITION = glGetUniformLocation(shaderProgram, "position")
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
	glClearColor(0,0,0,1)
	glClear(GL_COLOR_BUFFER_BIT)

	glUseProgram(shaderProgram)

	glUniform1f(ANGLE, TIME)
	glUniform1f(TIME1,TIME)
	glUniform1f(scaleTime,TIME)
	glUniform1f(XR, xR)
	glUniform1f(YR, yR)
	glUniform4f(LP,xL,yL,zL,iL)
	glDrawArrays(GL_TRIANGLES, 0, 6)

	glUseProgram(0)
	glutSwapBuffers()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(860,860)
	glutInitWindowPosition(200,200)
	glutCreateWindow("Triangle")
	init()
	glutDisplayFunc(render)
	glutTimerFunc(25, timer, 0)
	glutMainLoop()

if __name__ == "__main__":
	main()
