#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 22 January 2015
#
from __future__ import print_function
import re
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    f.close()
    scanner = re.Scanner([
        (r'<T R>', lambda scanner, token:('RUBRIC'))
    ])
    scanner.scan(file)

if __name__ == '__main__':
    main()
