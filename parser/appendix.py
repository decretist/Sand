#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 8 February 2015
#
from __future__ import print_function
import re
import sys
import xform
def main():
    dictionary_1r = {}
    dictionary_2r = {}
    (toc_Fr, dictionary_Fr) = xform.xform()

    keysandpatterns = [
        {'key': 'D.5 c.4', 'pattern': '(Ad eius uero.*?qui gignitur ablactetur\.)(.*?)(Si autem filios.*?est, ut esuriamus\.)'},
        {'key': 'D.9 c.1', 'pattern': '(Quicumque legibus imperatorum.*?acquirit grande premium\.)'},
        {'key': 'D.10 c.1', 'pattern': '(Lege imperatorum non.*?iura ecclesiastica dissolui\.)(.*?)(Non quod imperatorum.*?inferre preiudicium asseramus\.)'},
        {'key': 'D.17 c.1', 'pattern': '(Sinodum episcoporum absque.*?potestis regulariter facere\.)'},
        {'key': 'D.19 c.1', 'pattern': '(Si Romanorum Pontificum.*?sibi ueniam denegari\.)(.*?)(Dicendo uero: "omnia.*?Gelasium, mandasse probauimus\.)'},
        {'key': 'D.25 d.p.c.1', 'pattern': '(Ex hac epistola liquet, quid cuiusque offitii sit\.)'},
        {'key': 'D.25 d.p.c.3', 'pattern': '(Nunc autem per.*?mentem eius remordeat\.)'},
        {'key': 'D.26 d.p.c.4', 'pattern': '(Iohannes etiam Baptista.*?alteram habuisse probantur\.)'},
        {'key': 'D.30 d.a.c.1', 'pattern': '(Illud autem, quod.*?que coniugium detestabatur,)'},
        {'key': 'D.31 d.p.c.11', 'pattern': '(Ut igitur ex.*?reddere non ualent. Sed obicitur illud Tripartitae ystoriae:)'},
        {'key': 'D.32 c.6', 'pattern': '(Preter hoc autem.*?ecclesiae communione separentur\.)'},
        {'key': 'D.38 c.4', 'pattern': '(Nulli sacerdotum liceat.*?Patrum regulis obuiare\.)'},
        {'key': 'D.42 d.p.c.1', 'pattern': '(Hinc etiam Iohannes.*?de ecclesia eiciebat\.)'},
        {'key': 'D.45 d.p.c.17', 'pattern': '(Hinc etiam alibi.*?uero patrem exhibeat.")'},
        {'key': 'D.47 d.p.c.8', 'pattern': '(Necesse est etiam.*?sollicitam diligentiam exhibebit\?)'},
        {'key': 'D.48 c.2', 'pattern': '(Sicut neophitus dicebatur,.*?abrupta querit ascensum\.)'},
        {'key': 'D.50 c.52', 'pattern': '(Hii, qui altario.*?offitia ulterius promoueri\.)'},
        {'key': 'D.54 d.p.c.23', 'pattern': '(Ecce, quomodo serui.*?quomodo non admittantur\.)'},
        {'key': 'D.55 c.13', 'pattern': '(illi, cui erutus.*?sui perderet facultatem\.)'},
        {'key': 'D.56 c.1', 'pattern': '(Presbiterorum filios a sacris ministeriis remouemus,)'},
        {'key': 'D.61 c.3', 'pattern': '(Non negamus in.*?prestare quam sumere\.)'},
        {'key': 'D.61 c.5', 'pattern': '(Patrum beatorum uenerabiles.*?loci premium debetur\.)'},
        {'key': 'D.61 c.16', 'pattern': '(Obitum Victoris Panormitanae.*?credimus\) poterit inueniri,)'},
        {'key': 'D.62 c.1', 'pattern': '(Nulla ratio sinit,.*?a plebibus expetiti,)'},
        {'key': 'D.62 c.2', 'pattern': '(Docendus est populus, non sequendus,)'},
        {'key': 'D.63 d.p.c.28', 'pattern': '(Verum, quia inperatores.*?anathematis uinculo innodaretur,)(.*?)(Postremo presentibus legatis.*?ecclesiae Dei conferentes\.)'},
        {'key': 'D.63 d.p.c.34', 'pattern': '(Ex his constitutionibus.*?habita constitutum est\.)'},
        {'key': 'D.67 c.2', 'pattern': '(Episcopus sacerdotibus ac ministris solus honorem dare potest,)'},
        {'key': 'D.68 d.p.c.2', 'pattern': '(Quod ergo consecratus.*?ad cautelam salutis\.)'},
        {'key': 'D.68 c.4', 'pattern': '(Quamuis corepiscopis et.*?cuilibet epistolas mittere\.)(.*?)(Quoniam, quamquam consecrationem.*?apicem non habent\.)'},
        {'key': 'D.74 c.2', 'pattern': '(sicut iustum est,.*?ministerio deiciatur iniuste\.)'},
        {'key': 'D.89 c.5', 'pattern': '(cauendum est a.*?amministrent, quam accusent\.)'},
        {'key': 'D.93 c.13', 'pattern': '(Diaconos propriam constituimus.*?facere plerumque conceditur\.)'},
        {'key': 'D.93 c.14', 'pattern': '(in sua diaconi.*?ministerio cessare debebit\.)'},
        {'key': 'D.93 c.19', 'pattern': '(Diaconus sedeat iubente.*?presbiterorum interrogatus loquatur\.)'},
        {'key': 'C.1 q.1 c.16', 'pattern': '(Cito turpem sequitur.*?transit in posteros\.)'},
        {'key': 'C.1 q.1 c.27', 'pattern': '(Non est putanda.*?offeruntur ex scelere\.)(.*?)(Nimis ergo declinandum.*?symoniacae hereseos perpetrare\.)'},
        {'key': 'C.1 q.1 c.28', 'pattern': '(Vulnerato namque pastore.*?semetipsos placare debuerant\.)'},
        {'key': 'C.1 q.1 c.47', 'pattern': '(Sicut urgeri uideor,.*?operibus mortua est\.)'},
        {'key': 'C.1 q.1 d.p.c.51', 'pattern': '(Sed notandum est.*?Non sanat baptismus perfidorum, etc.")'},
        {'key': 'C.1 q.1 c.97', 'pattern': '(Quod quidam dicunt.*?non posse iudicatur\?)'},
        {'key': 'C.1 q.1 d.p.c.123', 'pattern': '(Quolibet ergo munere.*?falsa diiudicatur ordinatio\.)'},
        {'key': 'C.1 q.4 d.p.c.9', 'pattern': '(Cum ergo de baptizatis.*?impediat nomen erroris\.)'},
        {'key': 'C.1 q.4 d.p.c.12', 'pattern': '(Ignorabat autem Petrus.*?permittitur ignorare, aliis non\.)'},
        {'key': 'C.2 q.1 c.7', 'pattern': '(de falsis se capitulis.*?modis omnibus reuocetur\.)'},
        {'key': 'C.2 q.3 c.6', 'pattern': '(Paulum itaque diaconum.*?ei culpam ignoscimus\.)'},
        # {'key': 'C.2 q.3 d.p.c.7', 'pattern': '(Notandum quoque est.*?quod obiecerat desistat\.)'}, # @.2
        {'key': 'C.2 q.3 d.p.c.7', 'pattern': '(Notandum quoque est.*?in Libro Capitulorum:)'}, # @.2
        {'key': 'C.2 q.6 c.12', 'pattern': '(omnium appellantium apostolicam.*?reseruata esse liquet;)'},
        {'key': 'C.2 q.6 d.p.c.31', 'pattern': '(Forma uero appellationis.*?in scriptis fieri debent\.)'},
        {'key': 'C.2 q.6 d.p.c.39', 'pattern': '(Cum autem in.*?suam agere oportet\.)'},
        {'key': 'C.2 q.7 d.p.c.40', 'pattern': '(Cum ergo Petrus.*?suscipere reprehensionem subditorum\.)'},
        {'key': 'C.2 q.8 d.p.c.5', 'pattern': '(Sed Calixtus Papa.*?per epistolam accusare audeat)'},
        {'key': 'C.3 q.1 d.p.c.6', 'pattern': '(Patet ergo, quod.*?quam uocentur ad causam\.)'},
        {'key': 'C.3 q.4 c.3', 'pattern': '(Si quis uero.*?fide suspecti sunt\.)'},
        {'key': 'C.3 q.4 c.4', 'pattern': '(Consanguineorum coniunctiones nec.*?omnes eis consentientes\.)'},
        {'key': 'C.3 q.5 c.15', 'pattern': '(Athanasius a patriarcha suo.*?suae ecclesiae reddi precipitur)'},
        {'key': 'C.3 q.7 c.3', 'pattern': '("Qui sine peccato.*?illam lapidem mittat\.")(.*?)(prius ipsi purgandi.*?uicia corrigere festinant\?)'},
        {'key': 'C.3 q.7 c.4', 'pattern': '(Iudicet ille de alterius.*?nulla leuitate ducatur\.)'},
        {'key': 'C.3 q.9 c.10', 'pattern': '(Decreuimus uestram debere.*?occasione non utitur\.)'},
        {'key': 'C.3 q.11 d.p.c.3', 'pattern': '(Hoc autem intelligendum.*?auctoritatibus non prohibetur\.)'},
        # {'key': 'C.4 q.2 d.p.c.3', 'pattern': '(Sed obicitur illud.*?humanae actionis trahenda\.)'},
        {'key': 'C.4 q.4 c.1', 'pattern': '(Nullus umquam presumat.*?idoneos accusatores, defensores)'},
        {'key': 'C.5 q.3 c.1', 'pattern': '(Si egrotans fuerit.*?prout causa dictauerit\.)'}, # 2015-02-08 data engineering fix
        {'key': 'C.5 q.3 d.p.c.1', 'pattern': '(Ecce episcopus.*?se agere licet\.)'},
        {'key': 'C.5 q.6 c.3', 'pattern': '(Quia iuxta canonicas.*?famae plenitudine caruisse\.)'},
        {'key': 'C.6 q.1 d.p.c.21', 'pattern': '(Verum hoc Augustini.*?accusatione ipse repellit\.)'},
        {'key': 'C.6 q.4 c.7', 'pattern': '(Osius episcopus dixit:.*?Sinodus respondit: Placet\.)'}, # 2015-02-08 data engineering fix
        {'key': 'C.7 q.1 c.4', 'pattern': '(Pontifices, qui aliqua.*?presumptionis pullulet ambicio\.)'},
        {'key': 'C.8 q.3 c.1', 'pattern': '(Cum hic filius.*?promereri non poterit\.)'},
        {'key': 'C.9 q.2 c.3', 'pattern': '(Nullus primas, nullus metropolitanus,.*?rerum dispositio prohibetur\.)'},
        {'key': 'C.9 q.3 c.8', 'pattern': '(Conquestus est apostolatui.*?priuilegia seruentur ecclesiis,)'},
        {'key': 'C.11 q.1 c.5', 'pattern': '(Continua lege sancimus,.*?commune cum legibus\.)'},
        {'key': 'C.11 q.1 c.29', 'pattern': '(Neque enim iudicem.*?salus hominibus datur\.)'},
        {'key': 'C.11 q.1 d.p.c.34', 'pattern': '(Non ait propter.*?quam criminalem intelligens\.)'},
        {'key': 'C.11 q.1 c.36', 'pattern': '(Omnes itaque causae.*?episcoporum sententia deciderit\.)'},
        {'key': 'C.11 q.1 c.38', 'pattern': '(De persona presbiteri.*?executioni perfecte contradi\.")'},
        {'key': 'C.11 q.1 c.41', 'pattern': '(Sacerdotibus autem non.*?nos iudicemus Deos\.")'},
        {'key': 'C.11 q.1 c.45', 'pattern': '(Si quis cum.*?litis contestatione numerandum\.)(.*?)(Non autem aliter.*?huiusmodi causis habentibus\.)'},
        {'key': 'C.11 q.3 d.p.c.40', 'pattern': '(Premissis auctoritatibus, quibus.*?in se exceperunt\.)'},
        {'key': 'C.11 q.3 c.66', 'pattern': '(Qui recte iudicat,.*?acceptione pecuniae uendit\.)'},
        {'key': 'C.11 q.3 c.89', 'pattern': '(Iniustum iudicium et.*?acta, non ualeat\.)'},
        {'key': 'C.11 q.3 c.93', 'pattern': '(Si dominus iubet.*?quam hominibus obedire\.)'},
        {'key': 'C.12 q.1 c.1', 'pattern': '(Omnis etas ab.*?testem uitae habeant\.)'},
        {'key': 'C.12 q.1 c.9', 'pattern': '(Scimus uos non.*?illis omnia communia\.)'},
        {'key': 'C.13 q.1 d.p.c.1', 'pattern': '(In diocesi autem.*?qui secum erant)(.*?)(Quia ergo nos.*?ad diocesianum transferre\.)'},
        {'key': 'C.13 q.2 c.2', 'pattern': '(Ebron dicitur esse.*?in uno sepulcro\.")'}, # related to Beinecke MS 413 De iure sepulturae
        {'key': 'C.13 q.2 d.p.c.3', 'pattern': '(Item Ioseph, moriens.*?eo sepultus est\?)(.*?)(Exemplo igitur istorum.*?uoluntate tumulandi consistit\.)'},
        {'key': 'C.13 q.2 d.p.c.8', 'pattern': '(Hac nimirum auctoritate.*?quam prohibetur transscendere\.)'},
        {'key': 'C.14 q.1 d.p.c.1', 'pattern': '(Quia ergo generaliter.*?prohibentur stare coram iudice\.)'}, # 'stare coram iudice' occurs twice
        {'key': 'C.14 q.2 d.p.c.1', 'pattern': '(Potest etiam intelligi.*?pauperum, testimonium dicant\.)'},
        {'key': 'C.14 q.5 d.p.c.14', 'pattern': '(Sed hoc multipliciter.*?bonum possunt conuerti\.)'},
        {'key': 'C.15 q.6 c.1', 'pattern': '(Si sacerdotibus uel.*?successoribus, sustinere permittimus\.)(.*?)(Confessio ergo in.*?aut necessitatem fiunt\.)'},
        {'key': 'C.15 q.1 d.p.c.3', 'pattern': '(Ex eo autem.*?penam aut gloriam.")'},
        {'key': 'C.15 q.1 d.p.c.11', 'pattern': '(Cum itaque qui.*?Obicitur autem)'},
        {'key': 'C.15 q.1 d.p.c.12', 'pattern': '(Sunt quedam, que.*?muneris executionem inpediunt\.)'},
        {'key': 'C.16 q.1 c.12', 'pattern': '(Qui uere et.*?ipsius ciuitatis episcopo.)(.*?)(Conuenit uero ciuitatis.*?necessariam monasteriis exhibere.)'},
        {'key': 'C.16 q.1 d.p.c.40', 'pattern': '(Ostendit ergo Ieronimus.*?ipsum inperfectis connumerans)(.*?)(Ecce sufficienter monstratum.*?assecuntur potestatis executionem\.)'}, # inperfectis
        {'key': 'C.16 q.1 d.p.c.47', 'pattern': '(Quod autem dicitur.*?duos potest diuidi,)'},
        {'key': 'C.16 q.1 d.p.c.53', 'pattern': '(Sicut duo episcopatus.*?ad paucitatem redigeretur\.)'},
        {'key': 'C.16 q.1 c.60', 'pattern': '(Constitutum est a.*?iure presumant auferre,)'},
        {'key': 'C.16 q.2 c.8', 'pattern': '(Si quis episcoporum.*?cuius territorium est,)'},
        {'key': 'C.16 q.3 c.2', 'pattern': '(Illud etiam annecti.*?ita emanauit auctoritas\.)'},
        {'key': 'C.16 q.3 d.p.c.15', 'pattern': '(Potest etiam aliter.*?obici non potest\.)'},
        {'key': 'C.16 q.3 d.p.c.16', 'pattern': '(Sed sola prescriptione.*?spatio prescribi possunt\.)'},
        {'key': 'C.16 q.5 c.1', 'pattern': '(Consuetudo noua in.*?presumpserit, anathema sit\.)(.*?)(Is autem, qui.*?neglexerit, anathema sit\.)'},
        {'key': 'C.16 q.7 c.31', 'pattern': '(Filiis, uel nepotibus.*?iudici corrigenda denuncient\.)(.*?)(Ipsis tamen heredibus.*?iuris potestatem preferre,)'},
        {'key': 'C.17 q.2 d.p.c.2', 'pattern': '(Ecce iste se.*?concepit, et ore pronunciauit\.)'}, # 'et ore pronunciauit' occurs twice
        {'key': 'C.17 q.4 c.5', 'pattern': '(Omnes ecclesiae raptores.*?sacrilegos esse iudicamus;)'},
        {'key': 'C.18 q.2 c.5', 'pattern': '(Quam sit necessarium.*?aliquem honorem promoueat\.)'},
        {'key': 'C.19 q.2 c.2', 'pattern': '(Duae sunt, inquit,.*?lex est canonum,)(.*?)(Lex uero priuata.*?in corde scribitur,)'},
        {'key': 'C.19 q.3 c.6', 'pattern': '(Monasteriis omnibus fraternitas.*?modo audeant tonsorare\.)'},
        {'key': 'C.21 q.2 d.p.c.3', 'pattern': '(Sed aliud est.*?omnibus modis prohibetur\.)'},
        {'key': 'C.21 q.4 c.1', 'pattern': '(episcopos uel clericos.*?qui unguentis unguntur\.)(.*?)(Priscis enim temporibus.*?domibus regum sunt\.")'},
        {'key': 'C.22 q.1 d.p.c.16', 'pattern': '(Sic etiam cum.*?creatorem iurat mendaciter\.)'},
        {'key': 'C.22 q.2 c.4', 'pattern': '(qui dicit falsum.*?autem uoluntate mentitur\.)'},
        {'key': 'C.22 q.2 d.p.c.5', 'pattern': '(Ille ergo falsum.*?esse quod iurat\.)'},
        {'key': 'C.22 q.4 c.8', 'pattern': '(Unusquisque simplicem sermonem.*?quod amicitiae fuit\.)'},
        {'key': 'C.22 q.5 c.1', 'pattern': '(Qui conpulsus a.*?quam animam dilexit\.)'},
        {'key': 'C.23 q.3 c.7', 'pattern': '(Non in inferenda,.*?ille, qui facit\.)'},
        {'key': 'C.23 q.3 c.9', 'pattern': '(Iustum est, ut.*?seuerioribus corrigantur uindictis,)'},
        {'key': 'C.23 q.4 c.7', 'pattern': '(Quisquis autem in.*?habet socium criminis\.)'},
        {'key': 'C.23 q.4 d.p.c.26', 'pattern': '(Potest in hac.*?personae quendam excommunicauerat,)'},
        {'key': 'C.23 q.4 d.p.c.27', 'pattern': '(ostendens, quod peccata.*?potius dissimulanda sunt)'},
        {'key': 'C.23 q.4 d.p.c.30', 'pattern': '(Quod autem peccatum.*?patienter tollerasse asseritur\.)'},
        {'key': 'C.23 q.5 c.9', 'pattern': '(nequaquam contra hoc.*?homicidii crimine innectitur\.)'},
        {'key': 'C.23 q.7 c.4', 'pattern': '(Si autem consideremus.*?societate catholica utantur,)'},
        {'key': 'C.23 q.8 d.p.c.25', 'pattern': '(Hinc datur intelligi.*?Pontificis fieri debet\.)'},
        {'key': 'C.23 q.8 d.p.c.27', 'pattern': '(Reprehenduntur ergo Gallicani.*?orationibus Deo conmendent\.)'},
        {'key': 'C.24 q.1 c.26', 'pattern': '(Fides ergo.*?correptionem deuita\.")'},
        {'key': 'C.24 q.1 c.40', 'pattern': '(Si quem forte.*?unitatem seruabat,)'}, # see ch. 2
        {'key': 'C.24 q.2 c.2', 'pattern': '(Mortuos suscitasse.*?esse absoluendum\.)'},
        {'key': 'C.26 q.5 c.4', 'pattern': '(Non oportet sacris.*?suarum uincula conprobantur\.)'},
        {'key': 'C.26 q.6 c.13', 'pattern': '(Agnouimus penitenciam morientibus.*?Dei pietate desperet,)(.*?)(Quid hoc, rogo,.*?eo promittente promeruit\.)'},
        {'key': 'C.27 q.1 c.9', 'pattern': '(He uero, que.*?etc\. et infra\.)(.*?)(Nam si Apostolus.*?fidem conatae sunt\.)'},
        {'key': 'C.27 q.1 c.18', 'pattern': '(ualeat custodiri, detrudere,.*?ualeas sollicitudine minuere\.)'},
        {'key': 'C.27 q.2 c.19', 'pattern': '(Sunt qui dicunt,.*?quis audeat accusare\?)(.*?)(Si uero continentiam,.*?habet, sed mulier\.")'},
        {'key': 'C.27 q.2 c.46', 'pattern': '(Desponsatas puellas et.*?ante fuerant desponsatae,)'},
        {'key': 'C.29 q.1 d.a.c.1', 'pattern': '(Quod autem coniugium.*?potest eam dimittere)'},
        {'key': 'C.29 q.2 d.p.c.6', 'pattern': '(Cum dicitur: "sciens.*?fraude decepta est;)'},
        {'key': 'C.30 q.1 c.2', 'pattern': '(Si quis filiastrum.*?ab uxore sua,)'},
        # {'key': 'C.30 q.4 c.5', 'pattern': '(Post uxoris obitum.*?unionem spiritus pertransitur\.)'}, # 2015-02-08 Winroth appendix error?
        {'key': 'C.30 q.4 d.p.c.5', 'pattern': '(Notandum uero est.*?uiro suo cognoscitur\.)'},
        {'key': 'C.30 q.5 c.3', 'pattern': '(Nostrates, tam mares.*?uelamen celeste suscipiunt\.)'},
        {'key': 'C.31 q.1 d.p.c.7', 'pattern': '(Sed obicitur: Dauid.*?quam significatione futurorum\.)'},
        {'key': 'C.32 q.1 d.p.c.10', 'pattern': '(Si ergo, ut.*?sed adulteri appellantur\.)'},
        {'key': 'C.32 q.4 d.p.c.10', 'pattern': '(Ecce, quod nullo.*?nomine iudicantur indigni\.)'},
        {'key': 'C.32 q.5 c.4', 'pattern': '(Lucretiam, matronam nobilem.*?unus adulterium admisit.")'},
        {'key': 'C.32 q.5 c.6', 'pattern': '(De pudicitia quis.*?possit in corpore\.)(.*?)(Item Augustinus in.*?prius insita castitate\.)'},
        {'key': 'C.33 q.2 d.p.c.9', 'pattern': '(In premissis auctoritatibus.*?eis misericordia inpendatur\.)'},
        {'key': 'de Pen. D.1 d.a.c.1', 'pattern': '(Utrum sola cordis.*?promereri, iuxta illud)'}, # d.a.c.1
        {'key': 'de Pen. D.1 c.30', 'pattern': '(Item, sicut auctoritas.*?in oris confessione\.)'},
        {'key': 'de Pen. D.1 c.51', 'pattern': '(Et paulo post.*?Dei non habet\.)'},
        {'key': 'de Pen. D.1 c.81', 'pattern': '(Tres sunt autem.*?Domino utique iudicaremur\.)'},
        {'key': 'de Pen. D.1 d.p.c.87', 'pattern': '(His auctoritatibus asseritur.*?iugiter confiteri debemus\.)(.*?)(Similiter et illud.*?de penitencia ait:)'},
        {'key': 'de Pen. D.2 d.a.c.1', 'pattern': '(Alii dicunt penitenciam.*?tibi aliquid contingat.")'},
        {'key': 'de Pen. D.2 d.p.c.24', 'pattern': '(Hec itaque karitas.*?redeunt et cetera.")'},
        {'key': 'de Pen. D.3 c.6', 'pattern': '(Penitenciam agere digne.*?auaritiae estibus anhelat\?)'},
        {'key': 'de Pen. D.7 c.2', 'pattern': '("Si quis positus.*?bene hinc exit;)(.*?)(Si autem uis.*?non tu illa\.")'},
        {'key': 'C.33 q.5 c.4', 'pattern': '(Quod Deo pari.*?nullus defendisset annorum\.)'},
        {'key': 'C.35 q.2 c.10', 'pattern': '(Nec eam, quam.*?et cunctis hominibus\.)'},
        {'key': 'C.35 q.2 d.p.c.21', 'pattern': '(Hac auctoritate dum.*?ducat in uxorem.")'}, # ducat
        {'key': 'C.35 q.9 c.3', 'pattern': '(Quod quis conmisit.*?uult uitare, dampnabit\.)'},
        # {'key': '', 'pattern': '(.*?\.)'},
        # {'key': '', 'pattern': '(.*?\.)(.*?)(.*?\.)'},
    ]

    for i in range (len(keysandpatterns)):
        key = keysandpatterns[i]['key']
        pattern = keysandpatterns[i]['pattern']
        result = re.search(pattern, dictionary_Fr[key])
        if result:
            if len(result.groups()) == 1:
                dictionary_1r[key] = fixString(result.group(1))
                dictionary_2r[key] = fixString(re.sub(pattern, '', dictionary_Fr[key]))
            elif len(result.groups()) == 3:
                dictionary_1r[key] = fixString(result.group(1)) + ' ' + fixString(result.group(3))
                dictionary_2r[key] = fixString(result.group(2))
        else:
            print('no match: ' + key + '\n' + dictionary_Fr[key], file=sys.stderr)

    for i in range (len(keysandpatterns)):
        key = keysandpatterns[i]['key']
        print(key + ' (Fr)')
        print(dictionary_Fr[key])
        print(key + ' (1r)')
        print(dictionary_1r[key])
        print(key + ' (2r)')
        print(dictionary_2r[key] + '\n')

    # print(dictionary_Fr['D.32 c.6'])
    # print(dictionary_Fr['D.54 c.22'])
    # print(dictionary_Fr['C.4 q.4 c.2'])
    # print(dictionary_Fr['C.5 q.3 c.1'])
    # print(dictionary_Fr['C.13 q.2 c.8'])
    # print(dictionary_Fr['C.16 q.1 c.40'])
    # print(dictionary_Fr['C.16 q.3 c.16'])
    # print(dictionary_Fr['C.33 q.2 c.11'])

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
