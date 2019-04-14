#config.py
#Reads the config in config.ini

import configparser

# Get configurations from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Telegram API variables
session_name = config['telegramAPI']['session_name']
api_id = config['telegramAPI']['api_id']
api_hash = config['telegramAPI']['api_hash']

# Chat target ID variables
tarGame_id = config['targetID']['targetGame_id']
tarOrder_id = config['targetID']['targetOrder_id']
tarCastleBot_id = config['targetID']['targetCastleBot_id']
tarAdmin_id = config['targetID']['targetAdmin_id']

# Chat target name variables
tarGame_name = config['target']['targetGame_name']
tarOrder_name = config['target']['targetOrder_name']
tarCastleBot_name = config['target']['targetCastleBot_name']
tarAdmin_name = config['target']['targetAdmin_name']

# Program settings variables
master_status = config['settings']['master_status']
status_go = config['settings']['status_go']
status_pledge = config['settings']['status_pledge']
status_def = config['settings']['status_def']
status_tact = config['settings']['status_tact']
status_tactTarget = config['settings']['status_tactTarget']
status_report = config['settings']['status_report']
status_report_sentcheck = config['settings']['status_report_sentcheck']
status_report_location = config['settings']['status_report_location']