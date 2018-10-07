#!/usr/bin/env python
import asyncio
import logging

from telethon import TelegramClient, events

import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)
client.start()

RELAY_MAP = {}


async def setup():
    user = await client.get_me()
    logger.info(f'Started serving as {user.first_name}')
    await client.get_dialogs()

    for x in config.RELAY_MAP.split(';'):
        if not x:
            return

        key, values = x.split(':', 1)
        values = values.split(',')
        RELAY_MAP[int(key)] = [int(x) for x in values]


@client.on(events.NewMessage)
async def my_event_handler(event):
    for chat_id, relays in RELAY_MAP.items():
        if chat_id == event.chat.id:
            for relay in relays:
                logger.info(f'Sending message from {event.chat.id} to {relay}')
                if config.FORWARD:
                    await client.forward_messages(relay, event.message)
                else:
                    await client.send_message(relay, event.message)
            break
    else:
        for relay in RELAY_MAP.get('default', []):
            logger.info(f'Sending message from {event.chat.id} default {relay}')
            if config.FORWARD:
                await client.forward_messages(relay, event.message)
            else:
                await client.send_message(relay, event.message)

loop = asyncio.get_event_loop()
loop.run_until_complete(setup())
client.run_until_disconnected()
