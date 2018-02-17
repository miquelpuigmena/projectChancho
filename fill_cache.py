import unicodecsv as csv

def defineHit(team, sport):
	cache = csv.reader(open("cache/cache.csv","r"))
	for row in cache:
		if row[1]==team:
			if row[0]==sport:
				print "HIT>> "+row[1]+" matches with "+team+". Sport: "+sport
		elif checkHitByPercentage(0.85, team, row[1]):
			print

def checkHitByPercentage(percentage, team1, team2):
	t1 = list(team1)
	t2 = list(team2)
	for letter1 in list(team1):
		print
#defineHit("aja")
	

l1=list("haksdjh kshfljksdf khsfkjhfsd")
l2=list("wekljfw lkdfsjlgk lkfje")
print len(l2)
for letter in l1:
	try:
		l2.remove(letter)
	except:
		pass
print len(l2)

