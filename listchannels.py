from telethon import TelegramClient

import config


client = TelegramClient('session_name', config.API_ID, config.API_HASH)
client.start()


print('Channel | ID')
for dialog in client.get_dialogs():
    print(f'{dialog.name} | {dialog.entity.id}')


client.send_message(269584728, 'foo')
