#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 23 January 2015 -
# 7 February 2015
#
from __future__ import print_function
import re
import sys
citation_stack = []
table_of_contents = []
dictionary = {}
def parse_decretum():
    file = open('./edF.txt', 'r').read()
    m = re.search('(\<1 D\>.*?)(\<1 C\>.*?)(\<1 DC\>.*?)$', file, re.S)
    parse_part_1(preprocess(m.group(1)))
    parse_part_2(preprocess(m.group(2)))
    parse_part_3(preprocess(m.group(3)))
    return(table_of_contents, dictionary)

# D.1-101
def parse_part_1(text):
    distinctions = re.findall('(?:\<1 D\>)(.*?)(?=\<1 D\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('\<2 (\d{1,3})\> (\<T A\>) (.*?) (?=\<4 1\>)', distinction)
        citation_stack.append('D.' + m.group(1))
        add_to_dictionary('d.a.c.1', (m.group(2), m.group(3)))
        parse_canons(distinction)
        citation_stack.pop()

# C.1-36
def parse_part_2(text):
    cases = re.findall('(?:\<1 C\>)(.*?)(?=\<1 C\>|$)', text)
    for case in cases:
        case = case.strip(' ')
        m = re.match('\<2 (\d{1,2})\>(\<T Q\>) (.*?) (?=\<3 1\>)', case)
        citation_stack.append('C.' + m.group(1))
        add_to_dictionary('d.init.', (m.group(2), m.group(3)))
        parse_questions(case)
        citation_stack.pop()

def parse_questions(text):
    questions = re.findall('(\<3 \d{1,2}\>.*?)(?=\<3 \d{1,2}\>|$)', text)
    for question in questions:
        question = question.strip(' ')
        m0 = re.match('\<3 (\d{1,2})\> (\<T A\>) (.*?) (?=\<1 DP\>)', question) # C.33 q.3 (de Pen.)
        m1 = re.match('\<3 (\d{1,2})\> (\<T A\>) (.*?) (?=\<4 1\>)', question)
        m2 = re.match('\<3 (\d{1,2})\> (\<T A\>) (.*?)$', question) # C.11 q.2, C.17 q.3, C.22 q.3, C.29 q.1
        if m0:
            citation_stack.append('q.' + m0.group(1))
            add_to_dictionary('d.a.c.1', (m0.group(2), m0.group(3)))
            tmp_q = citation_stack.pop() # pop 'q.3'
            tmp_C = citation_stack.pop() # pop 'C.33'
            parse_de_pen(question)
            citation_stack.append(tmp_C) # push 'C.33'
            citation_stack.append(tmp_q) # push 'q.3'
        elif m1:
            citation_stack.append('q.' + m1.group(1))
            add_to_dictionary('d.a.c.1', (m1.group(2), m1.group(3)))
            parse_canons(question)
        elif m2:
            citation_stack.append('q.' + m2.group(1))
            add_to_dictionary('d.a.c.1', (m2.group(2), m2.group(3)))
        citation_stack.pop()

# de Penitentia
def parse_de_pen(text):
    distinctions = re.findall('(?:\<1 DP\>)(.*?)(?=\<1 DP\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('\<2 (\d)\> (\<T A\>) (.*?) (?=\<4 1\>)', distinction)
        citation_stack.append('de Pen. D.' + m.group(1))
        add_to_dictionary('d.a.c.1', (m.group(2), m.group(3)))
        parse_canons(distinction)
        citation_stack.pop()

# de Consecratione
def parse_part_3(text):
    distinctions = re.findall('(?:\<1 DC\>)(.*?)(?=\<1 DC\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('\<2 (\d)\> (?=\<4 1\>)', distinction)
        citation_stack.append('de Cons. D.' + m.group(1))
        parse_canons(distinction)
        citation_stack.pop()

def parse_canons(text):
    canons = re.findall('(\<4 \d{1,3}\>.*?)(?=\<4 \d{1,3}\>|$)', text)
    for canon in canons:
        canon = canon.strip(' ')
        m = re.match('\<4 (\d{1,3})\>', canon)
        citation_stack.append('c.' + m.group(1))
        parse_tagged_texts(canon)
        citation_stack.pop()

def parse_tagged_texts(text):
    canon_id = citation_stack.pop() # e.g., 'c.1'
    parts = re.findall('(\<T [AIPRT]\>.*?)(?=\<T [AIPRT]\>|$)', text)
    for part in parts:
        part = part.strip(' ')
        m = re.match('(\<T [AIPRT]\>) (.+)', part)
        add_to_dictionary(canon_id, (m.group(1), m.group(2)))
    citation_stack.append(canon_id) # push canon_id back onto citation stack.

def add_to_dictionary(reference, payload):
    citation_stack.append(reference)
    key = ' '.join(citation_stack)
    if key in dictionary:
        dictionary[key].append(payload)
    else:
        table_of_contents.append(key)
        dictionary[key] = [payload]
    citation_stack.pop()

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
