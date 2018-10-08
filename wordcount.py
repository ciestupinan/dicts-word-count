"""
Write a program, wordcount.py, that opens a file and 
counts how many times each space-separated word occurs 
in that file. Your program should then print those counts to the screen.
"""
import string

with open() as file:
	lines = [line.split() for line in file]		# [[as,i,was,going,to,st.,ives] [i,met,a,man,]]	
	words = [word for line in lines for word in line]

	wordcount = {}
	for word in words:

		# make all words lowercase and strip of their punctuation
		word_without_punct = word.lower().strip(string.punctuation)

		# add to dict if word isn't in it with count of 1. Otherwise, increment
		wordcount[word_without_punct] = wordcount.get(word_without_punct, 0) + 1

	for k,v in wordcount.items():
		print(k,v)
