#!/usr/bin/env python
from telethon import TelegramClient, events

import logging

import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)
client.start()

client.get_dialogs()
client.get_me()


RELAY_MAP = {
    1368436776: [   # Trobidia
        269584728,  # Relay
    ]
}


@client.on(events.NewMessage)
async def my_event_handler(event):
    for chat_id, relays in RELAY_MAP.items():
        if chat_id == event.chat.id:
            for relay in relays:
                logger.info(f'Sending message from {event.chat.id} to {relay}')
                await client.send_message(relay, event.message)
            break
    else:
        for relay in RELAY_MAP.get('default', []):
            logger.info(f'Sending message from {event.chat.id} default {relay}')
            await client.send_message(relay, event.message)

client.run_until_disconnected()
