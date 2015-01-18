#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 17 January 2015
#
import re
def main():
    flag = False
    lineNumber = 0
    f = open('./bones.txt', 'r')
    for line in f:
        lineNumber += 1
        if flag:
            flag = False
            print(str(lineNumber) + " " + line[:-1]) # chop(line)
        match = re.match(r'\<T R\>', line)
        if match:
            flag = True

if __name__ == '__main__':
    main()
