#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 23 January 2015
#
from __future__ import print_function
import re
canon_number = ''
distinction_number = ''
table_of_contents = []
dictionary = {}
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    f.close()
    parse_distinctions(preprocess(file))

def parse_distinctions(text):
    global distinction_number
    distinctions = re.findall('(?:\<1 D\>)(.*?)(?=\<1 D\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('\<2 (\d{1,3})\> \<T A\> (.*?) (?=\<4 1\>)', distinction)
        distinction_number = 'D.' + m.group(1)
        # key = distinction_number + ' d.a.c.1'
        # table_of_contents.append(key)
        # dictionary[key] = m.group(2)
        parse_canons(distinction)

def parse_canons(text):
    global canon_number
    canons = re.findall('(\<4 \d{1,2}\>.*?)(?=\<4 \d{1,2}\>|$)', text)
    for canon in canons:
        canon = canon.strip(' ')
        m = re.match('\<4 (\d{1,2})\>', canon)
        canon_number = 'c.' + m.group(1)
        print(distinction_number + ' ' + canon_number + ':')
        parse_parts(canon)

def parse_parts(text):
    parts = re.findall('(\<T [AIPRT]\>.*?)(?=\<T [AIPRT]\>|$)', text)
    for part in parts:
        part = part.strip(' ')
        print(part)

def preprocess(text):
    text = re.sub(re.compile('\-.*?\+', re.S), '', text) # remove comments
    text = re.sub('\<S \d{1,4}\>', '', text) # remove page number tags
    text = re.sub('\<L \d{1,2}\>', '', text) # remove line number tags
    text = re.sub('\<P 1\>|\<P 0\>', '', text) # remove Palea tags
    text = re.sub('\s+', ' ', text) # remove multiple whitespace characters
    text = re.sub('\s+$', '', text) # remove trailing whitespace characters
    return(text)

if __name__ == '__main__':
    main()
