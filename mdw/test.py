#!/usr/local/bin/python3
#
# Paul Evans (10evans@cua.edu)
# 17 December 2016
#
from cltk.corpus.utils.importer import CorpusImporter
from cltk.stem.latin.j_v import JVReplacer
from cltk.stem.lemma import LemmaReplacer

def main():
    corpus_importer = CorpusImporter('latin')
    corpora_list = corpus_importer.list_corpora
    print(corpora_list)
    corpus_importer.import_corpus('latin_models_cltk')
    sentence = 'Aeneadum genetrix, hominum divomque voluptas, alma Venus, caeli subter labentia signa quae mare navigerum, quae terras frugiferentis concelebras, per te quoniam genus omne animantum concipitur visitque exortum lumina solis.'
    sentence = sentence.lower()
    lemmatizer = LemmaReplacer('latin')
    lemmatized_sentence = lemmatizer.lemmatize(sentence)
    print(lemmatized_sentence)

if __name__ == '__main__':
    main()

