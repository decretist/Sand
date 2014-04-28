#!/usr/local/bin/python3
# Major divisions: <1 C>, <1 D>, <1 DC>, <1 DP>
import re
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    matches = re.findall(r'\<1 [CD][CP]?\>', file)
    # Should be 149, is 149.
    print('149: ' + str(len(matches)))
    # for match in matches:
    #     print(match)

if __name__ == '__main__':
    main()
