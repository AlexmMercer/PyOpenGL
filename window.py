import glfw
from OpenGL.GL import *


def main():
	
	if not glfw.init():
		return "I can't init GLFW, sorry"
	
	glfw.window_hint(glfw.SAMPLES, 4)
	glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
	glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
	glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
	glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
	window = glfw.create_window(800,600,"Tetris",None,None)
	if not window:
		glfw.terminate()
	
	glfw.make_context_current(window)
	
	while not glfw.window_should_close(window):
		glClear(GL_COLOR_BUFFER_BIT)
		glfw.swap_buffers(window)
		glfw.poll_events()
	glfw.terminate()

if __name__ == "__main__":
	main()
