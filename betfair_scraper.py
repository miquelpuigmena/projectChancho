from utils import saveHTML, writeCSVdocresults, getStringBetfairPretty, cross_local_to_visitant
from bs4 import BeautifulSoup
import constants as C


def getHTMLs():
	saveHTML(C.betfair_link_nba_tag,C.html_betfair_path_tag+"NBA.txt")
	saveHTML(C.betfair_link_laliga_tag,C.html_betfair_path_tag+"LALIGA.txt")
	saveHTML(C.betfair_link_champions_tag,C.html_betfair_path_tag+"CHAMPIONS.txt")
	saveHTML(C.betfair_link_premier_tag,C.html_betfair_path_tag+"PREMIER.txt")
	saveHTML(C.betfair_link_uefa_tag,C.html_betfair_path_tag+"UEFA.txt")
	saveHTML(C.betfair_link_bundesliga_tag,C.html_betfair_path_tag+"BUNDESLIGA.txt")
	saveHTML(C.betfair_link_seriea_tag,C.html_betfair_path_tag+"SERIEA.txt")
	saveHTML(C.betfair_link_ligue1_tag,C.html_betfair_path_tag+"LIGUE1.txt")

def priv_getDataResults(esport, casa, path):
	file = open (path, 'r')
	bsObj = BeautifulSoup(file, "lxml")

	eventos_separated_by_days = bsObj.find("div", {"id":"zone-container"}).div.div.find("div", {"class":"grid-1 "}).div.findAll("div", {"class":"grid-1 "})[1].div.div.div.div.find("div", {"class":"updated-markets browse-all-container"}).div.find("ul", {"class":"section-list"}).findAll("li", {"class":"section"})

	for group_by_day in eventos_separated_by_days:
		matches = group_by_day.find("ul", {"class":"event-list"}).findAll("li", {"class":"com-coupon-line-new-layout"})
		for match in matches:
			equips=[]
			equips_of_match = match.find("div", {"class":"event-information"}).find("div", {"class":"avb-col avb-col-runners"}).find("div", {"class":"event-name-info"}).a.div.findAll("span")
			for equip in equips_of_match:
				equips.append(getStringBetfairPretty(equip.text))
			cuotes=[]
			cuotes_of_match = match.find("div", {"class":"event-information"}).find("div", {"class":"avb-col avb-col-markets"}).findAll("div", {"class":"details-market"})[-1].find("div", {"class":"runner-list"}).find("ul", {"class":"runner-list-selections"}).findAll("li", {"class":"selection"})
			for cuota in cuotes_of_match:
				cuotes.append(cuota.a.span.text)
			if esport == C.nba_tag or esport == C.nhl_tag:
				equips, cuotes = cross_local_to_visitant(equips, cuotes)
			writeCSVdocresults(esport, casa, equips, cuotes)

			

def runBetfair():
	getHTMLs()
	priv_getDataResults(C.nba_tag,C.betfair_tag,C.html_betfair_path_tag+"NBA.txt")
	priv_getDataResults(C.laliga_tag,C.betfair_tag, C.html_betfair_path_tag+"LALIGA.txt")
	priv_getDataResults(C.champions_tag,C.betfair_tag, C.html_betfair_path_tag+"CHAMPIONS.txt")
	priv_getDataResults(C.premier_tag,C.betfair_tag, C.html_betfair_path_tag+"PREMIER.txt")
	priv_getDataResults(C.serie_a_tag,C.betfair_tag,C.html_betfair_path_tag+"SERIEA.txt")
	priv_getDataResults(C.bundesliga_tag,C.betfair_tag, C.html_betfair_path_tag+"BUNDESLIGA.txt")
	priv_getDataResults(C.ligue1_tag,C.betfair_tag, C.html_betfair_path_tag+"LIGUE1.txt")
	priv_getDataResults(C.uefa_tag,C.betfair_tag, C.html_betfair_path_tag+"UEFA.txt")

