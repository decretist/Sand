#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 5 February 2015 -
# 8 February 2015
#
from __future__ import print_function
import re
import sys
import parse
def xform():
    toc_Fr = []
    dictionary_Fr = {}
    (canons, intermediate) = parse.parse_all()
    for canon in canons:
        for node in intermediate[canon]:
            tag = node[0]
            text = node[1]
            if tag == '<T A>':
                if re.search('d.a.c.1', canon):
                    key = canon
                else: # special case C.16 q.2 d.a.c.8
                    key = re.sub('c.', 'd.a.c.', canon)
                toc_Fr.append(key)
                dictionary_Fr[key] = text
            if tag == '<T I>':
                key = canon + ' (i)'
                if key in dictionary_Fr:
                    key = canon
                    text = dictionary_Fr[key] + ' ' + text
                else:
                    toc_Fr.append(key)
                dictionary_Fr[key] = text
            if tag == '<T P>':
                key = re.sub('c.', 'd.p.c.', canon)
                if key in dictionary_Fr:
                    text = dictionary_Fr[key] + ' ' + text
                else:
                    toc_Fr.append(key)
                dictionary_Fr[key] = text
            if tag == '<T Q>':
                key = canon
                toc_Fr.append(key)
                dictionary_Fr[key] = text
            if tag == '<T R>':
                key = canon + ' (r)'
                toc_Fr.append(key)
                dictionary_Fr[key] = text
            if tag == '<T T>':
                key = canon
                if key in dictionary_Fr:
                    text = dictionary_Fr[key] + ' ' + text
                else:
                    toc_Fr.append(key)
                dictionary_Fr[key] = text
    return(toc_Fr, dictionary_Fr)

if __name__ == '__main__':
    main()
