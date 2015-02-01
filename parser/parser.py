#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 23 January 2015
#
from __future__ import print_function
import re
import sys
citation_stack = []
table_of_contents = []
dictionary = {}
def main():
    parse_distinctions(preprocess(open('./part1.txt', 'r').read()))
    parse_cases(preprocess(open('./part2.txt', 'r').read()))

def parse_distinctions(text):
    distinctions = re.findall('(?:\<1 D\>)(.*?)(?=\<1 D\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('\<2 (\d{1,3})\> \<T A\> (.*?) (?=\<4 1\>)', distinction)
        citation_stack.append('D.' + m.group(1))
        add_to_dictionary('d.a.c.1', m.group(2))
        parse_canons(distinction)
        citation_stack.pop()

def parse_cases(text):
    cases = re.findall('(?:\<1 C\>)(.*?)(?=\<1 C\>|$)', text)
    for case in cases:
        case = case.strip(' ')
        m = re.match('\<2 (\d{1,2})\><T Q> (.*?) (?=\<3 1\>)', case)
        citation_stack.append('C.' + m.group(1))
        add_to_dictionary('d.init.', m.group(2))
        parse_questions(case)
        citation_stack.pop()

def parse_questions(text):
    questions = re.findall('(\<3 \d{1,2}\>.*?)(?=\<3 \d{1,2}\>|$)', text)
    for question in questions:
        question = question.strip(' ')
        m = re.match('\<3 (\d{1,2})\> \<T A\> (.*?) (?=\<4 1\>)', question)
        if m:
            citation_stack.append('q.' + m.group(1))
            add_to_dictionary('d.a.c.1', m.group(2))
            parse_canons(question)
            citation_stack.pop()
        else:
            parse_special_case_question(question)

def parse_special_case_question(question):
    # parse special-case questions C.11 q.2, C.17 q.3, C.22 q.3, C.29 q.1, 
    # and C.33 q.3 (de Pen.)
    m = re.match('\<3 (\d{1,2})\> \<T A\> (.+)', question)
    citation_stack.append('q.' + m.group(1))
    add_to_dictionary('d.a.c.1', m.group(2))
    citation = ' '.join(citation_stack)
    if citation == 'C.33 q.3': # de Pen.
        tmp_q = citation_stack.pop() # pop 'q.3'
        tmp_C = citation_stack.pop() # pop 'C.33'
        parse_de_penitentia(preprocess(open('./de_penitentia.txt', 'r').read()))
        citation_stack.append(tmp_C) # push 'C.33'
        citation_stack.append(tmp_q) # push 'q.3'
    citation_stack.pop()

def parse_de_penitentia(text):
    distinctions = re.findall('(?:\<1 DP\>)(.*?)(?=\<1 DP\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('\<2 (\d{1,3})\> \<T A\> (.*?) (?=\<4 1\>)', distinction)
        citation_stack.append('de Pen. D.' + m.group(1))
        add_to_dictionary('d.a.c.1', m.group(2))
        parse_canons(distinction)
        citation_stack.pop()

def parse_canons(text):
    canons = re.findall('(\<4 \d{1,3}\>.*?)(?=\<4 \d{1,3}\>|$)', text)
    for canon in canons:
        canon = canon.strip(' ')
        m = re.match('\<4 (\d{1,3})\>', canon)
        citation_stack.append('c.' + m.group(1))
        parse_parts(canon)

def parse_parts(text):
    T_P_flag = False
    T_T_flag = False
    canon_number = citation_stack.pop()
    parts = re.findall('(\<T [AIPRT]\>.*?)(?=\<T [AIPRT]\>|$)', text)
    for part in parts:
        part = part.strip(' ')
        m = re.match('(\<T [AIPRT]\>) (.+)', part)
        tag = m.group(1)
        if tag == '<T A>':
            citation = ' '.join(citation_stack) + ' d.a.' + canon_number
            print('Warning: unexpected <T A> tag: ' + citation, file=sys.stderr)
        if tag == '<T I>' or tag == '<T R>':
            pass
        if tag == '<T P>':
            if T_P_flag:
                citation = ' '.join(citation_stack) + ' d.p.' + canon_number
                print('Warning: multiple <T P> tags: ' + citation, file=sys.stderr)
            else:
                add_to_dictionary(' d.p.' + canon_number, m.group(2))
                T_P_flag = True
        if tag == '<T T>':
            if T_T_flag:
                citation = ' '.join(citation_stack) + ' ' + canon_number
                print('Warning: multiple <T T> tags: ' + citation, file=sys.stderr)
            else:
                add_to_dictionary(canon_number, m.group(2))
                T_T_flag = True

def add_to_dictionary(label, text):
    citation_stack.append(label)
    citation = ' '.join(citation_stack)
    table_of_contents.append(citation)
    dictionary[citation] = text
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
