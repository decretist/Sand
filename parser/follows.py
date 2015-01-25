#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 17 January 2015
#
import re
def main():
    flag = False
    lineNumber = 0
    # pattern = r'\<2 \d{1,3}\>'
    pattern = r'\<4 \d{1,2}\>'
    # pattern = r'\<T R\>'
    f = open('./bones.txt', 'r')
    for line in f:
        lineNumber += 1
        if flag:
            flag = False
            print(line.strip())
            # print(str(lineNumber) + '\t' + line.strip())
        match = re.match(pattern, line)
        if match:
            flag = True

if __name__ == '__main__':
    main()
