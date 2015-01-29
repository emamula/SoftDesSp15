#print "Hello, world!"

def draw_grid():
	line = 0

	for line in range (0,11):
		if line <= 10:
			if (line == 0) or (line/5.0 == 1) or (line/5.0 == 2):
				print ("+" + " -" * 4 + " ") * 2 + "+"
				line = line + 1
			else:
				print ("|" + " " * 9) * 2 + "|"
				line = line + 1
		

draw_grid()