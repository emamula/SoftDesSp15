def check_fermat(a,b,c,n):
	a_n = a**n
	b_n = b**n
	c_n = c**n

	if (a_n + b_n) == c_n and  a >= 0 and b >= 0 and c>=0:
		print 'Holy smokes, Fermat was wrong!'
	else:
		print "No, that doesn't work."

def check_fermat_user():
	a = raw_input("Enter a posistive interger 'a': ")
	b = raw_input("Enter a posistive interger 'b': ")
	c = raw_input("Enter a posistive interger 'c': ")

	a_n = a**n
	b_n = b**n
	c_n = c**n

	if (a_n + b_n) == c_n and  a >= 0 and b >= 0 and c>=0:
		print 'Holy smokes, Fermat was wrong!'
	else:
		print "No, that doesn't work."