
#!/usr/bin/env python

import sys
import string

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()

    # convert to lowercase
    line = line.lower()

    # remove punctuation (.,;())
    line = line.translate(str.maketrans("", "", string.punctuation))

    # split the line into words, output data type list
    words = line.split()

    # we are looping over the words array and printing the word
    # with the count of 1 to the STDOUT
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        print('%s\t%s' % (word, 1))
