def filter_out_negative_numbers(list):

	""" 

        >>> filter_out_negative_numbers([-2.0,1.0,3.0])
        [1.0,3.0]
    """

	x = 0
	n = len(list)

	for x in range(0,n):
		if list[x] < 0:
			list.remove(list[x])

	return list


if __name__ == '__main__':
    import doctest