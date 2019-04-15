#handlerAdmin.py
#Handler for admin commands

# Import python regex module
import re

# Import Telethon modules
from telethon import events

# Import own module
import timeModule, configChecker as conf
from handlerFunctions import currTime

# Function for displaying help message
async def show_help(theEvent):
	help_msg = ("<b>===== HELP =====</b>\n"
		+ "> About: <code>/about</code>\n"
		+ "> View help: <code>/help</code>\n"
		+ "> View help (detailed): <code>/help_details</code>\n"
		+ "> View config: <code>/config</code>\n"
		+ "> View status: <code>/status</code>\n"
		+ "\n<b># # # # # [Auto] # # # # #</b>\n"
		+ "> Master Switch: <code>/switch_{on|off}</code>\n"
		+ "\n> On/Off /go: <code>/set_go_{on|off}</code>\n"
		+ "> On/Off pledge: <code>/set_pledge_{on|off}</code>\n"
		+ "> On/Off defend after /go: <code>/set_def_{on|off}</code>\n"
		+ "> On/Off tactics: <code>/set_tact_{on|off}</code>\n"
		+ ">> Edit tactics: <code>/tactics_{CASTLENAME}</code>\n>>>Example: /tactics_moonlight\n"
		+ "> On/Off report: <code>/set_rep_{full|semi|off}</code>\n"
		+ ">>> On/Off sent check: <code>/set_repsentcheck_{on|off}</code>\n"
		+ ">>> Edit report location: <code>/set_reploc_{order|bot|none}</code>\n"
		+ "\n<b># # # # # [Chat] # # # # #</b>\n"
		+ "> Change Admin chat: <code>/set_admin_{name|id} {{NAME|USERNAME}|{USERID}}</code>\n"
		+ "> Change Order chat: <code>/set_order_{name|id} {{NAME|USERNAME}|{USERID}}</code>\n"
		+ "> Change Castle Bot chat: <code>/set_castlebot_{name|id} {{NAME|USERNAME}|{USERID}}</code>\n"
		+ ">>> Example: /set_castlebot_name Chat Wars Helper\n"
		+ ">>> Example: /set_castlebot_id 526586204\n"
		+ "\n<b>===== NOTES =====</b>\n"
		+ "> No player castle check feature.\n")
	await theEvent.reply(help_msg, parse_mode='html')
	print(currTime() + " Log: Display Help")

