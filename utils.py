import unicodecsv as csv
import requests
import constants as C


path = C.dataresultpath_tag
##########################################################
## Writing in csv
def writeCSVdocresults(esport, casa, equip, cuota):
	if(len(equip)==2):
		if(len(cuota)==2):
			f = open(path, 'a')
			writer = csv.writer(f)
			writer.writerow((esport, casa, equip[0], equip[1], cuota[0], C.none_tag,cuota[1]))
			f.close()
		elif(len(cuota)==3):
			f = open(path, 'a')
			writer = csv.writer(f)
			writer.writerow((esport, casa, equip[0], equip[1], cuota[0], cuota[1], cuota[2]))
			f.close()

##########################################################
## Prettify String from Sportium
def getStringSportiumPretty(string):
	return string.replace(C.enterchar_tag, C.emptychar_tag)

##########################################################
## Prettify String from Betfair
def getStringBetfairPretty(string):
	return string.replace(C.enterchar_tag, C.emptychar_tag).replace(C.arroba_espace_tag, C.emptychar_tag)

##########################################################
## Empty csv 2 results doc
def emptydocresults():
	f = open(path, 'w')
	f.close()
	
##########################################################
## Save html given url and path to store
def saveHTML(url, where):
	response = requests.get(url)
	file = open (where, 'w')
	file.write(response.text.encode(C.utf8_tag))
	file.close()

##########################################################
## Switch position of local and visitant
def cross_local_to_visitant(equips, cuotes):
	try:
		auxequip = equips[1]
		equips[1] = equips[0]
		equips[0] = auxequip 
		auxcuotes = cuotes[-1]
		cuotes[-1] = cuotes[0]
		cuotes[0] = auxcuotes
		return equips, cuotes
	except:
		return
