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

# Chat target name variables
tarGame_name = config['target']['targetGame_name']
tarOrder_name = config['target']['targetOrder_name']
tarCastleBot_name = config['target']['targetCastleBot_name']

# Program settings variables