# Function for displaying help message (detailed)
async def show_helpdetails(theEvent):
	help_msg = ("<b>=== HELP (DETAILS) ===</b>\n"
		+ "> About: <code>Show the version info and build date.</code>\n\n"
		+ "> View help: <code>Show commands available.</code>\n\n"
		+ "> View help (detailed): <code>Show detailed info about the commands.</code>\n\n"
		+ "> View config: <code>View various chat targets used for this program.\n\
			Admin - For input and detection of commands\n\
			Game - The target game for this script\n\
			Order - The target chat for getting orders\n\
			CastleBot - The castle bot of the player</code>\n\n"
		+ "> View status: <code>View status of all features.</code>\n\n"
		+ "\n<b># # # # # [Auto] # # # # #</b>\n"
		+ "> Master Switch: <code>Kill switch for the program. Stops all function if switch turned off.</code>\n"
		+ "\n> On/Off /go: <code>Enable/disable auto /go</code>\n\n"
		+ "> On/Off pledge: <code>Enable/disable auto /pledge. Only works for knight.</code>\n\n"
		+ "> On/Off defend after /go: <code>Enable/disable auto defend, after auto or manual /go happened.</code>\n\n"
		+ "> On/Off tactics: <code>Enable/disable sentinel tactics. Only works for sentinel.</code>\n\n"
		+ ">> Edit tactics: <code>Edit the tactics that will be used by auto tactics. If player's castle is chosen, \"Invalid action\" message will be encountered.\n\
			==> default - Randomly choose wolfpack or dragonscale.\n\
			==> highnest - Highnest castle\n\
			==> wolfpack - Wolfpack castle\n\
			==> deerhorn - Deerhorn castle\n\
			==> sharkteeth - Sharkteeth castle\n\
			==> dragonscale - Dragonscale castle\n\
			==> moonlight - Moonlight castle\n\
			==> potato - Potato castle</code>\n\n"
		+ "> On/Off report: <code>Enable or disable auto battle report.\n\
			==> off - no auto\n\
			==> semi - semi auto\n\
			==> full - full auto\n\
			\n- For non-wolf players, better to use semi (and no report sent check).\n\
			- For wolf players in squad, use full (with report sent check).\n\
			- Full auto will use the order chat to get cwminireport message and battleover message, to simulate battle finished.\
			It will then auto /report and forward to order chat or castle bot. This was created with wolfpack style of message in mind.\n\
			- Semi auto will auto forward battle report to order chat or castle bot, when user types /report.</code>\n\n"
		+ ">>> On/Off sent check: <code>Enable/disable checks to see whether battle reportt was sent.</code>\n\n"
		+ ">>> Edit report location: <code>Change the location for sending battle report.\n\
			==> bot - castle bot\n\
			==> order - chat containing the battle order\n\
			==> none - disable auto forward of battle report</code>\n\n"
		+ "\n<b># # # [Chat] # # #</b>\n"
		+ "> Change Admin chat: <code>Change the chat/group used for detecting user input commands. 'Saved Messages' will always detect commands!\n\
			Set value to 'none' to remove it.\n\
			==> /set_admin_name - Set the chat using name or username of new target\n\
			==> /set_admin_id - Set the chat using telegram unique ID of the target</code>\n\n"
		+ "> Change Order chat: <code>Change the chat/group used for detecting battle orders. Set value to 'none' to remove it.</code>\n"
		+ "> Change Castle Bot chat: <code>Change the bot used for forwarding battle reports. Set value to 'none' to remove it.</code>\n")
	await theEvent.reply(help_msg, parse_mode='html')
	print(currTime() + " Log: Display Help (detailed)")

# Function for displaying information about this program
async def show_about(theEvent):
	about_msg = ("<b>===== ABOUT =====</b>\n"
		+ "Version: BETA REWRITE v2.0b2\n"
		+ "Build Date: 15 April 2019\n")
	await theEvent.reply(about_msg, parse_mode='html')
	print(currTime() + " Log: Display About")

# Function to get chat name and id as string
async def get_chat_name(client_arg, target_entity):
	tempTarget = None
	tempResult = ""
	if(target_entity is None):
		tempResult = "(" + str(target_entity) +")"
	else:
		tempTarget = await client_arg.get_entity(target_entity)
		try:
			if(tempTarget.title):
				tempResult += (str(tempTarget.title))
		except:
			print(currTime() + " Warning: Checking stored entity (" + str(target_entity) + "): no title")
		
		try:
			if(tempTarget.first_name):
				tempResult += (str(tempTarget.first_name))
		except:
			print(currTime() + " Warning: Checking stored entity (" + str(target_entity) + "): no first name")
		
		try:
			if(tempTarget.last_name):
				tempResult += (str(" " + tempTarget.last_name))
		except:
			print(currTime() + " Warning: Checking stored entity (" + str(target_entity) + "): no last name")
		
		try:
			if(tempTarget.username):
				tempResult += (str(" (</code>@" + tempTarget.username) + "<code>)")
		except:
			print(currTime() + " Warning: Checking stored entity (" + str(target_entity) + "): no username")

		tempResult += (" (" + str(target_entity) + ")")
	return tempResult

# Function for displaying config file settings
async def show_config(theEvent):
	client_arg = theEvent.client
	config_msg = ("<b>=== CONFIGURATION ===</b>\n"
		+ "<b>[Target Chats]</b>\n"
		+ "> Admin: <code>" + await get_chat_name(client_arg, conf.tarAdmin) + "</code>\n"
		+ "> Game: <code>" + await get_chat_name(client_arg, conf.tarGame) + "</code>\n"
		+ "> Order: <code>" + await get_chat_name(client_arg, conf.tarOrder) + "</code>\n"
		+ "> Castle Bot: <code>" + await get_chat_name(client_arg, conf.tarCastleBot) + "</code>\n")
	await theEvent.reply(config_msg, parse_mode='html')
	print(currTime() + " Log: Display Configuration")

