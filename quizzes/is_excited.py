def is_excited(string):
    """	
    
    >>>	is_excited('IF')
    True
    
    """
    status = False
    x = 0
    n = len(string)
    num_caps = 0

    while x < n:
        if string[x] == '!':
            status = True
        if string[x].isupper() == True:
            num_caps = num_caps + 1
            if num_caps > (n/2.0):
                status = True
        x = x + 1

    return status

if __name__ == "__main__":
	import doctest
	doctest.testmod()