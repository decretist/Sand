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
    toc = open('./toc.txt', 'r')
    dictionary_1r = {}
    dictionary_2r = {}
    dictionary_Fr = {}
    # (?<=...) positive lookbehind assertion.
    rubrics = re.findall('(?:\<T R\>|(?<=\<T R\>))(.*?)'    # rubric starts with rubric (<T R>) tag.
        '(?:'                   # non-capturing group.
            '\<T [IPT]\>'       # rubric ends with inscription, dictum (post), or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    print('expected 3423 rubrics, found ' + str(len(rubrics)) + ' rubrics', file=sys.stderr)
    for rubric in rubrics:
        rubric = re.sub('\<P 1\> \-\[PALEA\.\+', '', rubric) # remove Palea tag.
        rubric = re.sub(re.compile('\-\[.*?\]\+', re.S), '', rubric)
        rubric = re.sub('\-.*?\+', '', rubric)
        rubric = re.sub('\s+', ' ', rubric)
        rubric = re.sub('^\s+', '', rubric) # remove leading whitespace characters
        rubric = re.sub('\s+$', '', rubric) # remove trailing whitespace characters
        key = toc.readline().rstrip()
        dictionary_Fr[key] = rubric
    #
    keys = tuple(open('./toc_1r.txt', 'r'))
    outfilename_r1 = './tmp/all_1r_rubrics.txt'
    f = open(outfilename_r1, 'w')
    for key in keys:
        key = key.rstrip()
        dictionary_1r[key] = dictionary_Fr[key]
        f.write(dictionary_1r[key] + '\n')
    f.close
    #
    keys = tuple(open('./toc_2r.txt', 'r'))
    outfilename_2r = './tmp/all_2r_rubrics.txt'
    f = open(outfilename_2r, 'w')
    for key in keys:
        key = key.rstrip()
        dictionary_2r[key] = dictionary_Fr[key]
        f.write(dictionary_2r[key] + '\n')
    f.close

if __name__ == '__main__':
    main()
