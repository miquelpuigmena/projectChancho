import constants as C
import csv
from shutil import copyfile
import os
def normalizeTeamNames():
	disposed = 0
	contador = 0
	copyfile(C.dataresultpath_tag, C.dataresultpathaux_tag)
	datar = open(C.dataresultpathaux_tag, 'r')
	dataw = open(C.dataresultpath_tag, 'w')
	readerNormalize = csv.reader(datar)
	writerNormalize = csv.writer(dataw)
	for line in readerNormalize:
		equips_update=[]
		equips = [line[C.local_tag], line[C.visitant_tag]]
		casa = line[C.casa_tag]
		sport = line[C.esport_tag]
		print contador,". Info current match: ", equips[0], equips[1], casa,
		for equip in equips:
			checkNameOwnBettingHouse = priv_checkNameOwnBettingHouse(equip, sport, casa)
			if (checkNameOwnBettingHouse == 0):
				checkNameOnOfficial = priv_checkNameOnOfficial(equip, sport)
				if (checkNameOnOfficial == 0):
					print "DISPOSED"
					disposed += 1
					break
				else:
					for nom_equip in checkNameOnOfficial:
						response = raw_input("Is this a propper hit? ["+nom_equip[0]+", "+equip+"] yes/no (default yes)> ")
						if(response == "yes" or response == ""):
							priv_updateCache_cache(nom_equip[1], casa, equip)
							equips_update.append(nom_equip[0])
							break
			else:
				equips_update.append(checkNameOwnBettingHouse)
		if(len(equips_update)==2):
			line[C.local_tag] = equips_update[0]
			line[C.visitant_tag] = equips_update[1]
			writerNormalize.writerow(line)
		contador += 1
		print
	dataw.close()
	datar.close()
	os.remove(C.dataresultpathaux_tag)
	print "Total disposed: ", disposed
def priv_getPositionOnCache(nom_casa):
	if(nom_casa==C.sportium_tag):
		return C.sportium_pos_cache
	elif (nom_casa==C.codere_tag):
		return C.codere_pos_cache
	elif (nom_casa==C.betfair_tag):
		return C.betfair_pos_cache
	elif (nom_casa==C.bwin_tag):
		return C.bwin_pos_cache
def priv_checkNameOwnBettingHouse(nom_equip, sport, nom_casa):
	cache = open(C.cachepath_tag, 'r')
	readerOwn = csv.reader(cache)
	for line in readerOwn:
		if (line[priv_getPositionOnCache(nom_casa)]==nom_equip and line[C.esport_tag]==sport):
			cache.close()
			return line[C.official_pos_cache]
	cache.close()
	return 0
def priv_similarityStringsByPercentage(string1, string2, ratio):
	contador = 0
	total_length=len(string1)+len(string2)
	vector2=list(string2)
	for letter1 in string1:
	    for letter2 in vector2:
	        if letter1 == letter2:
	            vector2.remove(letter1)
	            contador += 2
	            break
	return float(contador)/total_length >= ratio
def priv_checkNameOnOfficial(nom_equip, sport):
	hits=[]
	cache = open(C.cachepath_tag, 'r')
	readerOfficial = csv.reader(cache)
	contador = 0
	for line in readerOfficial:
		if (priv_similarityStringsByPercentage(nom_equip, line[C.official_pos_cache], C.ratio_hit) and line[C.esport_tag]==sport):
			hits.append((line[C.official_pos_cache], contador))
		contador += 1
	cache.close()
	if (len(hits) == 0) :
		return 0
	else:
		return hits
def priv_updateCache_cache(pos_to_update, nom_casa, nom_equip):
    copyfile(C.cachepath_tag, C.cachepathaux_tag)
    cacher = open(C.cachepathaux_tag, 'r')
    readerUpdateCache = csv.reader(cacher)
    cachew = open(C.cachepath_tag, 'w')
    writerUpdateCache = csv.writer(cachew)
    contador = 0
    for line in readerUpdateCache:
        if (contador == pos_to_update):
            line[priv_getPositionOnCache(nom_casa)] = nom_equip
            writerUpdateCache.writerow(line)
        else:
            writerUpdateCache.writerow(line)
        contador += 1
    cacher.close()
    cachew.close()
    os.remove(C.cachepathaux_tag)
