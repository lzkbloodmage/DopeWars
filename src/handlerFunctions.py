#handlerFunctions.py
#Contains functions etc used in multiple handlers.

# Import python random module
import random

# Import Telethon modules
from telethon import events

# Import own module
import timeModule, configChecker as conf

# Assign external variables to local variables
currTime = timeModule.currTime

# Function to set defend status in game
async def setDefend(theEvent):
	client = theEvent.client
	await client.send_message(conf.tarGame, u'\U0001F6E1' + 'Defend')

# Function to set tactics status in game
async def setTactics(theEvent):
	client = theEvent.client
	target = conf.status_tactTarget
	if target == "default":
		tacticsCastle = random.randint(1,2)
		if tacticsCastle == 1:
			await client.send_message(conf.tarGame, "/tactics_dragonscale")
			print(currTime() + " Action: Auto tactics: dragonscale")
			await setSentCounter("tact", 1)
		elif tacticsCastle == 2:
			await client.send_message(conf.tarGame, "/tactics_wolfpack")
			print(currTime() + " Action: Auto tactics: wolfpack")
			await setSentCounter("tact", 1)
		else:
			print(currTime() + " ERROR: Auto default tactics cancelled due to argument error!")
	elif target == "highnest":
		await client.send_message(conf.tarGame, "/tactics_highnest")
		print(currTime() + " Action: Auto tactics: highnest")
		await setSentCounter("tact", 1)
	elif target == "wolfpack":
		await client.send_message(conf.tarGame, "/tactics_wolfpack")
		print(currTime() + " Action: Auto tactics: wolfpack")
		await setSentCounter("tact", 1)
	elif target == "deerhorn":
		await client.send_message(conf.tarGame, "/tactics_deerhorn")
		print(currTime() + " Action: Auto tactics: deerhorn")
		await setSentCounter("tact", 1)
	elif target == "sharkteeth":
		await client.send_message(conf.tarGame, "/tactics_sharkteeth")
		print(currTime() + " Action: Auto tactics: sharkteeth")
		await setSentCounter("tact", 1)
	elif target == "dragonscale":
		await client.send_message(conf.tarGame, "/tactics_dragonscale")
		print(currTime() + " Action: Auto tactics: dragonscale")
		await setSentCounter("tact", 1)
	elif target == "moonlight":
		await client.send_message(conf.tarGame, "/tactics_moonlight")
		print(currTime() + " Action: Auto tactics: moonlight")
		await setSentCounter("tact", 1)
	elif target == "potato":
		await client.send_message(conf.tarGame, "/tactics_potato")
		print(currTime() + " Action: Auto tactics: potato")
		await setSentCounter("tact", 1)
	else:
		print(currTime() + " Error: Auto tactics cancelled due to argument error!")

# Function to set value of various counter variables
async def setSentCounter(act, val):
	if act == "att":
		if val == 0:
			conf.sent_att = 0
		else:
			conf.sent_att = 1
	elif act == "go":
		if val == 0:
			conf.sent_go = 0
		else:
			conf.sent_go = 1
	elif act == "godef":
		if val == 0:
			conf.sent_godef = 0
		else:
			conf.sent_godef = 1
	elif act == "pledge":
		if val == 0:
			conf.sent_pledge = 0
		else:
			conf.sent_pledge = 1
	elif act == "tact":
		if val == 0:
			conf.sent_tact = 0
		else:
			conf.sent_tact = 1
	elif act == "report":
		if val == 0:
			conf.sent_report = 0
		else:
			conf.sent_report = 1
	else:
		print("ERROR: Invalid sentCounter!")
