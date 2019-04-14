#!/usr/bin/python3.7

# -*- coding: utf-8 -*-

# Import python async i/o module
import asyncio

# Import python logging module
import logging

# Import Telethon modules
from telethon import TelegramClient

# Import own modules
import timeModule, configChecker as conf
import handlerAdmin, handlerGame, handlerOrder

# Configure Telethon events logging level
logging.basicConfig(level=logging.ERROR)

# Assign external variables to local variables
client = conf.client
currTime = timeModule.currTime

# Sign-in Function
async def signin():
	try:
		print("\n" + currTime() + " Signing in...")
		await client.start()
		conf.userME = await client.get_me()
	except:
		print("* Sign-in: Connection Error")
		quit()
	else:
		print("Sign-in: Connected")
	
	return None

# Function for welcome message
async def welcome():
	print("welcome")
	await client.send_message(conf.userME, "Notice: Script has (re)started!\n\n\
		<code>/status</code> for current script status\n\
		<code>/help</code> for help", parse_mode='html')

# Main Method
async def main():
    # Sign-in
	await signin()
	
	# Initialise and set variables from config file
	await conf.start()

	print(currTime() + " Completed startup process")

	# Add handlers
	client.add_event_handler(handlerAdmin.admin_message_handler)
	client.add_event_handler(handlerAdmin.me_message_handler)
	client.add_event_handler(handlerGame.game_message_handler)
	client.add_event_handler(handlerOrder.battle_order_handler)
	client.add_event_handler(handlerOrder.minireport_handler)

	await welcome()
	
	await client.run_until_disconnected()

# Start main if main method found
if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
