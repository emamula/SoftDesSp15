

from swampy.TurtleWorld import *

def draw_line(turtle, start_x, start_y, angle, line_length):
	"""	Draws a line in turtle world

		turtle:
		start_x:
		start_y:
		angle:
		line_length:
	"""

	turtle.x = start_x
	turtle.y = start_y
	turtle.heading = angle
	turtle.fd(line_length)


world = TurtleWorld()
beth = Turtle()
beth.set_pen_color('red')
draw_line(beth, 100, 100, 45, 50)
wait_for_user()