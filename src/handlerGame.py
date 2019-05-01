#handlerGame.py
#Handler for game messages

# Import python regex module
import re

# Import Telethon modules
from telethon import events

# Import own module
import timeModule, configChecker as conf, handlerFunctions as hfunc

# Event handler for game messages (no client)
@events.register(events.NewMessage(chats = conf.tarGame))
async def game_message_handler(event):
	client = event.client
	gmsg = event.message
	if(conf.master_status == 1):
		if(gmsg.from_id == conf.tarGame):
			strgm = str(gmsg.message.casefold())
			
			if "Your result on the battlefield".casefold() in strgm:
				# Auto-forward report function
				if((conf.status_report != 0) and (conf.status_report is not None)):
					if(conf.status_reportsentcheck == 1):
						if(conf.sent_report == 0):
							if(conf.status_reportlocation == "bot"):
								if(conf.tarCastleBot is not None):
									await client.forward_messages(conf.tarCastleBot, gmsg)
									print(hfunc.currTime() + " Action: Auto forward report (report sent checked): to castle bot")
									await hfunc.setSentCounter("report", 1)
								else:
									print(hfunc.currTime() + " ERROR: Invalid value in tarCastleBot!")
							elif(conf.status_reportlocation == "order"):
								if(conf.tarOrder is not None):
									await client.forward_messages(conf.tarOrder, gmsg)
									print(hfunc.currTime() + " Action: Auto forward report (report sent checked): to order")
									await hfunc.setSentCounter("report", 1)
								else:
									print(hfunc.currTime() + " ERROR: Invalid value in tarOrder!")
							else:
								print(hfunc.currTime() + " Warning: Auto forward report (report sent checked) cancelled possibly due to disabled/invalid report location")
						else:
							print(hfunc.currTime() + " Warning: Auto forward report cancelled due to report count already more than 0!")
					elif(conf.status_reportsentcheck == 0):
						if(conf.status_reportlocation == "bot"):
							if(conf.tarCastleBot is not None):
								await client.forward_messages(conf.tarCastleBot, gmsg)
								print(hfunc.currTime() + " Action: Auto forward report (no report sent check): to castle bot")
								await hfunc.setSentCounter("report", 1)
							else:
								print(hfunc.currTime() + " ERROR: Invalid value in tarCastleBot!")
						elif(conf.status_reportlocation == "order"):
							if(conf.tarOrder is not None):
								await client.forward_messages(conf.tarOrder, gmsg)
								print(hfunc.currTime() + " Action: Auto forward report (no report sent check): to order")
								await hfunc.setSentCounter("report", 1)
							else:
								print(hfunc.currTime() + " ERROR: Invalid value in tarOrder!")
						else:
							print(hfunc.currTime() + " Warning: Auto forward report (no sent check) cancelled possibly due to disabled/invalid report location")
					else:
						print(hfunc.currTime() + " ERROR: Invalid value in statuus_reportsentcheck!")
				else:
					print(hfunc.currTime() + " Notice: Auto forward report cancelled due disabled")
			
			if "Castle trying to pillage a local village. To stop him click /go".casefold() in strgm:
				# Auto-go function
				await hfunc.setSentCounter("go", 0)
				if(conf.status_go == 1):
					await timeModule.sleepyHuman(15, 40)
					if(conf.sent_go == 0):
						await client.send_message(conf.tarGame, "/go")
						print(hfunc.currTime() + " Action: Auto /go")
						await hfunc.setSentCounter("go", 1)
					else:
						print(hfunc.currTime() + " Warning: Auto /go cancelled possibly due to manual /go done!")
				else:
					print(hfunc.currTime() + " Notice: Auto /go not carried out due disabled")
			
			if "You lift up your sword and charge at the violator".casefold() in strgm:
				# Set go counter to 1
				print(hfunc.currTime() + " Action: /go done")
				await hfunc.setSentCounter("go", 1)
				await hfunc.setSentCounter("godef", 0)
			
			forayResults = ["As he was crawling away, you picked up some of the gold he left behind.", 
				"Sadly, he was too strong. Your body hurts, but for some reason you feel enlightened.", 
				"go and he pillaged the village. We hope you feel terrible."]
			for fResults in forayResults:
				if fResults.casefold() in strgm:
					# Auto-def after /go
					await hfunc.setSentCounter("godef", 0)
					if(conf.status_def == 1):
						await timeModule.sleepyHuman(3, 10)
						if(conf.sent_godef == 0):
							await hfunc.setDefend(event)
							print(hfunc.currTime() + " Notice: Done /go. Now defending")
							await hfunc.setSentCounter("godef", 1)
						else:
							print(hfunc.currTime() + " Warning: Auto def (after /go) cancelled possibly due to manual def done!")
					else:
						print(hfunc.currTime() + " Notice: Auto def (after /go) not carried out due disabled")
			
			if "To accept their offer, you shall /pledge to protect".casefold() in strgm:
				# Auto-pledge function
				await hfunc.setSentCounter("pledge", 0)
				if(conf.status_pledge == 1):
					await timeModule.sleepyHuman(5, 10)
					if(conf.sent_pledge == 0):
						await client.send_message(conf.tarGame, "/pledge")
						print(hfunc.currTime() + " Action: Auto /pledge")
						await hfunc.setSentCounter("pledge", 1)
					else:
						print(hfunc.currTime() + " Warning: Auto /pledge cancelled possibly due to manual /pledge done!")
				else:
					print(hfunc.currTime() + " Notice: Auto pledge not carried out due disabled")

			if "You've pledged to protect poor villagers. You can track /tributes".casefold() in strgm:
				# Set pledge counter to 1
				print(hfunc.currTime() + " Action: /pledge done")
				await hfunc.setSentCounter("pledge", 1)

			tactKeywords = ["/tactics_highnest", "/tactics_wolfpack", "/tactics_deerhorn", "/tactics_sharkteeth", 
				"/tactics_dragonscale", "/tactics_moonlight", "/tactics_potato"]
			if "You joined the defensive formations. The next battle is in".casefold() in strgm:
				# Set defend counter to 1 and auto-tactics function
				print(hfunc.currTime() + " Action: Defend done")
				if(conf.sent_go == 1):
					await hfunc.setSentCounter("godef", 1)
				if(conf.status_tact == 1):
					tactKeyMatch = next((x for x in tactKeywords if x in strgm), False)
					if tactKeyMatch != False:
						# Auto-tactics function
						await hfunc.setSentCounter("tact", 0)
						await timeModule.sleepyHuman(3, 6)
						if(conf.sent_tact == 0):
							await hfunc.setTactics(event)
						else:
							print(hfunc.currTime() + " Warning: Auto tactics cancelled possibly due to manual tactics done!")
						
			if "Defence tactics selected.".casefold() in strgm:
				# Sets tactics counter to 1
				print(hfunc.currTime() + " Action: Tactics done")
				await hfunc.setSentCounter("tact", 1)

			if "You are too busy with a different adventure. Try a bit later.".casefold() in strgm:
				# Log when "busy" message appear
				print(hfunc.currTime() + " Warning: Character busy.")
			
			if "[invalid action]".casefold() in strgm:
				# Log when "invalid action" message appear
				print(hfunc.currTime() + " Warning: Invalid action.")
			
			if "The wind is howling in the meadows, castles are unusually quiet. Warriors are mending their wounds and repairing armor after a tiresome battle. All the establishments and castle gates are closed for the next couple of minutes".casefold() in strgm:
				# When battle is still on-going
				# Retry auto report if is set to semi/fully auto mode
				if(conf.status_report == 2):
					if(conf.status_reportsentcheck == 1):
						await timeModule.sleepyHuman(60, 100)
						if(conf.sent_report == 0):
							await event.client.send_message(conf.tarGame, "/report")
							print(hfunc.currTime() + " Action: Retrying auto report (fully auto, with report sent check) due battle on-going")
					elif(conf.status_reportsentcheck == 0):
						await timeModule.sleepyHuman(45, 60)
						await event.client.send_message(conf.tarGame, "/report")
						print(hfunc.currTime() + " Action: Retrying auto report (fully auto, no report sent check) due battle on-going")
				elif(conf.status_report == 1):
					if(conf.status_reportsentcheck == 1):
						await timeModule.sleepyHuman(60, 100)
						if(conf.sent_report == 0):
							await event.client.send_message(conf.tarGame, "/report")
							print(hfunc.currTime() + " Action: Retrying auto report (semi auto, with report sent check) due battle on-going")
