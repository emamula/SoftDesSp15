def sum_of_squares(n):
    """	
    
    >>>	sum_of_squares(4)
    30
    
    """
    
    x = 0
    sum1 = 0

    while x < n:
        sum1 = sum1 + (n**2)

    return sum1

if __name__ == "__main__":
	import doctest
	doctest.testmod()