# Function for displaying status of program
async def show_status(theEvent):
	sMasterSwitch = None
	sGo = None
	sPledge = None
	sDef = None
	sTact = None
	sTactTarget = None
	sReport = None
	sReportsentcheck = None
	sReportlocation = None

	try: sMasterSwitch = conf.master_status
	except: sMasterSwitch = None
	else: sMasterSwitch = conf.master_status
	try: sGo = conf.status_go
	except: sGo = None
	try: sPledge = conf.status_pledge
	except: sPledge = None
	try: sDef = conf.status_def
	except: sDef = None
	try: sTact = conf.status_tact
	except: sTact = None
	try: sTactTarget = conf.status_tactTarget
	except: sTactTarget = None
	try: sReport = conf.status_report
	except: sReport = None
	try: sReportsentcheck = conf.status_reportsentcheck
	except: sReportsentcheck = None
	try: sReportlocation = conf.status_reportlocation
	except: sReportlocation = None

	statusMsg = []
	statusMsg.append("<b>===== STATUS =====</b>\n")
	if sMasterSwitch == 0:
		statusMsg.append("> Master Switch:- <code>OFF !!!</code> (On: <code>/switch_on</code>)\n")
	elif sMasterSwitch == 1:
		statusMsg.append("> Master Switch:- <code>On</code>  (Off: <code>/switch_off</code>)\n")
	else:
		statusMsg.append("> Master Switch:- <code>ERROR ERROR</code>\n")
	
	statusMsg.append("\n")
	
	if sGo == 0:
		statusMsg.append("> /go:- <code>OFF !!!</code>\n")
	elif sGo == 1:
		statusMsg.append("> /go:- <code>On</code>\n")
	else:
		statusMsg.append("> /go:- <code>ERROR ERROR</code>\n")
	
	if sPledge == 0:
		statusMsg.append("> Pledge:- <code>OFF !!!</code>\n")
	elif sPledge == 1:
		statusMsg.append("> Pledge:- <code>On</code>\n")
	elif sPledge == 2:
		statusMsg.append("> Pledge:- <code>DISABLED</code>\n")
	else:
		statusMsg.append("> Pledge:- <code>ERROR ERROR</code>\n")
	
	if sDef == 0:
		statusMsg.append("> Defend:- <code>OFF !!!</code>\n")
	elif sDef == 1:
		statusMsg.append("> Defend:- <code>On</code>\n")
	else:
		statusMsg.append("> Defend:- <code>ERROR ERROR</code>\n")
	
	if sTact == 0:
		statusMsg.append("> Tactics:- <code>OFF !!!</code>\n")
	elif sTact == 1:
		statusMsg.append("> Tactics:- ")
		if sTactTarget == "default":
			statusMsg.append("<code>Default (wolfpack/dragonscale)</code>\n")
		elif sTactTarget == "highnest":
			statusMsg.append("<code>highnest</code>\n")
		elif sTactTarget == "wolfpack":
			statusMsg.append("<code>wolfpack</code>\n")
		elif sTactTarget == "deerhorn":
			statusMsg.append("<code>deerhorn</code>\n")
		elif sTactTarget == "sharkteeth":
			statusMsg.append("<code>sharkteeth</code>\n")
		elif sTactTarget == "dragonscale":
			statusMsg.append("<code>dragonscale</code>\n")
		elif sTactTarget == "moonlight":
			statusMsg.append("<code>moonlight</code>\n")
		elif sTactTarget == "potato":
			statusMsg.append("<code>potato</code>\n")
		else:
			statusMsg.append("<code>ERROR ERROR</code>\n")
	elif sTact == 2:
		statusMsg.append("> Tactics:- <code>DISABLED</code>\n")
	else:
		statusMsg.append("> Tactics:- <code>ERROR ERROR</code>\n")
	
	if sReport == 0:
		statusMsg.append("> Report:- <code>OFF</code>\n")
	elif sReport == 1:
		statusMsg.append("> Report:- <code>Semi-Auto</code>\n")
	elif sReport == 2:
		statusMsg.append("> Report:- <code>Full-Auto</code>\n")
	else:
		statusMsg.append("> Report:- <code>ERROR ERROR</code>\n")
	
	if sReportsentcheck == 0:
		statusMsg.append(">> Report Sent Check:- <code>OFF</code>\n")
	elif sReportsentcheck == 1:
		statusMsg.append(">> Report Sent Check:- <code>On</code>\n")
	else:
		statusMsg.append(">> Report Sent Check:- <code>ERROR ERROR</code>\n")
	
	if sReportlocation == "bot":
		statusMsg.append(">> Report Location:- <code>bot</code>\n")
	elif sReportlocation == "order":
		statusMsg.append(">> Report Location:- <code>order</code>\n")
	elif sReportlocation == None:
		statusMsg.append(">> Report Location:- <code>DISABLED</code>\n")
	else:
		statusMsg.append(">> Report Sent Check:- <code>ERROR ERROR</code>\n")
	
	await theEvent.reply(''.join(statusMsg), parse_mode='html')
	print(currTime() + " Log: Display Status")

