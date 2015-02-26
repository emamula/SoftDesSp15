""" @Emily Mamula
    Mini-Project 3: Text Mining and Analysis
    SoftDes Spring 2015 """
import re
import nltk.data
from pattern.en import *
import matplotlib.pyplot as plt
import numpy



def process_text(filename):
    """ """

    darcy = []
    values = []

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fp = open(filename,'r')
    data = fp.read()
    sentences = tokenizer.tokenize(data)

    for x in range(0,len(sentences)):
    	sentences[x] = sentences[x].replace('\n', ' ')

    	if 'Darcy' in sentences[x]:
    		darcy.append(sentences[x])
    		values.append(sentiment(sentences[x]))
    	#print sentences[x]+'\n\n'
    
    print len(sentences)

    fig = plt.figure()
    plt.plot(train_percentages, test_accuracies)
    plt.xlabel('Percentage of Data Used for Training')
    plt.ylabel('Accuracy on Test Set')
    plt.show()


if __name__ == "__main__":
    process_text("pride_and_prejudice.txt")