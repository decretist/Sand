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
    canons = re.findall('(?:\<T T\>|(?<=\<T T\>))(.*?)'    # canon starts with text (<T T>) tag.
        '(?:'                   # non-capturing group.
            '\<1 [CD][CP]?\>|'  # canon ends with major division,
            '\<2 \d{1,3}\>|'    # or number of major division,
            '\<3 \d{1,2}\>|'    # or number of question,
            '\<4 \d{1,3}\>|'    # or number of canon,
            '\<P 1\>|'          # or Palea,
            # '\<T [AIPT]\>'    # or inscription or text tag.
            '\<T [APT]\>'      # or dicta or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    # print('expected 4392 canons, found ' + str(len(canons)) + ' canons', file=sys.stderr)
    for canon in canons:
        canon = re.sub('\<S \d{1,4}\>\<L 1\> \-\d{1,4}\+', '', canon) # remove page and line number tags.
        canon = re.sub('\<P 1\> \-\[PALEA\.\+', '', canon) # remove Palea tag.
        canon = re.sub('\<P 0\>', '', canon) # remove Palea tag.
        canon = re.sub('\<T I\>', '', canon) # remove inscription tag.
        canon = re.sub(re.compile('\-\[.*?\]\+', re.S), '', canon)
        canon = re.sub('\-.*?\+', '', canon)
        canon = re.sub('\s+', ' ', canon)
        canon = re.sub('^\s+', '', canon) # remove leading whitespace characters
        canon = re.sub('\s+$', '', canon) # remove trailing whitespace characters

        print(canon)

if __name__ == '__main__':
    main()
