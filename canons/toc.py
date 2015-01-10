#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
import re
def main():
    seite = ''
    pars = ''
    number = ''
    # distinctio = ''
    # causa = ''
    quaestio = ''
    canon = '0'
    f = open('./bones.txt', 'r')
    for line in f:
        m10 = re.match(r'\<1 C>', line) # Causa
        m11 = re.match(r'\<1 D>', line) # Distinctio
        m12 = re.match(r'\<1 DC>', line) # De Consecratione
        m13 = re.match(r'\<1 DP>', line) # De Penitentia
        m14 = re.match(r'\<2 (\d{1,3})\>', line)
        m15 = re.match(r'\<3 (\d{1,2})\>', line)
        m16 = re.match(r'\<4 (\d{1,3})\>', line)
        # m20 = re.search('\<P 0\>', line) # Palea end
        # m21 = re.match('\<P 1\>', line) # Palea start
        m22 = re.match(r'\<S (\d{1,4})\>', line) 
        m23 = re.match(r'\<T A\>', line) # Dictum ante
        # m24 = re.match(r'\<T I\>', line) # Inscriptio
        m25 = re.match(r'\<T P\>', line) # Dictum post
        m26 = re.match(r'\<T Q\>', line) # Quaestio
        # m27 = re.match(r'\<T R\>', line) # Rubrik
        m28 = re.match(r'\<T T\>', line) # Text des Kapitels
        m30 = re.search(r'\<.*?\>', line)

        if m10:
            canon = '0'
            pars = 'C.'
            pass
        elif m11:
            canon = '0'
            quaestio = ''
            pars = 'D.'
            pass
        elif m12: # De Consecratione
            canon = '0'
            quaestio = ''
            pars = 'de Cons. D.'
            pass
        elif m13: # De Penitentia
            canon = '0'
            quaestio = ''
            pars = 'de Pen. D.'
            pass
        elif m14:
            number = str(m14.group(1)) + ' '
            pass
        elif m15:
            canon = '0'
            quaestio = 'q.' + str(m15.group(1)) + ' '
            pass
        elif m16: # <4 \d{1,3}>
            canon = m16.group(1)
            # print(pars + number + quaestio + 'c.' + canon)
        elif m22:
            seite = str(m22.group(1)) + ': '
            pass
        elif m23: # <T A>
            # print(pars + number + quaestio + 'd.a.c.' + str(int(canon) + 1))
            pass
        elif m25: # <T P>
            # print(pars + number + quaestio + 'd.p.c.' + canon)
            pass
        elif m26: # <T Q>
            # print(seite + pars + number + 'd.init')
            pass
        elif m28: # <T T>
            print(pars + number + quaestio + 'c.' + canon)
            pass

if __name__ == '__main__':
    main()
