#!/usr/bin/python3
# -*- coding: utf-8 -*-

# DopeWars version 1.0

# Import python async i/o module
import asyncio

# Import python datetime module
import datetime

# Import python secrets and random number module
import secrets, random

# Import python regex module
import re

# Import own modules
import config, target

# Import telethon modules
from telethon import TelegramClient, events, logging

# Configure telethon events logging level
logging.basicConfig(level=logging.ERROR)

# Client sign-in settings
client = TelegramClient(config.session_name, config.api_id, config.api_hash)

# Initialise chat variables
tarGame = None
tarChat = None
tarCastleBot = None

# Initialise variable
attackTarget = None
reportSent = 0
foraySent = 0
pledgeSent = 0

# Function to get current time
def currTime():
	now = datetime.datetime.now()
	nowM = now.replace(microsecond = 0)
	nowMS = str(nowM)
	return nowMS

# Sign-in Function
async def signin():
	try:
		print("\n" + currTime() + " Signing in...")
		await client.start()
	except:
		print("* Sign-in: Connection Error")
		quit()
	else:
		print("Sign-in: Connected")
	
	return None

# Function to set target game/chat/bot variables
async def getTarget():
	global tarGame, tarChat, tarCastleBot
	tarGame, tarChat, tarCastleBot = await target.iniTarget(client)

# Function to get specific message from specific chat and id
async def getSpecificMessage(chat, msgid):
	result = await client.get_messages(chat, min_id = msgid - 1, max_id = msgid + 1)
	return result[0]

# Function to set defend status
async def setStatDef():
	await client.send_message(tarGame, u'\U0001F6E1' + 'Defend')

# Function to set attack status
async def setStatAtt():
	await client.send_message(tarGame, u'\U00002694' + 'Attack')

# Function to set value of various counter variables
async def setSentCounter(act, val):
	global reportSent
	global foraySent
	global pledgeSent

	if act == "report":
		if val == 0:
			reportSent = 0
		else:
			reportSent += 1
	elif act == "foray":
		if val == 0:
			foraySent = 0
		else:
			foraySent += 1
	elif act == "pledge":
		if val == 0:
			pledgeSent = 0
		else:
			pledgeSent += 1

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

# INCOMPLETE Event handler for game itself
@client.on(events.NewMessage(chats = tarGame))
async def game_message_handler(event):
	gmsg = event.message
	if gmsg.from_id == tarGame:
		strgm = str(gmsg.message.casefold())

		if "Choose an enemy".casefold() in strgm:
			# Auto-attack function
			await sleepyHuman(1, 2)
			global attackTarget
			await client.send_message(tarGame, attackTarget)
			attackTarget = None
		if "Your result on the battlefield".casefold() in strgm:
			# Auto-result function
			if reportSent == 0:
				await client.forward_messages(tarChat, gmsg)
				print(currTime() + " Notice: Auto-result now")
				await setSentCounter("report", 1)
			else:
				print(currTime() + " Warning: Auto-result cancelled due to report count already more than 0!")
		if "You were strolling around on your horse when you noticed".casefold() in strgm:
			# Auto-foray function
			await setSentCounter("foray", 0)
			await sleepyHuman(15, 30)
			if foraySent == 0:
				await client.send_message(tarGame, "/go")
				print(currTime() + " Notice: Auto /go")
				await setSentCounter("foray", 1)
			else:
				print(currTime() + " Warning: Auto /go cancelled possibly due to manual /go done!")
		if "You lift up your sword and charge at the violator".casefold() in strgm:
			# Sets foray counter to 1
			print(currTime() + " Notice: /go done")
			await setSentCounter("foray", 1)
		if "To accept their offer, you shall /pledge to protect".casefold() in strgm:
			# Auto-pledge function
			await setSentCounter("pledge", 0)
			await sleepyHuman(5, 10)
			if pledgeSent == 0:
				await client.send_message(tarGame, "/pledge")
				print(currTime() + " Notice: Auto /pledge")
				await setSentCounter("pledge", 1)
			else:
				print(currTime() + " Warning: Auto /pledge cancelled possibly due to manual /pledge done!")
		if "You've pledged to protect poor villagers. You can track /tributes".casefold() in strgm:
			# Sets pledge counter to 1
			print(currTime() + " Notice: /pledge done")
			await setSentCounter("pledge", 1)
		# HERE: FUTURE FEATURE FOR QUEST MESSAGE AUTO FORWARD TO CASTLE BOT


