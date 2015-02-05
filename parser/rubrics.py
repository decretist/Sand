#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 5 February 2015
#
from __future__ import print_function
import re
import sys
import parse_decretum
def main():
    (canons, dictionary) = parse_decretum.parse_decretum()
    count = 0
    for canon in canons:
        for part in dictionary[canon]:
            tag = part[0]
            text = part[1]
            if tag == '<T R>':
                count += 1
                # generates Winroth's list of 389 (not 398) 'de eodem' rubrics
                # Making of Gratian's Decretum, 127
                # Uncovering Gratian Original Decretum with the help of electronic resources, 28
                if re.match('(De eodem\.)|(Item de eodem\.)|(De eodem\,.*?)', text):
                    print(canon + ': ' + text)
    print('expected 3423 rubrics, found ' + str(count) + ' rubrics', file=sys.stderr)

if __name__ == '__main__':
    main()
