# -*- coding: utf-8 -*-

class Userbot:
    """
    .uz <text>
    (test modul – loader ishlashini tekshiradi)
    """

    def __init__(self, client):
        self.client = client

    async def uzcmd(self, message):
        text = message.text.split(maxsplit=1)
        if len(text) < 2:
            return await message.edit("🇺🇿 Test ishladi")

        await message.edit(f"🇺🇿 Test matn:\n\n{text[1]}")
