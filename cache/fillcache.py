import unicodecsv as csv
import os

def updateCache(pointer, string, casa):
	cache = open("cache.csv", 'r')
	updater = open("updater.csv", 'w')
	for line in cache:
		if (line["Oficial Name"]!=pointer):
			updater.writerow(line)
		else:
			line[casa] = string
			updater.writerow(line)
	cache.close()
	updater.close()
	cache = open("cache.csv", 'w')
	updater = open("updater.csv", 'r')
	for line in updater:
		cache.writerow(line)
	cache.close()
	updater.close()
	os.remove("updater.csv")
	
def hitOwnCasa(string, casa):
	cache = open("cache.csv",'r')
	for linia in cache:
		if (linia[casa]==string):
			cache.close()
			return linia["Oficial Name"]
	cache.close()
	return False
def hitByPercentage(oficial, string, percentage):
	oficiallen=len(oficial)
	for letter in list(string):
		try:
			oficial.remove(letter)
		except:
			pass
	return (len(oficial)/oficiallen) < percentage

def askIfHitIsRight(oficial, string):
	if (input("Possible hit: [oficial: "+oficial+", hit: "+string+"]. Type Yes to confirm hit any other to refuse. ") == "yes"):
		return True
	return False

def hitInOficial(string, casa, percentage):
	cache = open("cache.csv",'r')
	for linia in cache:
		if(linia["Oficial Name"]==string or hitByPercentage(linia["Oficial Name"], string, percentage)):
			if(askIfHitIsRight(linia["Oficial Name"], string))
				cache.close()
				updateCache(linia["Oficial Name"], string, casa )
				return linia["Oficial Name"]
	cache.close()
	return False

list = ["barcelona", "mandril", "aqui", "pataya"]
