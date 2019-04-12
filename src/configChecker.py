#configChecker.py
#Contains functions related to checking/getting chat targets

# Import python datetime module
import datetime

# Import config.py file
import config

# Initialise client variable for use in here
client2 = None

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

	tGameName = config.tarGame_name
	tOrderName = config.tarOrder_name
	tCastleBotName = config.tarCastleBot_name
	
	try:
		a = await checkTargetID(tGameID, tGameName, 1)
		b = await checkTargetID(tOrderID, tOrderName, 0)
		c = await checkTargetID(tCastleBotID, tCastleBotName, 0)
	except:
		print(str(datetime.datetime.now().replace(microsecond = 0)) + " EXIT DUE ERROR IN CHECKING CHAT TARGET!!!")
		quit()
	else:
		print("Initialisation complete")
		return a, b, c

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