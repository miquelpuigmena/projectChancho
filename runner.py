from sportium_scraper import runSportium
from codere_scraper import runCodere
from betfair_scraper import runBetfair
from bwin_scraper import runBwin
from utils import emptydocresults
from cacheUpdater import normalizeTeamNames
from alphas import define_Alphas
from drive import upload_file_to_drive, download_file_from_drive
import time
import sys
import constants as C
def runner():
	download_file_from_drive(C.cache_tag, C.cachepath_tag)
	emptydocresults()
	priv_run()
	normalizeTeamNames()
	upload_file_to_drive(C.cache_tag, C.cachepath_tag)
	define_Alphas()

def priv_run():
	args = sys.argv
	print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
	if len(args)==1 or args == C.all_houses_tag:
		runSportium()
		runCodere()
		runBetfair()
		runBwin()
	for arg in args:
		print "Working with ", arg, "..."
		if arg==C.sportium_tag:		
			runSportium()
		elif arg==C.codere_tag:
			runCodere()
		elif arg==C.betfair_tag:
			runBetfair()
		elif arg==C.bwin_tag:
			runBwin()
			
runner()
