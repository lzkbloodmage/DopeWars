#timeModule.py
#Contains functions related to time

# Import python datetime module
import datetime

# Import python async i/o module
import asyncio

# Import python secrets and random number module (requires python3.7)
import secrets, random

# Function to get current time
def currTime():
	now = datetime.datetime.now()
	nowFormatted = now.replace(microsecond = 0)
	nowString = str(nowFormatted)
	return nowString

# Function to simulate human wait time
async def sleepyHuman(min, max):
	minSec = min
	maxSec = max
	diffVar = min + 2

	randSec = 0
	randMS1 = 0.0
	randMS2 = 0.0

	if(maxSec > minSec):
		randMS1 = secrets.SystemRandom().random()

		if(maxSec == diffVar):
			randSec = minSec
			randMS2 = random.SystemRandom().random()

		if(maxSec > diffVar):
			if(maxSec - diffVar) == 1:
				mr2 = maxSec - 2
				randSec = random.randint(minSec, mr2)
			else:
				mr1 = maxSec - 1
				randSec = secrets.choice(range(minSec, mr1))
			
			randMS2 = random.SystemRandom().random()
	else:
		randSec = minSec

	reactTime = randSec + randMS1 + randMS2
	await asyncio.sleep(reactTime)