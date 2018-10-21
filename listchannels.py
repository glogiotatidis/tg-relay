#!/usr/bin/env python
import telethon.sync
from telethon import TelegramClient


import config


client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)
client.start()


print('Channel | ID')
for dialog in client.get_dialogs():
    print(f'{dialog.name} | {dialog.entity.id}')