# Event handler for battle order
@client.on(events.ChatAction(chats = tarChat))
async def battle_order_handler(event):
	if event.new_pin:
		pinmsg = event.action_message
		if pinmsg.to_id.channel_id == tarChat:
			battleOrder = await getSpecificMessage(tarChat, pinmsg.reply_to_msg_id)
			strBO = str(battleOrder.raw_text.casefold())

			global attackTarget

			if re.search(r'(?=.*FULL DEFEND)(?=.*\U0001F6E1)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'full defend' and sheild emoji
				await sleepyHuman(0,1)
				await setStatDef()
			elif re.search(r'(?=.*Defend)(?=.*\U0001F6E1)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'defend' and shield emoji
				await sleepyHuman(3, 7)
				await setStatDef()
			elif re.search(r'(?=.*Defense)(?=.*\U0001F6E1)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'defense' and shield emoji
				await sleepyHuman(10, 20)
				await setStatDef()
			if re.search(r'(?=.*BATTLE\ IS\ OVER)(?=.*Send)(?=.*reports)', strBO, re.IGNORECASE | re.UNICODE | re.DOTALL):
				# Contains the word 'battle is over', 'send', and 'reports'
				await sleepyHuman(7, 25)
				if(reportSent == 0):
					await client.send_message(tarGame, "/report")
					print(currTime() + " Notice: Auto-reporting now")
				else:
					print(currTime() + " Warning: Auto-report cancelled possibly due to manual report done!")
			if re.search(r'(?=.*Attack)(?=.*\U0001F409)(?=.*DRAGONS)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'attack', 'dragons', and dragon emoji
				attackTarget = "\U0001F409"
				await setStatAtt()
			if re.search(r'(?=.*Attack)(?=.*\U0001F954)(?=.*POTATO)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'attack', 'potato', and potato emoji
				attackTarget = "\U0001F954"
				await setStatAtt()
			if re.search(r'(?=.*Attack)(?=.*\U0001F985)(?=.*EAGLES)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'attack', 'eagles', and eagle emoji
				attackTarget = "\U0001F985"
				await setStatAtt()
			if re.search(r'(?=.*Attack)(?=.*\U0001F98C)(?=.*DEERS)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'attack', 'deers', and deer emoji
				attackTarget = "\U0001F98C"
				await setStatAtt()
			if re.search(r'(?=.*Attack)(?=.*\U0001F988)(?=.*SHARKS)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'attack', 'sharks', and shark emoji
				attackTarget = "\U0001F988"
				await setStatAtt()
			if re.search(r'(?=.*Attack)(?=.*\U0001F311)(?=.*MOON)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'attack', 'moon', and moon emoji
				attackTarget = "\U0001F311"
				await setStatAtt()
			if re.search(r'(?=.*Attack)(?=.*\U0001F43A)(?=.*WOLF)', strBO, re.IGNORECASE | re.UNICODE):
				# Contains the word 'attack', 'wolf', and wolf emoji
				attackTarget = "\U0001F43A"
				await setStatAtt()

# Event handler for resetting report sent counter
@client.on(events.NewMessage(chats = tarChat, incoming = True, outgoing = False, forwards = True, from_users = 492881074))
async def minireport_handler(event):
	MRmsg = event.message
	strMR = str(MRmsg.message.casefold())
	MRchid = event.message.fwd_from.channel_id

	if MRchid == 1277259728:
		# If message from the channel id (1277259728) and CWMiniReportBot (492881074), and contains the specified words...
		if re.search(r'(?=.*\U000026F3)(?=.*Battle\ results)(?=.*\U0001F3C6)(?=.*Scores)', strMR, re.IGNORECASE | re.UNICODE | re.DOTALL):
			await setSentCounter("report", 0)
			print(currTime() + " Notice: Resetting value for report sent to 0.")

# Main Method
async def main():		
	# Sign-in
	await signin()
	
	# Get targets
	await getTarget()
	
	print(currTime() + " Completed startup process")
	
	await client.run_until_disconnected()

# Start main if main method found
if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())