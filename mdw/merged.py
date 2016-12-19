#!/usr/local/bin/python3
#
# Paul Evans (10evans@cua.edu)
# 18 December 2016
#
from cltk.corpus.utils.importer import CorpusImporter
from cltk.stem.lemma import LemmaReplacer
import re
import string

def main():
    input = open('./Gratian1.txt', 'r').read()
    input = re.sub('['+string.punctuation+']', '', input)
    input = input.lower()
    lemmatizer = LemmaReplacer('latin')
    lemmata = lemmatizer.lemmatize(input)
    dictionary_1r = {}
    for lemma in lemmata:
        if lemma in dictionary_1r:
            dictionary_1r[lemma] += 1
        else:
            dictionary_1r[lemma] = 1
    # lemmata = dictionary_1r.keys()
    # for lemma in lemmata:
    #     print("%2d\t%s" % (dictionary_1r[lemma], lemma))
    input = open('./Gratian2.txt', 'r').read()
    input = re.sub('['+string.punctuation+']', '', input)
    input = input.lower()
    lemmata = lemmatizer.lemmatize(input)
    dictionary_2r = {}
    for lemma in lemmata:
        if lemma in dictionary_2r:
            dictionary_2r[lemma] += 1
        else:
            dictionary_2r[lemma] = 1
    lemmata = dictionary_2r.keys()
    for lemma in lemmata:
        if lemma not in dictionary_1r:
            print("%2d\t%s" % (dictionary_2r[lemma], lemma))

if __name__ == '__main__':
    main()

