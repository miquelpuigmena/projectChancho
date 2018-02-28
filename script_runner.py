
from runner import runner
from random import randint
import time
contador = 0
while True:
	contador += 1
	sleep_time = randint(2850, 3500)
	print contador, "Sleeping for: "+str(sleep_time)
	runner()
	time.sleep(sleep_time)
	print "RUN"
	contador += 1
	sleep_time = randint(600, 966)
	print contador, "Sleeping for: "+str(sleep_time)
	runner()
	time.sleep(sleep_time)
	print "RUN"
