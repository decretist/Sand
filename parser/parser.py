#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 23 January 2015
#
from __future__ import print_function
import re
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    f.close()
    # preprocess
    file = re.sub(re.compile('\-.*?\+', re.S), '', file) # remove comments
    file = re.sub('\<S \d{1,4}\>', '', file) # remove page number tags
    file = re.sub('\<L \d{1,2}\>', '', file) # remove line number tags
    file = re.sub('\<P 1\>|\<P 0\>', '', file) # remove Palea tags
    file = re.sub('\s+', ' ', file) # remove multiple whitespace characters
    parse_all(file.strip(' '))
# parse distinctions
def parse_all(text):
    distinctions = re.findall('(?:\<1 D\>)(.*?)(?=\<1 D\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('\<2 (\d{1,3})\> \<T A\> (.*?) (?=\<4 1\>)', distinction)
        if m:
            print('D.' + m.group(1) + ' d.a.c.1: ' + m.group(2))
# parse canons
def parse_sub(text):
    canons = re.findall('(\<4 \d{1,2}\>.*?)(?=\<4 \d{1,2}\>|$)', text)
    for canon in canons:
        print(canon.strip(' '))

if __name__ == '__main__':
    main()
