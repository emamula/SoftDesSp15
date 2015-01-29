def factorials(n):
	"""
	>>> factorials('4')
	'24'
	"""
	i = 0
	x = i
	factorials = []
	
	while i < n:
		if i == 0:
			factorials.append(1)
			i = i + 1
		else:
			factorials.append(i * x)
			x = i * x
			i = i + 1

	return factorials

if __name__ == "__main__":
    import doctest
    doctest.testmod()