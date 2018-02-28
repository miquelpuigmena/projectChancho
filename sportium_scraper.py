import unicodecsv as csv
from bs4 import BeautifulSoup
import constants as C
from utils import writeCSVdocresults, saveHTML, getStringSportiumPretty, cross_local_to_visitant

##########################################################
## Sportium is structured in fragments where is posible ##
## That some of them have games inside
def getPossibleFragmentGames(bsObj):
	try:
		fragments = bsObj.find(C.div_tag, {C.class_tag:"cms-contents"}).div.find(C.div_tag, {C.id_tag:"main-contents"}).div.div.find(C.div_tag, {C.id_tag:"main-area"}).findAll(C.div_tag, {C.class_tag:"fragment"})
		return fragments
	except:
		return []

##########################################################
## Check if given fragment is right to have matches
def isFragmentaGamesFragment(fragment):
	if (fragment.h4 != None and fragment.div != None):
		if(fragment.find(C.table_tag, {C.class_tag,"coupon"}) != None ):
			return True
	return False

##########################################################
## Append to tbodys lines that can contain matches with ##
## 2 or 3 results
def getMatchesSportium(path):
	file = open(path,"r")
	bsObj = BeautifulSoup(file, "lxml")
	tbodys = []
	for currentFrag in getPossibleFragmentGames(bsObj):
		try:
			if isFragmentaGamesFragment(currentFrag):
				for tbody in currentFrag.find(C.div_tag, {C.class_tag:"expander-content"}).find(C.div_tag, {C.class_tag:None}).table.findAll("tbody"):
					tbodys.append(tbody)
		except:
			pass
	return tbodys

##########################################################
## Getting in equip and cuota data parsed of each game  ##
## with 2 results
def getData2Results(esport, casa, path):
	for tbody in getMatchesSportium(path):
		equips=[]
		cuotes=[]
		alltr = tbody.findAll(C.tr_tag) ## Should be 2 tr's
		try:
			for tr in alltr:
				equips.append(getStringSportiumPretty(tr.find(C.td_tag, {C.class_tag:"event-name"}).div.div.a.text))
				cuotes.append(tr.findAll(C.td_tag, {C.class_tag:"mkt-sort"})[-1].find("button", {C.class_tag:"price"}).find(C.span_tag, {C.class_tag:"price dec"}).text)

			if esport == C.nba_tag:
				equips, cuotes = cross_local_to_visitant(equips, cuotes)
			writeCSVdocresults(esport, casa, equips, cuotes)
		except:
			pass
##########################################################
## Getting in equip and cuota data parsed of each game  ##
## with 3 results
def getData3Results(esport, casa, path):
	for tbody in getMatchesSportium(path):
		for tr in tbody.findAll(C.tr_tag, {C.class_tag:"mkt"}):
			try:
				equips=[]
				cuotes=[]
				for seln in tr.findAll(C.td_tag, {C.class_tag:"seln"}):
						if(seln!=tr.findAll(C.td_tag, {C.class_tag:"seln"})[1]):
							equips.append(getStringSportiumPretty(seln.find("button", {C.class_tag:"price"}).find(C.span_tag, {C.class_tag:"seln-label"}).text))
						cuotes.append(seln.find("button", {C.class_tag:"price"}).find(C.span_tag, {C.class_tag:"price dec"}).text)
				writeCSVdocresults(esport, casa, equips, cuotes)
			except:
				pass


def getHTMLs():
	saveHTML("http://109.202.116.81/es/t/40073/NBA",htmls_sportium+"NBA.txt")
	saveHTML("http://109.202.116.81/es/Top_Basket",htmls_sportium+"EUROLIGA.txt")
	saveHTML("http://109.202.116.81/es/t/35983/NHL",htmls_sportium+"NHL.txt")
	saveHTML("http://109.202.116.81/es/t/45211/La-Liga",htmls_sportium+"LALIGA.txt")
	saveHTML("http://109.202.116.81/es/t/45225/Champions-League",htmls_sportium+"CHAMPIONS.txt")
	saveHTML("http://109.202.116.81/es/t/40527/Premier-League",htmls_sportium+"PREMIER.txt")
	saveHTML("http://109.202.116.81/es/t/44571/Serie-A",htmls_sportium+"SERIEA.txt")
	saveHTML("http://109.202.116.81/es/t/45915/Bundesliga",htmls_sportium+"BUNDESLIGA.txt")
	saveHTML("http://109.202.116.81/es/t/46074/Ligue-1",htmls_sportium+"LIGUE1.txt")
	saveHTML("http://109.202.116.81/es/t/45223/Europa-League",htmls_sportium+"UEFA.txt")


htmls_sportium=C.html_sportium_path_tag
######
def runSportium():
	getHTMLs()
	getData2Results(C.nba_tag,C.sportium_tag,htmls_sportium+"NBA.txt")
	getData2Results(C.euroliga_tag,C.sportium_tag,htmls_sportium+"EUROLIGA.txt")
	getData2Results(C.nhl_tag,C.sportium_tag,htmls_sportium+"NHL.txt")
	getData3Results(C.laliga_tag,C.sportium_tag, htmls_sportium+"LALIGA.txt")
	getData3Results(C.champions_tag,C.sportium_tag, htmls_sportium+"CHAMPIONS.txt")
	getData3Results(C.premier_tag,C.sportium_tag, htmls_sportium+"PREMIER.txt")
	getData3Results(C.serie_a_tag,C.sportium_tag, htmls_sportium+"SERIEA.txt")
	getData3Results(C.bundesliga_tag,C.sportium_tag, htmls_sportium+"BUNDESLIGA.txt")
	getData3Results(C.ligue1_tag,C.sportium_tag, htmls_sportium+"LIGUE1.txt")
	getData3Results(C.uefa_tag,C.sportium_tag, htmls_sportium+"UEFA.txt")
