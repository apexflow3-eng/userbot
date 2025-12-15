# -*- coding: utf-8 -*-

from googletrans import Translator

class Userbot:
    """
    .uz <text>
    Reply + .uz
    Qaysi tilda bo‘lsa ham avtomatik aniqlab O‘zbek tiliga tarjima qiladi
    """

    def __init__(self, client):
        self.client = client
        self.translator = Translator()

    async def uz(self, message):
        try:
            args = message.text.split(maxsplit=1)
            reply = await message.get_reply_message()

            if reply and reply.text:
                text = reply.text
            elif len(args) > 1:
                text = args[1]
            else:
                return await message.edit(
                    "❌ <b>Tarjima uchun matn yo‘q.</b>\n"
                    "<code>Reply + .uz</code> yoki <code>.uz matn</code>",
                    parse_mode="html"
                )

            await message.edit("🇺🇿 <b>Tarjima qilinmoqda...</b>", parse_mode="html")

            result = self.translator.translate(text, src="auto", dest="uz")

            out = (
                "🇺🇿 <b>O‘zbekcha tarjima</b>\n\n"
                f"🌐 <b>Aniqlangan til:</b> {result.src}\n\n"
                f"📝 <b>Matn:</b>\n<code>{result.text}</code>"
            )

            await message.edit(out, parse_mode="html")

        except Exception as e:
            await message.edit(
                f"❌ <b>Xatolik:</b> <code>{e}</code>",
                parse_mode="html"
            )
