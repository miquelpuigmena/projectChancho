import unicodecsv as csv
import requests


path = "csv/dataresult.csv"
##########################################################
## Writing in csv
def writeCSVdocresults(esport, casa, equip, cuota):
	if(len(equip)==2):
		if(len(cuota)==2):
			f = open(path, 'a')
			writer = csv.writer(f)
			writer.writerow((esport, casa, equip[0], equip[1], cuota[0], 'None',cuota[1]))
			f.close()
		elif(len(cuota)==3):
			f = open(path, 'a')
			writer = csv.writer(f)
			writer.writerow((esport, casa, equip[0], equip[1], cuota[0], cuota[1], cuota[2]))
			f.close()

##########################################################
## Prettify String from Sportium
def getStringSportiumPretty(string):
	return string.replace('\n', '')

##########################################################
## Empty csv 2 results doc 
def emptydocresults():
	f = open(path, 'w')
	f.close()

##########################################################
## Save html given url and path to store
def saveHTML(url, where):
	response = requests.get(url)
	file = open (where, "w")
	file.write(response.text.encode('utf-8'))
	file.close()
				