# Function for changing master switch status in settings
async def change_master(theEvent):
	mastmsg = theEvent.message
	strmastm = str(mastmsg.message.casefold())

	if strmastm == "/switch_on":
		conf.master_status = 1
		print(currTime() + " Change: Enabled Master Switch")
		await theEvent.reply("Successfully turned ON <code>MASTER SWITCH</code>\n\nAll functions will run as per settings.", parse_mode='html')
	elif strmastm == "/switch_off":
		conf.master_status = 0
		print(currTime() + " Change: Disabled Master Switch")
		await theEvent.reply("Successfully turned OFF <code>MASTER SWITCH</code>\n\nWARNING: All functions are disabled, regardless of settings!", parse_mode='html')
	else:
		await theEvent.reply("ERROR: Invalid command!", parse_mode='html')


# Function for changing tactics target in settings
async def change_tactics(theEvent):
	tactmsg = theEvent.message
	strtactm = str(tactmsg.message.casefold())

	if strtactm == "/tactics_highnest":
		conf.status_tactTarget = "highnest"
		print(currTime() + " Change: Tactics set to highnest")
		await theEvent.reply("Successfully changed tactics target (<code>highnest</code>)!", parse_mode='html')
	elif strtactm == "/tactics_wolfpack":
		conf.status_tactTarget = "wolfpack"
		print(currTime() + " Change: Tactics set to wolfpack")
		await theEvent.reply("Successfully changed tactics target (<code>wolfpack</code>)!", parse_mode='html')
	elif strtactm == "/tactics_deerhorn":
		conf.status_tactTarget = "deerhorn"
		print(currTime() + " Change: Tactics set to deerhorn")
		await theEvent.reply("Successfully changed tactics target (<code>deerhorn</code>)!", parse_mode='html')
	elif strtactm == "/tactics_sharkteeth":
		conf.status_tactTarget = "sharkteeth"
		print(currTime() + " Change: Tactics set to sharkteeth")
		await theEvent.reply("Successfully changed tactics target (<code>sharkteeth</code>)!", parse_mode='html')
	elif strtactm == "/tactics_dragonscale":
		conf.status_tactTarget = "dragonscale"
		print(currTime() + " Change: Tactics set to dragonscale")
		await theEvent.reply("Successfully changed tactics target (<code>dragonscale</code>)!", parse_mode='html')
	elif strtactm == "/tactics_moonlight":
		conf.status_tactTarget = "moonlight"
		print(currTime() + " Change: Tactics set to moonlight")
		await theEvent.reply("Successfully changed tactics target (<code>moonlight</code>)!", parse_mode='html')
	elif strtactm == "/tactics_potato":
		conf.status_tactTarget = "potato"
		print(currTime() + " Change: Tactics set to potato")
		await theEvent.reply("Successfully changed tactics target (<code>potato</code>)!", parse_mode='html')
	elif strtactm == "/tactics_default":
		conf.status_tactTarget = "default"
		print(currTime() + " Change: Tactics set to default")
		await theEvent.reply("Successfully changed tactics target (<code>default</code>)!", parse_mode='html')
	else:
		await theEvent.reply("ERROR: Invalid castle input!", parse_mode='html')

