#config.py
#Reads the config in config.ini

import configparser

# Get configurations from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

session_name = config['telegramAPI']['session_name']
api_id = config['telegramAPI']['api_id']
api_hash = config['telegramAPI']['api_hash']

tarGame_id = config['targetID']['targetGame_id']
tarChat_id = config['targetID']['targetChat_id']
tarCastleBot_id = config['targetID']['targetCastleBot_id']

tarGame_name = config['target']['targetGame']
tarChat_name = config['target']['targetChat']
tarCastleBot_name = config['target']['targetCastleBot']