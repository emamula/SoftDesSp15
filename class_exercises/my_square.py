

from swampy.TurtleWorld import *

def my_square(turtle, start_x, start_y, side_length):
	"""	Draws a line in turtle world

		turtle:
		start_x:
		start_y:
		side_length:
	"""

	turtle.x = start_x
	turtle.y = start_y
	turtle.heading = 90
	turtle.fd(side_length)
	turtle.heading = 0
	turtle.fd(side_length)
	turtle.heading = 270
	turtle.fd(side_length)
	turtle.heading = 180
	turtle.fd(side_length)



world = TurtleWorld()
beth = Turtle()
beth.set_pen_color('red')
my_square(beth, 100, 10, 50)
wait_for_user()