#!/usr/local/bin/python3
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
import re
import sys
def main():
    f = open('../../Gratian/corrections/edF.txt', 'r')
    file = f.read()
    dictionary = {}
    # (?<=...) positive lookbehind assertion.
    rubrics = re.findall('(?:\<T R\>|(?<=\<T R\>))(.*?)'    # rubric starts with rubric tag.
        '(?:'                   # non-capturing group.
            '\<1 [CD][CP]?\>|'  # rubric ends with major division,
            '\<2 \d{1,3}\>|'    # or number of major division,
            '\<3 \d{1,2}\>|'    # or number of question,
            '\<4 \d{1,3}\>|'    # or number of canon,
            '\<P 1\>|'          # or Palea,
            '\<T [AIPT]\>'      # or inscription or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    # print('expected 1277 rubrics, found ' + str(len(rubrics)) + ' rubrics', file=sys.stderr)
    for rubric in rubrics:
        rubric = re.sub('\<S \d{1,4}\>\<L 1\> \-\d{1,4}\+', '', rubric) # remove page and line number tags.
        rubric = re.sub('\<P 1\> \-\[PALEA\.\+', '', rubric)    # remove Palea tags.
        rubric = re.sub(re.compile('\-\[.*?\]\+', re.S), '', rubric)
        rubric = re.sub('\-.*?\+', '', rubric)
        rubric = re.sub('\s+', ' ', rubric)
        rubric = re.sub('^\s+', '', rubric) # remove leading whitespace characters
        rubric = re.sub('\s+$', '', rubric) # remove trailing whitespace characters

        print(rubric)

if __name__ == '__main__':
    main()
