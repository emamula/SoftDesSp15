def cum_sum_list(list):
	"""	
    
    >>>	cum_sum_list([4,5,6])
    [4, 9, 15]
    
    """

	x = 0
	result = []

	for x in range(len(list)):
		result.append(sum(list[0:x+1]))

	return result

if __name__ == "__main__":
	import doctest
	doctest.testmod()