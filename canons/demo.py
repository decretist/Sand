#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 14 January 2015
#
from __future__ import print_function
import re
import sys
def main():
    # D.5 c.4
    canon = '''Ad eius uero concubitum uir suus accedere non debet, quousque
	qui gignitur ablactetur. Praua autem in coniugatorum moribus
	consuetudo surrexit, ut mulieres filios quos gignunt, nutrire
	contemnant, eosque aliis mulieribus ad nutriendum tradant;
	quod uidelicet ex sola causa incontinentiae uidetur inuentum,
	quia dum se continere nolunt, despiciunt lactare quos
	gignunt. Si autem filios suos ex praua consuetudine aliis
	ad nutriendum tradunt, nisi purgationis tempus transierit,
	uiris suis non debent admisceri: quippe et sine partus causa
	cum in menstruis consuetis detinentur, uiris suis misceri
	prohibentur, ita ut morte lex sacra feriat, si quis uir ad
	menstruam mulierem accedat. Que tamen mulier, dum consuetudinem
	menstruam patitur, prohiberi ecclesiam intrare non ualet,
	quia ei naturae superfluitas in culpam non debet reputari,
	et per hoc, quod inuita patitur, iniustum est, ut ecclesiae
	priuetur ingressu. Nouimus namque, quod mulier, que fluxum
	patiebatur, sanguinis post tergum Domini humiliter ueniens
	uestimenti eius fimbriam tetigit, atque ab ea statim
	infirmitas sua recessit. Si ergo in fluxu sanguinis posita
	laudabiliter potuit Domini uestimentum tangere, cur, que
	menstruam patitur sanguinis, ei non liceat ecclesiam intrare?
	Si enim ea bene presumsit, que uestimentum Domini in languore
	posita tetigit, quod uni personae infirmanti conceditur,
	cur non concedatur cunctis mulieribus, que naturae suae
	uitio infirmantur? Sanctae autem communionis misterium in
	eisdem diebus percipere non debet prohiberi. Si autem ex
	ueneratione magna percipere non presumit, laudanda est; sed
	si perceperit, non est iudicanda. Bonarum quippe mentium
	est, etiam ibi culpas suas agnoscere, ubi culpa non est;
	quia sepe sine culpa agitur, quod uenit ex culpa. Unde etiam
	cum esurimus, sine culpa comedimus, quibus ex culpa primi
	hominis factum est, ut esuriamus.'''
    canon = re.sub('\s+', ' ', canon) # change newlines into spaces
    # pattern = '(Ad eius uero.*?qui gignitur ablactetur\.).*?(Si autem filios.*?est, ut esuriamus\.)'
    pattern = '(Ad eius uero.*?qui gignitur ablactetur\.)(.*?)(Si autem filios.*?est, ut esuriamus\.)'
    result = re.sub(pattern, '\\3', canon) # text added in second recension
    print(len(result))
    print(result)

if __name__ == '__main__':
    main()
