#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 8 February 2015 -
# 11 February 2015
#
from __future__ import print_function
import re
import sys
import parse
def main():
    file = open('./edF.txt', 'r').read()
    parse.parse_all(preprocess(file))

def preprocess(text):
    text = re.sub(re.compile('\-.*?\+', re.S), '', text) # remove comments
    text = re.sub('\<S \d{1,4}\>', '', text) # remove page number tags
    text = re.sub('\<L \d{1,2}\>', '', text) # remove line number tags
    text = re.sub('\<P 1\>|\<P 0\>', '', text) # remove Palea tags
    text = re.sub('\s+', ' ', text) # remove multiple whitespace characters
    text = re.sub('\s+$', '', text) # remove trailing whitespace characters
    return(text)

if __name__ == '__main__':
    main()
