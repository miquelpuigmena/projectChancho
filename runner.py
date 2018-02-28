from sportium_scraper import runSportium
from codere_scraper import runCodere
from betfair_scraper import runBetfair
from bwin_scraper import runBwin
from utils import emptydocresults
from cacheUpdater import normalizeTeamNames
from alphas import define_Alphas
import time
def runner():
	emptydocresults()
	runCodere()
	runSportium()
	runBetfair()
	runBwin()
	normalizeTeamNames()
	define_Alphas()
    
runner()
