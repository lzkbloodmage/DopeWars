# DopeWars
Dope Wars is a Telegram client script for lazy warriors. It contains a suite of features for automation of daily war and other actions. It is compatible with EU version, and untested for RU version.

# Disclaimer
This script is created for <b>Educational Purposes</b> only. 

It has not been tested for long hours or real-world usage. <b>Use this at your own risk!</b> None of the authors, contributors, or anyone else connected with this project, in any way whatsover, will be liable for any losses, damages, account bans, or any other issues caused by the usage of this script.

By using this script, you hereby agree that you will be responsible for any issues that might arise from its usage.

# Getting Started
## Installation
1. Install [Python](https://www.python.org/downloads/) (Min req: Python 3.6)
2. Install [Telethon](https://github.com/LonamiWebs/Telethon) (Min req: Telethon 1.1.1)
3. Clone or download this git repo

## Configuration
### Getting API id
1. Log in to Telegram core: https://my.telegram.org/
2. Go to ['API development tools'](https://my.telegram.org/apps) and fill out the form
3. The <b>api_id</b> and <b>api_hash</b> parameters will be given

### Editing config.ini
The settings are located in config.ini file, located in "src" folder. Below are the explainations for the various fields.

* <b>session_name</b>: Desired name for your session. Can be anything.
* <b>api_id</b>: API id to use for this script. Use the API id given in Telegram core.
* <b>api_hash</b>: API hash to use for this script. Use the API hash given in Telegram core.

* <b>targetGame_id</b>: Unique ID of the game. EU version: 408101137
* <b>targetChat_id</b>: Unique ID of the chat for receiving of pinned orders. Typically castle chat or squad chat.
* <b>targetCastleBot_id</b>: Unique ID of the castle bot. For forwarding of quest results to this bot.

* <b>targetGame</b>: Name of the game. This will only be used if ID entered is invalid or blank.
* <b>targetChat</b>: Name of the chat for receiving of orders. This will only be used if the ID entered is invalid or blank.
* <b>targetCastleBot</b>: Name of the castle bot. This will only be used if the ID entered is invalid or blank.

## Running
### Initial Run
1. Run "python bot.py" in console
2. Insert phone number
3. Insert Telegram confirmation code
4. Insert 2FA Telegram password (if needed)

### Subsequent Runs
a. Run as per the command in the initial run ("python bot.py")

b. [Linux] If you want to run it in background, run "nohup python bot.py &" in console

c. [Linux] Or run script as service in Linux

# Features
Version: 1.0

### Current
* Get orders from chat
* Auto attack and defend based on orders received
* Auto sending of /report to game
* Auto forwarding of battle report to chat
* Auto /go
* Auto /pledge
* Simulation of human wait time
* Disable auto actions if human had already done it (report, foray, pledge)

### Bugs
* Rare occurrence whereby target castle emoji is sent but game doesn't register it

### Planned
* Night mode (longer simulated human time at night)
* Toggle to turn on/off certain features
* Auto forwarding of quest results to castle bot
* Auto drinking of vpb rage/peace (based on orders)
* Auto arena (fast fight)
* Auto daily craft (educated technician exp)
* Possible guild wars support (/report, /g_atk, /g_def)