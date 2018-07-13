import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import sys
import numpy as np


def main():
	
	if not glfw.init():
		return "I can't init GLFW, sorry"
	glfw.window_hint(glfw.SAMPLES, 4)
	glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
	glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
	glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
	window = glfw.create_window(800,600,"Tetris",None,None)
	if not window:
		glfw.terminate()
	
	glfw.make_context_current(window)
	VertexArrayID = GLuint()
	glGenVertexArrays(1, VertexArrayID)
	glBindVertexArray(VertexArrayID)
	triangle = np.array([-1.0,-1.0,0.0,1.0,-1.0,0.0,0.0,1.0,0.0])
	vertexBuffer = GLuint()
	glGenBuffers(1, vertexBuffer)
	glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
	glBufferData(GL_ARRAY_BUFFER, sys.getsizeof(triangle), triangle, GL_STATIC_DRAW)
	while not glfw.window_should_close(window):
		glEnableVertexAttribArray(0)
		glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
		glVertexAttribPointer( 0,3,GL_FLOAT,GL_FALSE,0,0)
		glDrawArrays(GL_TRIANGLES,0,3)
		glDisableVertexAttribArray(0)
		glClear(GL_COLOR_BUFFER_BIT)
		glfw.swap_buffers(window)
		glfw.poll_events()
	glfw.terminate()

if __name__ == "__main__":
	main()
