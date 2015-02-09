def wc(text):
    """	Print number of letters and number of words in text
    
    >>>	wc('     Hello  there'   )
    'Number of words: 2
    Number of letters: 10'
    
    """
    
    num_letters = len(text.replace(" ",""))
    num_words = len(text.split())

    result  = "Number of words: " + str(num_words) + '\n' + "Number of letters: " + str(num_letters)

    return result

wc('Hello there')

if __name__ == "__main__":
	import doctest
	doctest.testmod()