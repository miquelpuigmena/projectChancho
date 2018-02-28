import constants as C
import unicodecsv as csv
import json
from utils import writeCSVdocresults, saveHTML

def getDataResults(esport, casa, jsonData):
	for game in jsonData:
		cuotes=[]
		equips=[]
		teams = game["Games"][0]["Results"]
		for team in teams:
			cuotes.append(team["Odd"])
			if (team["Name"]!="X"):
				equips.append(team["Name"])
		writeCSVdocresults(esport, casa, equips, cuotes)

linkConstructor="https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid="
NHL="139434016"
NBA="996842985"
EUROLIGA="103873721"
LALIGA="103852954"
PREMIER="103846129"
CHAMPIONS="103849007"
SERIEA="103856868"
LIGUE1="103879105"
UEFA="103881073"
BUNDESLIGA="103860942"
def getHTMLs():
	saveHTML(linkConstructor+NBA,htmls_codere+"NBA.txt")
	saveHTML(linkConstructor+EUROLIGA,htmls_codere+"EUROLIGA.txt")
	saveHTML(linkConstructor+NHL,htmls_codere+"NHL.txt")
	saveHTML(linkConstructor+LALIGA,htmls_codere+"LALIGA.txt")
	saveHTML(linkConstructor+CHAMPIONS,htmls_codere+"CHAMPIONS.txt")
	saveHTML(linkConstructor+PREMIER,htmls_codere+"PREMIER.txt")
	saveHTML(linkConstructor+SERIEA,htmls_codere+"SERIEA.txt")
	saveHTML(linkConstructor+LIGUE1,htmls_codere+"LIGUE1.txt")
	saveHTML(linkConstructor+UEFA,htmls_codere+"UEFA.txt")
	saveHTML(linkConstructor+BUNDESLIGA,htmls_codere+"BUNDESLIGA.txt")

htmls_codere=C.html_codere_path_tag
casa=C.codere_tag
def runCodere():
	getHTMLs()
	getDataResults(C.nba_tag, casa, json.load(open(htmls_codere+"NBA.txt")))
	getDataResults(C.euroliga_tag, casa, json.load(open(htmls_codere+"EUROLIGA.txt")))
	getDataResults(C.nhl_tag, casa, json.load(open(htmls_codere+"NHL.txt")))
	getDataResults(C.laliga_tag, casa, json.load(open(htmls_codere+"LALIGA.txt")))
	getDataResults(C.champions_tag, casa, json.load(open(htmls_codere+"CHAMPIONS.txt")))
	getDataResults(C.premier_tag, casa, json.load(open(htmls_codere+"PREMIER.txt")))
	getDataResults(C.serie_a_tag, casa, json.load(open(htmls_codere+"SERIEA.txt")))
	getDataResults(C.bundesliga_tag, casa, json.load(open(htmls_codere+"BUNDESLIGA.txt")))
	getDataResults(C.ligue1_tag, casa, json.load(open(htmls_codere+"LIGUE1.txt")))
	getDataResults(C.uefa_tag, casa, json.load(open(htmls_codere+"UEFA.txt")))
