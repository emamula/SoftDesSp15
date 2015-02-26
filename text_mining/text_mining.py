""" @Emily Mamula
    Mini-Project 3: Text Mining and Analysis
    SoftDes Spring 2015 """

import nltk.data
from pattern.en import *
import matplotlib.pyplot as plt
import numpy



def process_text(filename, character):
    """	This function takes a text file and string as an input. The 
    	string is intended to be a character name, and the function 
    	will collect the sentiment of all sentences containing that
    	character's name. It then plots the sentiment of sentences
    	mentioning the character related to their location in the book.

    	My original concept with this was to analyze Pride and Prejudice
    	for sentiments pertaining to Mr. Darcy, a main love interest who
    	also happens to be a massive jerk. This seems to track, as many of
    	the references to him were negative.
    """

    character_ref = []
    values = []
    loc = []

    #Loads tokenizer, which spilts sentences in text apart, beautifully
    #ignoring abbreviations and other confounding elements (aka MAGIC).
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    
    with open(filename, 'r') as fp:
    	data = fp.read()
    
    #Runs text through tokenizers, separating sentences.
    sentences = tokenizer.tokenize(data)

	#Remove straggling new lines
    for x in range(0,len(sentences)):
    	sentences[x] = sentences[x].replace('\n', ' ')

    	if character in sentences[x]:
    		character_ref.append(sentences[x])

    		#Add location to loc as a percentage within text.
    		loc.append(x/float(len(sentences)) * 100)

    		#Add positive vs. negative sentiment to values.
    		values.append(sentiment(sentences[x])[0])


    fig = plt.figure()
    plt.plot(loc, values)
    plt.xlabel('Location in Book (%)')
    plt.ylabel('Sentiment')
    plt.show()


if __name__ == "__main__":
    process_text("pride_and_prejudice.txt", 'Darcy')