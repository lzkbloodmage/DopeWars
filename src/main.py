#!/usr/bin/python3.7

# -*- coding: utf-8 -*-

# Import python async i/o module
import asyncio

# Import python datetime module
import datetime

# Import python secrets and random number module (requires python3.7)
import secrets, random

# Import python regex module
import re

# Import python logging module
import logging

# Import own modules
import configChecker

# Import Telethon modules
from telethon import TelegramClient, events

# Configure Telethon events logging level
logging.basicConfig(level=logging.ERROR)

# Client sign-in settings
sess_name, api_id, api_hash = configChecker.iniTelegramAPI()
client = TelegramClient(sess_name, api_id, api_hash)

# Initialise chat target variables
tarGame = None
tarOrder = None
tarCastleBot = None

# Initialise variables
userME = None


# Function to get current time
def currTime():
	now = datetime.datetime.now()
	nowFormatted = now.replace(microsecond = 0)
	nowString = str(nowFormatted)
	return nowString

# Sign-in Function
async def signin():
	try:
		print("\n" + currTime() + " Signing in...")
		await client.start()
		global userME
		userME = await client.get_me()
	except:
		print("* Sign-in: Connection Error")
		quit()
	else:
		print("Sign-in: Connected")
	
	return None

# Function to set chat target variables
async def getChatTargets():
	global tarGame, tarOrder, tarCastleBot
	tarGame, tarOrder, tarCastleBot = await configChecker.iniChatTargets(client)

# Function for welcome message
async def welcome():
	print("welcome")
	await client.send_message(userME, "Script has (re)started!\n\n" + getAllAutoStatus())

# Function to get script's auto status
def getAllAutoStatus():
	autoStatusMsg = []
	autoStatusMsg.append("=== Status of Auto ===\n")
	return ''.join(autoStatusMsg)

# INCOMPLETE Event handler for game itself
@client.on(events.NewMessage(chats = tarGame))
async def game_message_handler(event):
	gmsg = event.message
	if gmsg.from_id == tarGame:
		strgm = str(gmsg.message.casefold())

# Main Method
async def main():
    # Sign-in
	await signin()
	
	# Get chat targets
	await getChatTargets()
	
	print(currTime() + " Completed startup process")

	await welcome()
	
	await client.run_until_disconnected()

# Start main if main method found
if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
