#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 5 February 2015 -
# 6 February 2015
#
from __future__ import print_function
import re
import sys
import parse_decretum
def main():
    toc_new = []
    dictionary_new = {}
    (canons, dictionary_old) = parse_decretum.parse_decretum()
    for canon in canons:
        for part in dictionary_old[canon]:
            tag = part[0]
            text = part[1]
            if tag == '<T A>':
                if re.search('d.a.c.1', canon):
                    key = canon
                else: # special case C.16 q.2 d.a.c.8
                    key = re.sub('c.', 'd.a.c.', canon)
                toc_new.append(key)
                dictionary_new[key] = text
            if tag == '<T I>':
                key = canon + ' (i)'
                if key in dictionary_new:
                    key = canon
                    text = dictionary_new[key] + ' ' + text
                else:
                    toc_new.append(key)
                dictionary_new[key] = text
            if tag == '<T P>':
                key = re.sub('c.', 'd.p.c.', canon)
                if key in dictionary_new:
                    text = dictionary_new[key] + ' ' + text
                else:
                    toc_new.append(key)
                dictionary_new[key] = text
            if tag == '<T Q>':
                key = canon
                toc_new.append(key)
                dictionary_new[key] = text
            if tag == '<T R>':
                key = canon + ' (r)'
                toc_new.append(key)
                dictionary_new[key] = text
            if tag == '<T T>':
                key = canon
                if key in dictionary_new:
                    text = dictionary_new[key] + ' ' + text
                else:
                    toc_new.append(key)
                dictionary_new[key] = text

if __name__ == '__main__':
    main()
