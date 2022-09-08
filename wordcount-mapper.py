#!/usr/bin/python
import sys
for line in sys.stdin: # For each line
    line = line.strip() # Remove any leading or trailing whitespaces
    line = line.lower() # Convert all uppercase characters to lowercase
    words = line.split() # Split all words
    for word in words: # For each word
        print('%s\t%s' % (word, 1)) # Print the word followed by 1 occurrence
