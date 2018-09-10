#target.py
#Contains functions related to checking/getting targets

# Import python datetime module
import datetime

# Import config file
import config

# Initialise client variable for use in here
client2 = None

# Function to confirm given target ID
async def confirmTargetID(tid):
	did = None

	try:
		print(">> Confirming target ID...")
		
		for dialog in await client2.get_dialogs():
			did = (await client2.get_entity(dialog.id)).id
			if(did == tid):
				print(">> ok")
				return True
	
		return False
	except:
		print("*> ERROR: Possible client error")
		quit()

# Function to get target ID from name
async def getTargetID(tn):
	ntid = None
	
	try:
		print(">>> Getting target ID from target name:",tn)
		
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
			quit()

# Function to check target ID in config.ini
async def checkTargetID(tid, tn):
	ltid = None
	
	try:
		print("> Target:",tid,tn)
		ltid = int(tid)
	except:
		print("*> Target ID is invalid")
		ltid = await getTargetID(tn)
		return ltid
	else:
		boolTarget = await confirmTargetID(ltid)
		if(boolTarget):
			return ltid
		else:
			print("*> Target not found")
			ltid = await getTargetID(tn)
			return ltid

# Function to initialise targets
async def iniTarget(argv):
	print("Initialising targets...")
	
	global client2
	client2 = argv
	
	try:
		a = await checkTargetID(config.tarGame_id, config.tarGame_name)
		b = await checkTargetID(config.tarChat_id, config.tarChat_name)
		c = await checkTargetID(config.tarCastleBot_id, config.tarCastleBot_name)
	except:
		print(str(datetime.datetime.now().replace(microsecond = 0)) + " EXIT DUE ERROR SPECIFIED ABOVE!!!")
		quit()
	else:
		print("Initialisation complete")
		return a, b, c