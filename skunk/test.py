#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 8 February 2015
#
from __future__ import print_function
import re
import sys
import parse
def main():
    (toc_Fr, dictionary_Fr) = parse.parse_all()
    for key in toc_Fr:
        print(key + ': ' + str(dictionary_Fr[key]))

if __name__ == '__main__':
    main()