# Function for changing the chat targets using command
async def change_chat_details(theEvent, target_type, input_type):
	cmsg = theEvent.message
	target_input = str(cmsg.message).split(' ', 1)
	target_entity = None
	target_id = None
	target_name = None
	target_username = None
	none_flag = 0

	if(len(target_input) > 1):
		try:
			if(target_input[1].casefold() == "none"):
				none_flag = 1
			else:
				if(input_type == "int"):
					target_entity = await theEvent.client.get_entity(int(target_input[1]))
					target_id = target_entity.id
					try:
						if(target_entity.title):
							target_name = str(target_entity.title)
					except:
						print(currTime() + " Warning: Input entity (" + str(target_input[1]) + ") has no title")
					
					try:
						if(target_entity.first_name):
							target_name = (str(target_entity.first_name))
					except:
						print(currTime() + " Warning: Input entity (" + str(target_input[1]) + ") has no first name")
					
					try:
						if(target_entity.last_name):
							target_name += (str(" " + target_entity.last_name))
					except:
						print(currTime() + " Warning: Input entity (" + str(target_input[1]) + ") has no last name")
					
					try:
						if(target_entity.username):
							target_username = str("@" + target_entity.username)
					except:
						print(currTime() + " Warning: Input entity (" + str(target_input[1]) + ") has no username")
				elif(input_type == "str"):
					target_entity = await theEvent.client.get_entity(str(target_input[1]))
					target_id = target_entity.id
					try:
						if(target_entity.title):
							target_name = str(target_entity.title)
					except:
						print(currTime() + " Warning: Input entity (" + str(target_input[1]) + ") has no title")
					
					try:
						if(target_entity.first_name):
							target_name = (str(target_entity.first_name))
					except:
						print(currTime() + " Warning: Input entity (" + str(target_input[1]) + ") has no first name")
					
					try:
						if(target_entity.last_name):
							target_name += (str(" " + target_entity.last_name))
					except:
						print(currTime() + " Warning: Input entity (" + str(target_input[1]) + ") has no last name")
					
					try:
						if(target_entity.username):
							target_username = str("@" + target_entity.username)
					except:
						print(currTime() + " Warning: Input entity (" + str(target_input[1]) + ") has no username")
				else:
					print(currTime() + " ERROR: Invalid argument for input_type in change_chat_details function!")
					await theEvent.reply("ERROR: Invalid argument encountered!", parse_mode='html')
				
		except:
			print(currTime() + " ERROR: Unable to change", str(target_type), "chat, due problem with getting entity using", str(input_type), "input")
			await theEvent.reply("ERROR: Unable to get data about input target!", parse_mode='html')
		else:
			if(target_type == "admin"):
				if(none_flag == 0):
					conf.tarAdmin = int(target_id)
					print(currTime() + " Change: Changed admin chat to", str(target_id), str(target_name), str(target_username))
					tempString = "Successfully changed <code>admin chat</code> to:\n"
					tempString += "TG ID: " + str(target_id) + "\n"
					tempString += "TG Name: " + str(target_name) + "\n"
					tempString += "TG Username: " + str(target_username)
					await theEvent.reply(tempString, parse_mode='html')
				else:
					conf.tarAdmin = conf.userME.id
					print(currTime() + " Change: Changed admin chat to 'Saved Message'")
			elif(target_type == "order"):
				if(none_flag == 0):
					conf.tarOrder = int(target_id)
					print(currTime() + " Change: Changed order chat to", str(target_id), str(target_name), str(target_username))
					tempString = "Successfully changed <code>order chat</code> to:\n"
					tempString += "TG ID: " + str(target_id) + "\n"
					tempString += "TG Name: " + str(target_name) + "\n"
					tempString += "TG Username: " + str(target_username)
					await theEvent.reply(tempString, parse_mode='html')
				else:
					conf.tarOrder = None
					print(currTime() + " Change: Changed order chat to none")
			elif(target_type == "castlebot"):
				if(none_flag == 0):
					conf.tarCastleBot = int(target_id)
					print(currTime() + " Change: Changed castle bot chat to", str(target_id), str(target_name), str(target_username))
					tempString = "Successfully changed <code>order chat</code> to:\n"
					tempString += "TG ID: " + str(target_id) + "\n"
					tempString += "TG Name: " + str(target_name) + "\n"
					tempString += "TG Username: " + str(target_username)
					await theEvent.reply(tempString, parse_mode='html')
				else:
					conf.tarCastleBot = None
					print(currTime() + " Change: Changed castle bot chat to none")
			else:
				print(currTime() + " ERROR: Invalid argument for target_type in change_chat_details function!")
	else:
		print(currTime() + " Warning: Invalid input for changing", str(target_type), "chat")

