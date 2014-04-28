#!/usr/local/bin/python3
# '-' turns off visibility to the concordancer
# '+' turns on visibility to the concordancer
import re
def main():
    f = open('./edF.txt', 'r')
    number = 0 # line number
    for line in f:
        number += 1
        # match = re.match(r'\+.*\-', line)
        match = re.match(r'\-.*\+', line)
        if match:
            print(str(number) + ': ' + match.group())

if __name__ == '__main__':
    main()
