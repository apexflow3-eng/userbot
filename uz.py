# -*- coding: utf-8 -*-

class Userbot:
    """
    .uz <text>
    Reply + .uz
    Avtomatik O‘zbekchaga tarjima
    """

    def __init__(self, client):
        self.client = client

    async def uzcmd(self, message):  # ⚠️ MUHIM: uzcmd
        try:
            from googletrans import Translator

            translator = Translator()

            args = message.text.split(maxsplit=1)
            reply = await message.get_reply_message()

            if reply and reply.text:
                text = reply.text
            elif len(args) > 1:
                text = args[1]
            else:
                return await message.edit(
                    "❌ Tarjima uchun matn yo‘q\nReply + .uz yoki .uz matn"
                )

            await message.edit("🇺🇿 Tarjima qilinmoqda...")

            result = translator.translate(text, src="auto", dest="uz")

            await message.edit(
                f"🇺🇿 O‘zbekcha tarjima:\n\n{result.text}"
            )

        except Exception as e:
            await message.edit(f"❌ Xatolik: {e}")
