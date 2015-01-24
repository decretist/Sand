#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 24 April 2014
# 18 January 2015
#
# unique.py | sort -n -r
#
import re
def main():
    string = open('./Gratian1.txt', 'r').read()
    words = re.split('\W', string)
    dictionary_1r = {}
    for word in words:
        if word:
            key = word.lower()
            if key in dictionary_1r:
                dictionary_1r[key] += 1
            else:
                dictionary_1r[key] = 1
        else:
            pass
    # keys = dictionary_1r.keys()
    # for key in keys:
    #     if key not in stopwords:
    #         print("%2d\t%s" % (dictionary_1r[key], key))
    string = open('./Gratian2.txt', 'r').read()
    words = re.split('\W', string)
    dictionary_2r = {}
    for word in words:
        if word:
            key = word.lower()
            if key in dictionary_2r:
                dictionary_2r[key] += 1
            else:
                dictionary_2r[key] = 1
        else:
            pass
    stoplist = open('./mgh.txt', 'r')
    stopwords = [stopword.rstrip() for stopword in stoplist.readlines()]
    keys = dictionary_2r.keys()
    for key in keys:
        if key not in dictionary_1r and key not in stopwords:
            print("%2d\t%s" % (dictionary_2r[key], key))

if __name__ == '__main__':
    main()
