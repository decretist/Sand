#!/usr/bin/python3
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 14 December 2014
#
import re
import sys
def main():
    # C.1 q.1 c.16
    canon = '''Cito turpem sequitur lepra mercedem, et pecunia male
        quesita corpus animamque commaculat.
        Vides, quia facto auctoris successio dampnatur heredis.
        Inexpiabilis est enim uenditi culpa ministerii, et uindicta
        gratiae celestis transit in posteros. Denique Moabitae
        et ceteri non intrabunt in ecclesiam Dei usque in
        terciam et quartam generationem, tamdiu uidelicet, (ut
        simplicius interpretemur), donec culpam auctorum multiplicis
        successio generationis aboleret. Sed cum illi, qui in
        Deum ydololatriae errore deliquerunt, in quartam generationem
        uideantur esse mulctati, profecto durior uidetur
        esse sententia, qua Giezi semen usque in eternum dampnatur,
        pro cupiditate habendi prophetica auctoritate presertim
        cum Dominus noster Iesus Christus per lauacri
        regenerationem dederit omnibus remissionem peccatorum.
        Cur ergo Giezi semen in eternum dampnatur, nisi ut
        uitiorum magis quam generis semen intelligas? Sicut enim
        qui filii promissionum sunt existimantur in semen
        bonum, ita etiam qui erroris sunt existimantur in
        semen malum. Nam et Iudei ex patre diabolo sunt,
        non utique carnis successione, sed criminis. Ergo omnes
        cupidi, omnes auari Giezi lepram cum diuitiis suis possident,
        et male quesita mercede non tam patrimonii facultatem,
        quam thesaurum criminum congregarunt eterno supplicio et
        breui fructu.'''
    canon = re.sub('\s+', ' ', canon) # change newlines into spaces
    pattern = '(Cito turpem sequitur.*?transit in posteros\.)'
    added = re.sub(pattern, '', canon) # text added in second recension
    added = re.sub('^\s+', '', added) # remove leading whitespace characters
    result = re.search(pattern, canon)
    if result:
        if len(result.groups()) == 1:
            canon = fixString(result.group(1))
        elif len(result.groups()) == 2:
            canon = fixString(result.group(1)) + ' ' + fixString(result.group(2))
        else:
            pass
        print(canon + '\n\n' + added)
    else:
        print('No match: ' + '\n' + pattern + '\n' + canon, file=sys.stderr)

def fixString(string):
    if string[0].islower():
        string = string[0].upper() + string[1:]
    if string[-1] == ',' or string[-1] == ';':
        string = string[0:-1] + '.'
    if string[-1].isalpha():
        string = string + '.'
    return string

if __name__ == '__main__':
    main()
