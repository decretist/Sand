#!/usr/local/bin/python3
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
import re
import sys
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    toc = open('./toc.txt', 'r')
    dictionary = {}
    # (?<=...) positive lookbehind assertion.
    canons = re.findall('(?:\<T T\>|(?<=\<T T\>))(.*?)'    # canon starts with text (<T T>) tag.
        '(?:'                   # non-capturing group.
            '\<1 [CD][CP]?\>|'  # canon ends with major division,
            '\<2 \d{1,3}\>|'    # or number of major division,
            '\<3 \d{1,2}\>|'    # or number of question,
            '\<4 \d{1,3}\>|'    # or number of canon,
            '\<P 1\>|'          # or Palea,
            '\<T [AIPT]\>'      # or inscription or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    for canon in canons:
        canon = re.sub('\<S \d{1,4}\>\<L 1\> \-\d{1,4}\+', '', canon) # remove page and line number tags.
        canon = re.sub('\<P 1\> \-\[PALEA\.\+', '', canon)    # remove Palea tags.
        canon = re.sub(re.compile('\-\[.*?\]\+', re.S), '', canon)
        canon = re.sub('\-.*?\+', '', canon)
        canon = re.sub('\s+', ' ', canon)
        canon = re.sub('^\s+', '', canon) # remove leading whitespace characters
        canon = re.sub('\s+$', '', canon) # remove trailing whitespace characters
        key = toc.readline().rstrip()
        if key in dictionary:
        # if there's already a dictionary entry with this key, merge the entries
            canon = dictionary[key] + ' ' + canon
        dictionary[key] = canon

    keys = tuple(open('./toc_etc.txt', 'r'))
    for key in keys:
        key = key.rstrip()
        if dictionary[key].endswith('etc.') or dictionary[key].endswith('et cetera.'):
            # print(key)
            print(key + '\n\n' + dictionary[key] + '\n')

if __name__ == '__main__':
    main()
