#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
from __future__ import print_function
import re
import sys
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    dictionary = {}
    # (?<=...) positive lookbehind assertion.
    rubrics = re.findall('(?:\<T R\>|(?<=\<T R\>))(.*?)'    # rubric starts with rubric tag.
        '(?:'                   # non-capturing group.
            '\<T [IPT]\>'       # rubric ends with inscription, dictum (post), or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    print('expected 3422 rubrics, found ' + str(len(rubrics)) + ' rubrics', file=sys.stderr)
    for rubric in rubrics:
        rubric = re.sub('\<P 1\> \-\[PALEA\.\+', '', rubric)    # remove Palea tags.
        rubric = re.sub(re.compile('\-\[.*?\]\+', re.S), '', rubric)
        rubric = re.sub('\-.*?\+', '', rubric)
        rubric = re.sub('\s+', ' ', rubric)
        rubric = re.sub('^\s+', '', rubric) # remove leading whitespace characters
        rubric = re.sub('\s+$', '', rubric) # remove trailing whitespace characters
        print(rubric)

if __name__ == '__main__':
    main()
