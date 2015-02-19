

from swampy.TurtleWorld import *

def snow_flake_side(turtle, length, level):
	"""	Draws a line in turtle world

		turtle:
		start_x:
		start_y:
		side_length:
	"""

	turtle.x = 0
	turtle.y = 0
	turtle.heading = 0
	turtle.delay = .001

	turtle.fd(length)
	turtle.heading = 60
	turtle.fd(length)
	turtle.heading = 300
	turtle.fd(length)
	turtle.heading = 0
	turtle.fd(length)

	

	if level > 1:
		snow_flake_side(beth, length/3.0, level - 1)



world = TurtleWorld()
beth = Turtle()
beth.set_pen_color('red')
snow_flake_side(beth, 50, 10)
wait_for_user()