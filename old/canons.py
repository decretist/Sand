#!/usr/local/bin/python3
import re
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    matches = re.findall(r'\<4 \d{1,3}\>', file)
    # 1582 edition: 3945.
    # Manuscripts: 3458.
    # Reuter's file: 3848.
    print('3848: ' + str(len(matches)))
    # for match in matches:
    #     print(match)

if __name__ == '__main__':
    main()
