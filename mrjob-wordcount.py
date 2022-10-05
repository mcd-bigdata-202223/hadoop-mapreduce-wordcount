from mrjob.job import MRJob
import re

class MRWordCount(MRJob):

    def mapper(self, _, line): # This function is called once per line
        for word in re.split("\W+",line): # Split each word
            yield (word.lower(), 1) # Return the key (word) and the count (1)

    def reducer(self, key, values): # The key is the word - the values are the counters
        yield (key, sum(values)) # Return the word and the sum of all counters

if __name__ == '__main__':
     MRWordCount.run()