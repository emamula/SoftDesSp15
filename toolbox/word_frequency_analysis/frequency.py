""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	words = []

	#open file and readf lines
	f = open(file_name,'r')
	lines = f.readlines()

	#remove gutengerg's pre-text
	curr_line = 0

	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1

	lines = lines[curr_line+1:]

	#remove punctuation, split lines to get words, and cast 
	#all words to lowercase
	for line in lines:
		for p in string.punctuation:
			line = line.replace(p,"")

		words_in_line = line.split()

		for word in words_in_line:
			words.append(word.lower())

	return words


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_count = {}
	top_n_words = []

	for word in word_list:
		if word in word_count:
			word_count[word] += 1

		if word not in word_count:
			word_count[word] = 1

	ordered_by_frequency = sorted(word_count, key = word_count.get, reverse = True)

	for x in range(0,n):
		top_n_words.append(ordered_by_frequency[x])

	return top_n_words


if __name__ == "__main__":
    print get_top_n_words(get_word_list("grimm.txt"), 100)