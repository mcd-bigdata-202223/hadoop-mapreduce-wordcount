#!/usr/bin/python
import sys

current_word = None
current_counter = 0

for line in sys.stdin:
    line = line.strip()
    word, counter = line.split()

    counter = int(counter)

    if current_word == word:
        current_counter += counter
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_counter))
        current_counter = counter
        current_word = word

print('%s\t%s' % (current_word, current_counter))
