#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 5 February 2015
#
from __future__ import print_function
import re
import sys
import parse
def main():
    (packages, dictionary) = parse.parse_all()
    for package in packages:
        T_A_flag = False
        T_P_flag = False
        T_Q_flag = False
        T_R_flag = False
        for part in dictionary[package]:
            tag = part[0]
            text = part[1]
            if tag == '<T A>':
                if T_A_flag:
                    print('Warning: multiple <T A> tags: ' + package, file=sys.stderr)
                else:
                    T_A_flag = True
            if tag == '<T Q>':
                if T_Q_flag:
                    print('Warning: multiple <T Q> tags: ' + package, file=sys.stderr)
                else:
                    T_Q_flag = True
            if tag == '<T P>':
                if T_P_flag:
                    print('Warning: multiple <T P> tags: ' + package, file=sys.stderr)
                else:
                    T_P_flag = True
            if tag == '<T R>':
                if T_R_flag:
                    print('Warning: multiple <T R> tags: ' + package, file=sys.stderr)
                else:
                    T_R_flag = True

if __name__ == '__main__':
    main()
