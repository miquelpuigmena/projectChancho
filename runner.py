from sportium_scraper import runSportium
from codere_scraper import runCodere
from betfair_scraper import runBetfair
from bwin_scraper import runBwin
from utils import emptydocresults
from cacheUpdater import normalizeTeamNames
from alphas import define_Alphas
from drive import uploadCache_to_drive_CSV, downloadCache_CSV_from_drive
import time
def runner():
	downloadCache_CSV_from_drive()
	emptydocresults()
	runCodere()
	runSportium()
	runBetfair()
	runBwin()
	normalizeTeamNames()
	uploadCache_to_drive_CSV()
	define_Alphas()
runner()
