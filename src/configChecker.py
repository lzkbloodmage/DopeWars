#configChecker.py
#Contains functions related to checking/getting chat targets

# Import python datetime module
import datetime

# Import Telethon module
from telethon import TelegramClient

# Import config.py file
import config

# Initialise client variable for use in here
client2 = None


##### Initialse variable for use with other modules too #####
# Initialise chat target variables
tarGame = None
tarOrder = None
tarCastleBot = None
tarAdmin = None

# Initialise variables
userME = None

# Initialise admin command status variables
master_status = None
status_go = None
status_pledge = None
status_def = None
status_tact = None
status_tactTarget = "default"
status_report = None
status_reportsentcheck = None
status_reportlocation = None

# Initialise counter variables
attack_target = None
#sent_att = 0
sent_go = 0
sent_godef = 0
sent_pledge = 0
sent_tact = 0
sent_report = 0

##############################################################


# Function to confirm given chat target ID
async def confirmTargetID(tid):
	cid = None

	try:
		print(">> Confirming target ID...")
		
		for dialog in await client2.get_dialogs():
			cid = (await client2.get_entity(dialog.id)).id
			if(cid == tid):
				print(">> ok")
				return True

		return False
	except:
		print("*> ERROR: Possible client error")
		quit()

# Function to get target ID from name
async def getTargetID(tn, reqflag):
	ntid = None
	
	try:
		print(">>> Getting target ID from target name:", tn)
		
		for dialog in await client2.get_dialogs():
			if(dialog.name == tn):
				ntid = (await client2.get_entity(dialog.id)).id
				print(">>>> Target ID found:", ntid)
				break
	except:
		print("**> ERROR: Possible client error")
		quit()
	else:
		try:
			ltid = int(ntid)
			return ltid
		except:
			print("***> ERROR:  Unable to find target ID from target name")

			if(reqflag == True):
				print("****> WARNING: TERMINATING DUE ERROR FOR COMPULSORY TARGET")
				quit()
			else:
				print("****> WARNING: SKIPPING DUE ERROR AND NOT COMPULSORY")
				return None

# Function to check target ID in config.ini
async def checkTargetID(tid, tn, tflag):
	chkid = None
	required = False
	flagValue = None

	try:
		flagValue = int(tflag)
	except:
		print("> ERROR: tflag in checkTargetID function is invalid! Setting it to false.")
		required == False
	else:
		if(flagValue == 1):
			required = True
		elif(flagValue == 0):
			required == False
		else:
			print("> ERROR: tflag in checkTargetID function is out of bounds. Setting it to false.")
			required == False
	
	try:
		# Get target ID from variable given
		print("> Target:",tid,tn)
		chkid = int(tid)
	except:
		print("*> Target ID is invalid")
		chkid = await getTargetID(tn, required)
		return chkid
	else:
		# Confirm the target ID if ID is valid int
		boolTarget = await confirmTargetID(chkid)
		if(boolTarget):
			return chkid
		else:
			print("*> Target not found")
			chkid = await getTargetID(tn, required)
			return chkid

# Function to initialise targets
async def iniChatTargets(argv):
	print("Initialising chat targets...")
	
	global client2
	client2 = argv
	
	# Get chat target values from config file
	tGameID = config.tarGame_id
	tOrderID = config.tarOrder_id
	tCastleBotID = config.tarCastleBot_id
	tAdminID = config.tarAdmin_id
	tGameName = config.tarGame_name
	tOrderName = config.tarOrder_name
	tCastleBotName = config.tarCastleBot_name
	tAdminName = config.tarAdmin_name
	
	try:
		a = await checkTargetID(tGameID, tGameName, 1)
		b = await checkTargetID(tOrderID, tOrderName, 0)
		c = await checkTargetID(tCastleBotID, tCastleBotName, 0)
		d = await checkTargetID(tAdminID, tAdminName, 0)
		if(d is None):
			d = await client2.get_me()
			d = int(d.id)
	except:
		print(str(datetime.datetime.now().replace(microsecond = 0)) + " EXIT DUE ERROR IN CHECKING CHAT TARGET!!!")
		quit()
	else:
		print("Initialisation complete")
		return a, b, c, d

# Function to get Telegram api variables
def iniTelegramAPI():
	tgSessName = config.session_name
	tgAPIID = config.api_id
	tgAPIHash = config.api_hash
	
	if None not in (tgSessName, tgAPIID, tgAPIHash):
		return tgSessName, tgAPIID, tgAPIHash
	else:
		print("ERROR: Telegram API variables not complete!")
		quit()

# Function to get variable values from config file
def iniStatus():
	try: sGo = int(config.status_go)
	except: sGo = None
	try: sPledge = int(config.status_pledge)
	except: sPledge = None
	try: sDef = int(config.status_def)
	except: sDef = None
	try: sTact = int(config.status_tact)
	except: sTact = None
	try: sTactTarget = config.status_tactTarget
	except: sTactTarget = None
	try: sReport = int(config.status_report)
	except: sReport = None
	try: sReportsentcheck = int(config.status_report_sentcheck)
	except: sReportsentcheck = None
	try: sReportlocation = config.status_report_location
	except: sReportlocation = None
	
	return sGo, sPledge, sDef, sTact, sTactTarget, sReport, sReportsentcheck, sReportlocation

# Client sign-in settings
sess_name, api_id, api_hash = iniTelegramAPI()
client = TelegramClient(sess_name, api_id, api_hash)

# Main. Assign values from config file to variables
async def start():
	global tarGame
	global tarOrder
	global tarCastleBot
	global tarAdmin
	tarGame, tarOrder, tarCastleBot, tarAdmin = await iniChatTargets(client)

	global userME
	userME = await client.get_entity("me")

	global master_status
	try: master_status = int(config.master_status)
	except: master_status = None

	global status_go
	global status_pledge
	global status_def
	global status_tact
	global status_tactTarget
	global status_report
	global status_reportsentcheck
	global status_reportlocation
	status_go, status_pledge, status_def, status_tact, status_tactTarget, status_report, status_reportsentcheck, status_reportlocation = iniStatus()