#handlerOrder.py
#Handler for battle order

# Import python regex module
import re

# Import Telethon modules
from telethon import events

# Import own module
import timeModule, configChecker as conf, handlerFunctions as hfunc

# Function to get specific message from specific chat and id
async def getSpecificMessage(theEvent, chat, msgid):
	client = theEvent.client
	result = await client.get_messages(chat, min_id = msgid - 1, max_id = msgid + 1)
	return result[0]

# Event handler for battle order messages (no client)
@events.register(events.ChatAction(chats = conf.tarOrder))
async def battle_order_handler(event):
	if(conf.master_status == 1):
		if(conf.tarOrder is not None):
			if event.new_pin:
				pinmsg = event.action_message
				if pinmsg.to_id.channel_id == conf.tarOrder:
					battleOrder = await getSpecificMessage(event, conf.tarOrder, pinmsg.reply_to_msg_id)
					strBO = str(battleOrder.raw_text.casefold())

					if re.search(r'(?=.*BATTLE\ IS\ OVER)(?=.*Send)(?=.*reports)', strBO, re.IGNORECASE | re.UNICODE | re.DOTALL):
						# Contains the word 'battle is over', 'send', and 'reports'
						if(conf.status_report == 2):
							await timeModule.sleepyHuman(7, 30)
							if(conf.status_reportsentcheck == 1):
								if(conf.sent_report == 0):
									await event.client.send_message(conf.tarGame, "/report")
									print(hfunc.currTime() + " Action: Auto report (with report sent check)")
								else:
									print(hfunc.currTime() + " Warning: Auto report cancelled possibly due to report already sent!")
							elif(conf.status_reportsentcheck == 0):
								await event.client.send_message(conf.tarGame, "/report")
								print(hfunc.currTime() + " Action: Auto report (no report sent check)")
							else:
								print(hfunc.currTime() + " ERROR: Invalid value in status_reportsentcheck!")
						else:
							print(hfunc.currTime() + " Notice: Auto report not carried out due disabled or not fully auto")

# Event handler for resetting report sent counter (no client)
# Detects whether @CWMiniReportsBot sent battle results to chat
@events.register(events.NewMessage(chats = conf.tarOrder, incoming = True, outgoing = False, forwards = True, from_users = 492881074))
async def minireport_handler(event):
	if(conf.master_status == 1):
		if(conf.tarOrder is not None):
			if((conf.status_report != 0) and (conf.status_report is not None) and (conf.status_reportsentcheck == 1)):
				MRmsg = event.message
				strMR = str(MRmsg.message.casefold())
				MRchid = event.message.fwd_from.channel_id

				if MRchid == 1277259728:
					# If message from Chat Wars Mini Reports channel (1277259728) and sent by CWMiniReportBot (492881074), and contains the specified words...
					if re.search(r'(?=.*\U000026F3)(?=.*Battle\ results)(?=.*\U0001F3C6)(?=.*Scores)', strMR, re.IGNORECASE | re.UNICODE | re.DOTALL):
						print(hfunc.currTime() + " Notice: Resetting counter for report sent to 0")
						await hfunc.setSentCounter("report", 0)