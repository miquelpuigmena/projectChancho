import unicodecsv as csv
import json
from utils import writeCSVdocresults, saveHTML
casa="Codere"
linkConstructor="https://m.apuestas.codere.es/csbgonline/home/GetEvents?parentid="
NHL="139434016"
NBA="996842985"
EUROLIGA="103873721"
LALIGA="103852954"
PREMIER="103846129"
CHAMPIONS="103849007"
htmls_codere="htmls/codere/"
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

def getHTMLs():
	saveHTML(linkConstructor+NBA,htmls_codere+"NBA.txt")
	saveHTML(linkConstructor+EUROLIGA,htmls_codere+"EUROLIGA.txt")
	saveHTML(linkConstructor+NHL,htmls_codere+"NHL.txt")
	saveHTML(linkConstructor+LALIGA,htmls_codere+"LALIGA.txt")
	saveHTML(linkConstructor+CHAMPIONS,htmls_codere+"CHAMPIONS.txt")
	saveHTML(linkConstructor+PREMIER,htmls_codere+"PREMIER.txt")
def runCodere():
	getHTMLs()
	getDataResults("Nba", casa, json.load(open(htmls_codere+"NBA.txt")))
	getDataResults("Euroliga", casa, json.load(open(htmls_codere+"EUROLIGA.txt")))
	getDataResults("Nhl", casa, json.load(open(htmls_codere+"NHL.txt")))
	getDataResults("Laliga", casa, json.load(open(htmls_codere+"LALIGA.txt")))
	getDataResults("Champions", casa, json.load(open(htmls_codere+"CHAMPIONS.txt")))
	getDataResults("Premier", casa, json.load(open(htmls_codere+"PREMIER.txt")))