# Function for changing status in settings
async def change_status(theEvent):
	statmsg = theEvent.message
	strstatm = str(statmsg.message.casefold())

	if "/set_admin_id".casefold() in strstatm:
		await change_chat_details(theEvent, "admin", "int")
	elif "/set_admin_name".casefold() in strstatm:
		await change_chat_details(theEvent, "admin", "str")
	elif "/set_order_id".casefold() in strstatm:
		await change_chat_details(theEvent, "order", "int")
	elif "/set_order_name".casefold() in strstatm:
		await change_chat_details(theEvent, "order", "str")
	elif "/set_castlebot_id".casefold() in strstatm:
		await change_chat_details(theEvent, "castlebot", "int")
	elif "/set_castlebot_name".casefold() in strstatm:
		await change_chat_details(theEvent, "castlebot", "str")
	elif strstatm == "/set_go_on":
		conf.status_go = 1
		print(currTime() + " Change: Enabled auto /ago")
		await theEvent.reply("Successfully enabled <code>auto /go</code>", parse_mode='html')
	elif strstatm == "/set_go_off":
		conf.status_go = 0
		print(currTime() + " Change: Disabled auto /ago")
		await theEvent.reply("Successfully disabled <code>auto /go</code>", parse_mode='html')
	elif strstatm == "/set_pledge_on":
		conf.status_pledge = 1
		print(currTime() + " Change: Enabled auto pledge")
		await theEvent.reply("Successfully enabled <code>auto pledge</code>", parse_mode='html')
	elif strstatm == "/set_pledge_off":
		conf.status_pledge = 0
		print(currTime() + " Change: Disabled auto pledge")
		await theEvent.reply("Successfully disabled <code>auto pledge</code>", parse_mode='html')
	elif strstatm == "/set_def_on":
		conf.status_def = 1
		print(currTime() + " Change: Enabled auto defend")
		await theEvent.reply("Successfully enabled <code>auto defend</code>", parse_mode='html')
	elif strstatm == "/set_def_off":
		conf.status_def = 0
		print(currTime() + " Change: Disabled auto defend")
		await theEvent.reply("Successfully disabled <code>auto defend</code>", parse_mode='html')
	elif strstatm == "/set_tact_on":
		conf.status_tact = 1
		print(currTime() + " Change: Enabled auto tactics")
		await theEvent.reply("Successfully enabled <code>auto tactics</code>", parse_mode='html')
	elif strstatm == "/set_tact_off":
		conf.status_tact = 0
		print(currTime() + " Change: Disabled auto tactics")
		await theEvent.reply("Successfully disabled <code>auto tactics</code>", parse_mode='html')
	elif strstatm == "/set_rep_full":
		conf.status_report = 2
		print(currTime() + " Change: Enabled auto report (full auto)")
		await theEvent.reply("Successfully enabled <code>auto report (full auto)</code>", parse_mode='html')
	elif strstatm == "/set_rep_semi":
		conf.status_report = 1
		print(currTime() + " Change: Enabled auto report (semi auto)")
		await theEvent.reply("Successfully enabled <code>auto report (semi auto)</code>", parse_mode='html')
	elif strstatm == "/set_rep_off":
		conf.status_report = 0
		print(currTime() + " Change: Disabled auto report")
		await theEvent.reply("Successfully disabled <code>auto report</code>", parse_mode='html')
	elif strstatm == "/set_repsentcheck_on":
		conf.status_reportsentcheck = 1
		print(currTime() + " Change: Enabled report sent check")
		await theEvent.reply("Successfully enabled <code>report sent check</code>", parse_mode='html')
	elif strstatm == "/set_repsentcheck_off":
		conf.status_reportsentcheck = 0
		print(currTime() + " Change: Disabled report sent check")
		await theEvent.reply("Successfully disabled <code>report sent check</code>", parse_mode='html')
	elif strstatm == "/set_reploc_bot":
		conf.status_reportlocation = "bot"
		print(currTime() + " Change: Report location set to \"bot\"")
		await theEvent.reply("Successfully changed <code>report location</code> to bot", parse_mode='html')
	elif strstatm == "/set_reploc_order":
		conf.status_reportlocation = "order"
		print(currTime() + " Change: Report location set to \"order\"")
		await theEvent.reply("Successfully changed <code>report location</code> to order", parse_mode='html')
	elif strstatm == "/set_reploc_none":
		conf.status_reportlocation = None
		print(currTime() + " Change: Report location set to \"none\"")
		await theEvent.reply("Successfully changed <code>report location</code> to none", parse_mode='html')
	else:
		await theEvent.reply("ERROR: Invalid command!", parse_mode='html')

