# -*- coding: utf-8 -*-

import time

class Userbot:
    """
    .ping
    Userbot ishlayaptimi tekshiradi
    """

    def __init__(self, client):
        self.client = client

    async def ping(self, message):
        start = time.time()
        await message.edit("🏓 Ping...")
        end = time.time()

        ms = int((end - start) * 1000)

        await message.edit(f"🏓 <b>Pong!</b>\n⏱ <b>{ms} ms</b>", parse_mode="html")
