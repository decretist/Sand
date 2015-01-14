#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 10 January 2015
#
from __future__ import print_function
import re
import sys
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    toc = open('./toc.txt', 'r')
    dictionary = {}
    dictionary_r1 = {}
    dictionary_r2 = {}
    # (?<=...) positive lookbehind assertion.
    canons = re.findall('(?:\<T T\>|(?<=\<T T\>))(.*?)'    # canon starts with text (<T T>) tag.
        '(?:'                   # non-capturing group.
            '\<1 [CD][CP]?\>|'  # canon ends with major division,
            '\<2 \d{1,3}\>|'    # or number of major division,
            '\<3 \d{1,2}\>|'    # or number of question,
            '\<4 \d{1,3}\>|'    # or number of canon,
            '\<P 1\>|'          # or Palea,
            # '\<T [AIPT]\>'    # or inscription or text tag.
            '\<T [APT]\>'       # or dicta or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    # print('expected 4392 canons, found ' + str(len(canons)) + ' canons', file=sys.stderr)
    for canon in canons:
        canon = re.sub('\<S \d{1,4}\>\<L 1\> \-\d{1,4}\+', '', canon) # remove page and line number tags.
        canon = re.sub('\<P 1\> \-\[PALEA\.\+', '', canon) # remove Palea tag.
        canon = re.sub('\<P 0\>', '', canon) # remove Palea tag.
        canon = re.sub('\<T I\>', '', canon) # remove inscription tag.
        canon = re.sub(re.compile('\-\[.*?\]\+', re.S), '', canon)
        canon = re.sub('\-.*?\+', '', canon)
        canon = re.sub('\s+', ' ', canon)
        canon = re.sub('^\s+', '', canon) # remove leading whitespace characters
        canon = re.sub('\s+$', '', canon) # remove trailing whitespace characters
        key = toc.readline().rstrip()
        if key in dictionary:
        # if there's already a dictionary entry with this key, merge the entries
            # print('duplicate key: ' + key, file=sys.stderr)
            canon = dictionary[key] + ' ' + canon
        dictionary[key] = canon

    keysandpatterns = [
        # {'key': 'D.5 c.4', 'pattern': '(Ad eius uero.*?qui gignitur ablactetur\.).*?(Si autem filios.*?est, ut esuriamus\.)'},
        {'key': 'D.9 c.1', 'pattern': '(Quicumque legibus imperatorum.*?acquirit grande premium\.)'},
        # {'key': 'D.10 c.1', 'pattern': '(Lege imperatorum non.*?iura ecclesiastica dissolui\.).*?(Non quod imperatorum.*?inferre preiudicium asseramus\.)'},
        {'key': 'D.17 c.1', 'pattern': '(Sinodum episcoporum absque.*?potestis regulariter facere\.)'},
        # {'key': 'D.19 c.1', 'pattern': '(Si Romanorum Pontificum.*?sibi ueniam denegari\.).*?(Dicendo uero: "omnia.*?Gelasium, mandasse probauimus\.)'},
        {'key': 'D.32 c.6', 'pattern': '(Preter hoc autem.*?ecclesiae communione separentur\.)'},
        {'key': 'D.38 c.4', 'pattern': '(Nulli sacerdotum liceat.*?Patrum regulis obuiare\.)'},
        {'key': 'D.48 c.2', 'pattern': '(Sicut neophitus dicebatur,.*?abrupta querit ascensum\.)'},
        {'key': 'D.50 c.52', 'pattern': '(Hii, qui altario.*?offitia ulterius promoueri\.)'},
        {'key': 'D.55 c.13', 'pattern': '(illi, cui erutus.*?sui perderet facultatem\.)'},
        {'key': 'D.56 c.1', 'pattern': '(Presbiterorum filios a sacris ministeriis remouemus,)'},
        {'key': 'D.61 c.3', 'pattern': '(Non negamus in.*?prestare quam sumere\.)'},
        {'key': 'D.61 c.5', 'pattern': '(Patrum beatorum uenerabiles.*?loci premium debetur\.)'},
        {'key': 'D.61 c.16', 'pattern': '(Obitum Victoris Panormitanae.*?credimus\) poterit inueniri,)'},
        {'key': 'D.62 c.1', 'pattern': '(Nulla ratio sinit,.*?a plebibus expetiti,)'},
        {'key': 'D.62 c.2', 'pattern': '(Docendus est populus, non sequendus,)'},
        {'key': 'D.67 c.2', 'pattern': '(Episcopus sacerdotibus ac ministris solus honorem dare potest,)'},
        # {'key': 'D.68 c.4', 'pattern': '(Quamuis corepiscopis et.*?cuilibet epistolas mittere\.).*?(Quoniam, quamquam consecrationem.*?apicem non habent\.)'},
        {'key': 'D.74 c.2', 'pattern': '(sicut iustum est,.*?ministerio deiciatur iniuste\.)'},
        {'key': 'D.89 c.5', 'pattern': '(cauendum est a.*?amministrent, quam accusent\.)'},
        {'key': 'D.93 c.13', 'pattern': '(Diaconos propriam constituimus.*?facere plerumque conceditur\.)'},
        {'key': 'D.93 c.14', 'pattern': '(in sua diaconi.*?ministerio cessare debebit\.)'},
        {'key': 'D.93 c.19', 'pattern': '(Diaconus sedeat iubente.*?presbiterorum interrogatus loquatur\.)'},
        # {'key': '', 'pattern': '(.*?\.)'},
        # {'key': '', 'pattern': '(.*?\.).*?(.*?\.)'},
    ]

    for i in range (len(keysandpatterns)):
        key = keysandpatterns[i]['key']
        pattern = keysandpatterns[i]['pattern']
        dictionary_r2[key] = fixString(re.sub(pattern, '', dictionary[key])) # text added in second recension
        # print(dictionary_r2[key], file=sys.stderr)

    keys = tuple(open('./toc_test.txt', 'r')) # uniq toc.txt > dedup.txt
    for key in keys:
        key = key.rstrip()
        #
        print(key + '\n' + dictionary_r2[key] + '\n')
        #
        outfilename = './tmp/auto/2r_pre/' + key + '.txt'
        f = open(outfilename, 'w')
        f.write(dictionary_r2[key] + '\n')
        f.close
        #
        # Generate files for hand-editing. Only do this once, or you'll overwrite your work!
        # outfilename = './tmp/hand/2r/' + key + '.txt'
        # f = open(outfilename, 'w')
        # f.write(dictionary[key] + '\n')
        # f.close

def fixString(string):
    string = re.sub('\s+', ' ', string) # 2r
    string = re.sub('^\s+', '', string) # 2r
    string = re.sub('\s+$', '', string) # 2r
    if string[0].islower():
        string = string[0].upper() + string[1:]
    if string[-1] == ',' or string[-1] == ';':
        string = string[0:-1] + '.'
    if string[-1].isalpha():
        string = string + '.'
    return string

if __name__ == '__main__':
    main()
