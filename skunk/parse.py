#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 23 January 2015 -
# 9 February 2015
#
from __future__ import print_function
import re
import sys
def parse_all():
    part_list = []
    file = open('./edF.txt', 'r').read()
    m = re.search('(\<1 D\>.*?)(\<1 C\>.*?)(\<1 DC\>.*?)$', file, re.S)
    # part_list.append(parse_part_1(preprocess(m.group(1))))
    part_list.append(parse_part_2(preprocess(m.group(2))))
    # part_list.append(parse_part_3(preprocess(m.group(3))))
    return(part_list)

# D.1-101
def parse_part_1(text):
    distinction_list = []
    distinctions = re.findall('(?:\<1 D\>)(.*?)(?=\<1 D\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('(\<2 \d{1,3}\>) (\<T A\>) (.*?) (\<4 1\>.*?)$', distinction)
        distinction_list.append((m.group(1), parse_canons(m.group(4))))
    return(distinction_list)

# C.1-36
def parse_part_2(text):
    case_list = []
    cases = re.findall('(?:\<1 C\>)(.*?)(?=\<1 C\>|$)', text)
    for case in cases:
        case = case.strip(' ')
        m = re.match('(\<2 \d{1,2}\>)(\<T Q\>) (.*?) (\<3 1\>.*?)$', case)
        case_list.append((m.group(1), parse_questions(m.group(4))))
    return(case_list)

# de Consecratione
def parse_part_3(text):
    distinction_list = []
    distinctions = re.findall('(?:\<1 DC\>)(.*?)(?=\<1 DC\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('(\<2 \d\>) (\<4 1\>.*?)$', distinction)
        distinction_list.append((m.group(1), parse_canons(m.group(2))))
    return(distinction_list)

def parse_questions(text):
    questions = re.findall('(\<3 \d{1,2}\>.*?)(?=\<3 \d{1,2}\>|$)', text)
    for question in questions:
        question = question.strip(' ')
        m0 = re.match('(\<3 \d{1,2}\>) (\<T A\>) (.*?) (\<1 DP\>.*?)$', question) # C.33 q.3 (de Pen.)
        m1 = re.match('(\<3 \d{1,2}\>) (\<T A\>) (.*?) (\<4 1\>.*?)$', question)
        m2 = re.match('(\<3 \d{1,2}\>) (\<T A\>) (.*?)$', question) # C.11 q.2, C.17 q.3, C.22 q.3, C.29 q.1
        if m0:
            # parse_de_pen(question)
            pass
        elif m1:
            parse_canons(m1.group(4))
        elif m2:
            pass

# return list of canons
def parse_canons(text):
    canon_list = []
    canons = re.findall('(\<4 \d{1,3}\>.*?)(?=\<4 \d{1,3}\>|$)', text)
    for canon in canons:
        canon = canon.strip(' ')
        m = re.match('(\<4 \d{1,3}\>) (.*?)$', canon)
        if m:
            nodes = parse_nodes(m.group(2))
        else: # C.1 q.4 c.6
            m = re.match('(\<4 \d{1,3}\>)$', canon)
            nodes = []
        canon_list.append((m.group(1), nodes))
    return(canon_list)

# return list of leaf nodes (tag-text tuples)
def parse_nodes(text):
    node_list = []
    nodes = re.findall('(\<T [AIPRT]\>.*?)(?=\<T [AIPRT]\>|$)', text)
    for node in nodes:
        node =node.strip(' ')
        m = re.match('(\<T [AIPRT]\>) (.*?)$', node)
        node_list.append((m.group(1), m.group(2)))
    return(node_list)

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
