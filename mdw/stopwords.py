#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 27 January 2015
#
import re
import sys
def main():
    input = sys.stdin.read()
    output = []
    stoplist = open('./mgh.txt', 'r')
    stopwords = [stopword.rstrip() for stopword in stoplist.readlines()]
    words = re.split('\W', input)
    for word in words:
        if word != '':
            word = word.lower()
            if word not in stopwords:
                output.append(word)
    print(' '.join(output))

if __name__ == '__main__':
    main()
