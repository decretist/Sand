#!/usr/local/bin/python3
import re
def main():
    # http://www.perseus.tufts.edu/hopper/stopwords
    stopwords = [ 'ab', 'ac', 'ad', 'adhic', 'aliqui', 'aliquis', 'an', 'ante',
        'apud', 'at', 'atque', 'aut', 'autem', 'cum', 'cur', 'de', 'deinde',
        'dum', 'ego', 'enim', 'ergo', 'es', 'est', 'et', 'etiam', 'etsi', 'ex',
        'fio', 'haud', 'hic', 'iam', 'idem', 'igitur', 'ille', 'in', 'infra',
        'inter', 'interim', 'ipse', 'is', 'ita', 'magis', 'modo', 'mox', 'nam',
        'ne', 'nec', 'necque', 'neque', 'nisi', 'non', 'nos', 'o', 'ob', 'per',
        'possum', 'post', 'pro', 'quae', 'quam', 'quare', 'qui', 'quia',
        'quicumque', 'quidem', 'quilibet', 'quis', 'quisnam', 'quisquam',
        'quisque', 'quisquis', 'quo', 'quoniam', 'sed', 'si', 'sic', 'sive',
        'sub', 'sui', 'sum', 'super', 'suus', 'tam', 'tamen', 'trans', 'tu',
        'tum', 'ubi', 'uel', 'uero', 'unus', 'ut']
    patterns =[]
    for stopword in stopwords:
        patterns.append(re.compile('r\'\\b' + stopword + '\\b\''))
#    for pattern in patterns:
#        print(pattern.pattern)
    f = open('./gratian.txt', 'r')
    for line in f:
        for pattern in patterns:
            line = re.sub(pattern, '', line)
        print(line.rstrip())

if __name__ == '__main__':
    main()