# Function to match input commands
async def check_commands(theEvent):
	admsg = theEvent.message
	stradm = str(admsg.message.casefold())
	event = theEvent

	# Send help message if /help entered
	if re.match(r'(?=\/help$)', stradm, re.IGNORECASE | re.UNICODE):
		await show_help(event)
	if re.match(r'(?=\/help_details$)', stradm, re.IGNORECASE | re.UNICODE):
		await show_helpdetails(event)
	if re.match(r'(?=\/about$)', stradm, re.IGNORECASE | re.UNICODE):
		await show_about(event)
	if re.match(r'(?=\/config$)', stradm, re.IGNORECASE | re.UNICODE):
		await show_config(event)
	if re.match(r'(?=\/status$)', stradm, re.IGNORECASE | re.UNICODE):
		await show_status(event)
	if re.match(r'(?=\/switch_)', stradm, re.IGNORECASE | re.UNICODE):
		await change_master(event)
	if re.match(r'(?=\/tactics_)', stradm, re.IGNORECASE | re.UNICODE):
		await change_tactics(event)
	if re.match(r'(?=\/set_)', stradm, re.IGNORECASE | re.UNICODE):
		await change_status(event)
	
# Event handler for admin messages (no client)
@events.register(events.NewMessage(chats = conf.tarAdmin))
async def admin_message_handler(event):
	if(conf.tarAdmin != conf.userME.id):
		admsg = event.message
		if(admsg.from_id == conf.userME.id):
			try:
				if(admsg.to_id.user_id):
					pass
			except:
				pass
			else:
				if(admsg.to_id.user_id == conf.tarAdmin):
					await check_commands(event)

# Event handler for admin messages (no client)
@events.register(events.NewMessage(chats = conf.userME))
async def me_message_handler(event):
	admsg = event.message
	if(admsg.from_id == conf.userME.id):
		try:
			if(admsg.to_id.user_id):
				pass
		except:
			pass
		else:
			if(admsg.to_id.user_id == conf.userME.id):
				await check_commands(event)