#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 23 January 2015
#
from __future__ import print_function
import re
import sys
canon_number = ''
case_number = ''
distinction_number = ''
question_number = ''
table_of_contents = []
dictionary = {}
def main():
    # parse_distinctions(preprocess(open('./part1.txt', 'r').read()))
    parse_cases(preprocess(open('./part2.txt', 'r').read()))
    # print(table_of_contents)

def parse_cases(text):
    global case_number
    cases = re.findall('(?:\<1 C\>)(.*?)(?=\<1 C\>|$)', text)
    for case in cases:
        case = case.strip(' ')
        m = re.match('\<2 (\d{1,2})\><T Q> (.*?) (?=\<3 1\>)', case)
        case_number = 'C.' + m.group(1)
        #
        key = case_number + ' d.init.'
        table_of_contents.append(key)
        dictionary[key] = m.group(2)
        #
        parse_questions(case)

def parse_questions(text):
    global question_number
    questions = re.findall('(\<3 \d{1,2}\>.*?)(?=\<3 \d{1,2}\>|$)', text)
    for question in questions:
        question = question.strip(' ')
        m = re.match('\<3 (\d{1,2})\> \<T A\> (.*?) (?=\<4 1\>)', question)
        if m:
            question_number = 'q.' + m.group(1)
            key = case_number + ' ' + question_number + ' d.a.c.1'
            table_of_contents.append(key)
            dictionary[key] = m.group(2)
            parse_canons(question)
        else:
            continue

def parse_distinctions(text):
    global distinction_number
    distinctions = re.findall('(?:\<1 D\>)(.*?)(?=\<1 D\>|$)', text)
    for distinction in distinctions:
        distinction = distinction.strip(' ')
        m = re.match('\<2 (\d{1,3})\> \<T A\> (.*?) (?=\<4 1\>)', distinction)
        distinction_number = 'D.' + m.group(1)
        #
        key = distinction_number + ' d.a.c.1'
        table_of_contents.append(key)
        dictionary[key] = m.group(2)
        #
        parse_canons(distinction)

def parse_canons(text):
    global canon_number
    canons = re.findall('(\<4 \d{1,2}\>.*?)(?=\<4 \d{1,2}\>|$)', text)
    for canon in canons:
        canon = canon.strip(' ')
        m = re.match('\<4 (\d{1,2})\>', canon)
        canon_number = 'c.' + m.group(1)
        parse_parts(canon)

def parse_parts(text):
    T_P_flag = False
    T_T_flag = False
    parts = re.findall('(\<T [AIPRT]\>.*?)(?=\<T [AIPRT]\>|$)', text)
    for part in parts:
        part = part.strip(' ')
        m = re.match('(\<T [AIPRT]\>) (.+)', part)
        tag = m.group(1)
        if tag == '<T A>':
            # key = distinction_number + ' d.a.' + canon_number
            key = case_number + ' ' + question_number  + ' d.a.' + canon_number
            print('Warning: unexpected <T A> tag: ' + key, file=sys.stderr)
        if tag == '<T I>' or tag == '<T R>':
            pass
        if tag == '<T P>':
            # key = distinction_number + ' d.p.' + canon_number
            key = case_number + ' ' + question_number + ' d.p.' + canon_number
            if T_P_flag:
                print('Warning: multiple <T P> tags: ' + key, file=sys.stderr)
            else:
                table_of_contents.append(key)
                dictionary[key] = m.group(2)
                T_P_flag = True
        if tag == '<T T>':
            # key = distinction_number + ' ' + canon_number
            key = case_number + ' ' + question_number + ' ' + canon_number
            if T_T_flag:
                print('Warning: multiple <T T> tags: ' + key, file=sys.stderr)
                pass
            else:
                table_of_contents.append(key)
                dictionary[key] = m.group(2)
                T_T_flag = True

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
