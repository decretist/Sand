#!/usr/local/bin/python3
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 24 April 2014
#
import re
def main():
    #
    # first pass
    #
    string = open('./Gratian1.txt', 'r').read()
    words = re.split('\W', string)
    dictionary = {}
    for word in words:
        if word:
            key = word.lower()
            if key in dictionary:
                count = dictionary[key]
                dictionary[key] = count + 1
            else:
                dictionary[key] = 1
        else:
            pass

    #
    # debug
    #
    # keys = dictionary.keys()
    # for key in keys:
    #     pass

    #
    # second pass
    #
    string = open('./Gratian2.txt', 'r').read()
    words = re.split('\W', string)
    for word in words:
        if word:
            key = word.lower()
            if key not in dictionary:
                print(key)
        else:
            pass

if __name__ == '__main__':
    main()
