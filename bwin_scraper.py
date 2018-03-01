from utils import saveHTML, writeCSVdocresults, cross_local_to_visitant
from bs4 import BeautifulSoup
import constants as C


def getHTMLs():
	saveHTML(C.bwin_link_nba_tag,C.html_bwin_path_tag+"NBA.txt")
	saveHTML(C.bwin_link_laliga_tag,C.html_bwin_path_tag+"LALIGA.txt")
	saveHTML(C.bwin_link_champions_tag,C.html_bwin_path_tag+"CHAMPIONS.txt")
	saveHTML(C.bwin_link_premier_tag,C.html_bwin_path_tag+"PREMIER.txt")
	saveHTML(C.bwin_link_uefa_tag,C.html_bwin_path_tag+"UEFA.txt")
	saveHTML(C.bwin_link_bundesliga_tag,C.html_bwin_path_tag+"BUNDESLIGA.txt")
	saveHTML(C.bwin_link_seriea_tag,C.html_bwin_path_tag+"SERIEA.txt")
	saveHTML(C.bwin_link_ligue1_tag,C.html_bwin_path_tag+"LIGUE1.txt")


def priv_getData3Results(esport, casa, path):
	file = open (path, 'r')
	bsObj = BeautifulSoup(file, "lxml")
	
	group_of_matches = bsObj.find(C.div_tag, {C.class_tag:"container"}).find(C.div_tag, {C.id_tag:"plugin-wrapper"}).find(C.div_tag, {C.id_tag:"main-wrap"}).find(C.div_tag, {C.id_tag:"main"}).find(C.div_tag, {C.class_tag:"center"}).find(C.div_tag, {C.class_tag:"bet-offer"}).find(C.div_tag, {C.id_tag:"markets-container"}).find(C.div_tag, {C.class_tag:"marketboard"}).find(C.div_tag, {C.class_tag:"ui-widget-content"}).find(C.div_tag, {C.class_tag,"ui-widget-content-body"}).find(C.div_tag, {C.class_tag:"marketboard-event-group"}).find(C.div_tag, {C.class_tag:"marketboard-event-group__item-container"}).find(C.div_tag, {C.class_tag:"marketboard-event-group__item--sub-group"}).find(C.div_tag, {C.class_tag:"marketboard-event-group__item-container"}).findAll(C.div_tag, {C.class_tag:"marketboard-event-group__item--sub-group"})
	for group in group_of_matches:
		matches = group.find(C.div_tag, {C.class_tag:"marketboard-event-group__item-container"}).findAll(C.div_tag, {C.class_tag:"marketboard-event-group__item--event"})
		for match in matches:
			equips=[]
			cuotes=[]
			buttons = match.find(C.div_tag, {C.class_tag:"marketboard-event-without-header"}).div.find(C.div_tag, {C.class_tag:"marketboard-event-without-header__markets-container"}).table.tr.findAll("td", {C.class_tag:"mb-option-button"})
			for button in buttons:
				equip = button.find("button", {C.class_tag,"no-uniform"}).find(C.div_tag, {C.class_tag:"mb-option-button__option-name"}).text
				if len(equip)>2: #asseguro que el nom del empat 'X' no entri o derivats de X
					equips.append(equip)
				cuotes.append(button.find("button", {C.class_tag,"no-uniform"}).find(C.div_tag, {C.class_tag:"mb-option-button__option-odds"}).text)
			writeCSVdocresults(esport, casa, equips, cuotes)

def priv_getData2Results(esport, casa, path):
	file = open (path, 'r')
	bsObj = BeautifulSoup(file, "lxml")
	
	matches = bsObj.find(C.div_tag, {C.class_tag:"container"}).find(C.div_tag, {C.id_tag:"plugin-wrapper"}).find(C.div_tag, {C.id_tag:"main-wrap"}).find(C.div_tag, {C.id_tag:"main"}).find(C.div_tag, {C.class_tag:"center"}).find(C.div_tag, {C.class_tag:"bet-offer"}).find(C.div_tag, {C.id_tag:"markets-container"}).find(C.div_tag, {C.class_tag:"marketboard"}).find(C.div_tag, {C.class_tag:"ui-widget-content"}).find(C.div_tag, {C.class_tag,"ui-widget-content-body"}).find(C.div_tag, {C.class_tag:"marketboard-event-group"}).find(C.div_tag, {C.class_tag:"marketboard-event-group__item-container"}).find(C.div_tag, {C.class_tag:"marketboard-event-group__item--sub-group"}).find(C.div_tag, {C.class_tag:"marketboard-event-group__item-container"}).findAll(C.div_tag, {C.class_tag:"marketboard-event-group__item--event"})	
		
	for match in matches:
		buttons = match.find(C.div_tag, {C.class_tag:"marketboard-event-with-header"}).find(C.div_tag, {C.class_tag:"marketboard-event-with-header__markets-container"}).table.tr.findAll("td", {C.class_tag:"mb-option-button"})
		equips = []
		cuotes = []
		for button in buttons:
			equips.append(button.find("button", {C.class_tag,"no-uniform"}).find(C.div_tag, {C.class_tag:"mb-option-button__option-name"}).text)
			cuotes.append(button.find("button", {C.class_tag,"no-uniform"}).find(C.div_tag, {C.class_tag:"mb-option-button__option-odds"}).text)
		writeCSVdocresults(esport, casa, equips, cuotes)

def runBwin():
	getHTMLs()
	#priv_getData3Results(C.laliga_tag,C.bwin_tag,C.html_bwin_path_tag+"LALIGA.txt")
	priv_getData3Results(C.champions_tag,C.bwin_tag,C.html_bwin_path_tag+"CHAMPIONS.txt")
	priv_getData3Results(C.uefa_tag,C.bwin_tag,C.html_bwin_path_tag+"UEFA.txt")
	priv_getData3Results(C.premier_tag,C.bwin_tag,C.html_bwin_path_tag+"PREMIER.txt")
	priv_getData3Results(C.bundesliga_tag,C.bwin_tag,C.html_bwin_path_tag+"BUNDESLIGA.txt")
	priv_getData3Results(C.ligue1_tag,C.bwin_tag,C.html_bwin_path_tag+"LIGUE1.txt")
	priv_getData3Results(C.serie_a_tag,C.bwin_tag,C.html_bwin_path_tag+"SERIEA.txt")
	priv_getData2Results(C.nba_tag,C.bwin_tag,C.html_bwin_path_tag+"NBA.txt")
	
