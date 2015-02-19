

from swampy.TurtleWorld import *

def my_regular_polygon(turtle, start_x, start_y, num_sides, side_length):
	"""	Draws a line in turtle world

		turtle:
		start_x:
		start_y:
		side_length:
	"""

	turtle.x = start_x
	turtle.y = start_y
	turtle.heading = 0
	turtle.delay = .001

	for x in range(0,num_sides):
		turtle.fd(side_length)
		turtle.heading = (turtle.heading) + (360.0/num_sides)



world = TurtleWorld()
beth = Turtle()
beth.set_pen_color('red')
my_regular_polygon(beth, 10, 10, 500, 1)
wait_for_user()