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
    inscriptions = re.findall('(?:\<T I\>|(?<=\<T I\>))(.*?)'    # inscription starts with inscription tag.
        '(?:'                   # non-capturing group.
            '\<1 [CD][CP]?\>|'  # inscription ends with major division,
            '\<2 \d{1,3}\>|'    # or number of major division,
            '\<3 \d{1,2}\>|'    # or number of question,
            '\<4 \d{1,3}\>|'    # or number of canon,
            '\<P 1\>|'          # or Palea,
            '\<T [AIPT]\>'      # or inscription or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    # print('expected 1277 inscriptions, found ' + str(len(inscriptions)) + ' inscriptions', file=sys.stderr)
    for inscription in inscriptions:
        inscription = re.sub('\<S \d{1,4}\>\<L 1\> \-\d{1,4}\+', '', inscription) # remove page and line number tags.
        inscription = re.sub('\<P 1\> \-\[PALEA\.\+', '', inscription)    # remove Palea tags.
        inscription = re.sub(re.compile('\-\[.*?\]\+', re.S), '', inscription)
        inscription = re.sub('\-.*?\+', '', inscription)
        inscription = re.sub('\s+', ' ', inscription)
        inscription = re.sub('^\s+', '', inscription) # remove leading whitespace characters
        inscription = re.sub('\s+$', '', inscription) # remove trailing whitespace characters

        print(inscription)

if __name__ == '__main__':
    main()
