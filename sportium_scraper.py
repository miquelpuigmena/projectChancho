import unicodecsv as csv
from bs4 import BeautifulSoup
from utils import writeCSVdocresults, saveHTML, getStringSportiumPretty

htmls_sportium="htmls/sportium/"
casa="Sportium"
##########################################################
## Sportium is structured in fragments where is posible ##
## That some of them have games inside
def getPossibleFragmentGames(bsObj):
	try:
		fragments = bsObj.find("div", {"class":"cms-contents"}).div.find("div", {"id":"main-contents"}).div.div.find("div", {"id":"main-area"}).findAll("div", {"class":"fragment"})
		return fragments
	except:
		return []

##########################################################
## Check if given fragment is right to have matches
def isFragmentaGamesFragment(fragment):
	if (fragment.h4 != None and fragment.div != None):
		if(fragment.find("table", {"class","coupon"}) != None ):
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
				for tbody in currentFrag.find("div", {"class":"expander-content"}).find("div", {"class":None}).table.findAll("tbody"):
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
		alltr = tbody.findAll("tr") ## Should be 2 tr's
		for tr in alltr:
			try:
				equips.append(getStringSportiumPretty(tr.find("td", {"class":"event-name"}).div.div.a.text))
				cuotes.append(tr.findAll("td", {"class":"mkt-sort"})[-1].find("button", {"class":"price"}).find("span", {"class":"price dec"}).text)
			except:
				pass
		writeCSVdocresults(esport, casa, equips, cuotes)
	
##########################################################
## Getting in equip and cuota data parsed of each game  ##
## with 3 results
def getData3Results(esport, casa, path):
	for tbody in getMatchesSportium(path):
		for tr in tbody.findAll("tr", {"class":"mkt"}):
			equips=[]
			cuotes=[]
			for seln in tr.findAll("td", {"class":"seln"}):
				try:
					if(seln!=tr.findAll("td", {"class":"seln"})[1]):
						equips.append(getStringSportiumPretty(seln.find("button", {"class":"price"}).find("span", {"class":"seln-label"}).text))
					cuotes.append(seln.find("button", {"class":"price"}).find("span", {"class":"price dec"}).text)
				except:
					pass
			writeCSVdocresults(esport, casa, equips, cuotes)

def getHTMLs():
	saveHTML("http://109.202.116.81/es/t/40073/NBA",htmls_sportium+"NBA.txt")
	saveHTML("http://109.202.116.81/es/Top_Basket",htmls_sportium+"EUROLIGA.txt")
	saveHTML("http://109.202.116.81/es/t/35983/NHL",htmls_sportium+"NHL.txt")
	saveHTML("http://109.202.116.81/es/t/45211/La-Liga",htmls_sportium+"LALIGA.txt")
	saveHTML("http://109.202.116.81/es/t/45225/Champions-League",htmls_sportium+"CHAMPIONS.txt")
	saveHTML("http://109.202.116.81/es/t/40527/Premier-League",htmls_sportium+"PREMIER.txt")
	
######
def runSportium():
	getHTMLs()
	getData2Results("Nba",casa,htmls_sportium+"NBA.txt")
	getData2Results("Euroliga",casa,htmls_sportium+"EUROLIGA.txt")
	getData2Results("Nhl",casa,htmls_sportium+"NHL.txt")
	getData3Results("Laliga",casa, htmls_sportium+"LALIGA.txt")
	getData3Results("Champions",casa, htmls_sportium+"CHAMPIONS.txt")
	getData3Results("Premier",casa, htmls_sportium+"PREMIER.txt")



