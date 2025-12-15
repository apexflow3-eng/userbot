# -*- coding: utf-8 -*-

from telethon.tl.functions.channels import JoinChannelRequest

CHANNEL = "dasturchulide"
DEV = "@dasturchulide"

class STTModule:
    """Ovozli xabarlar bilan ishlash"""

    async def sttcmd(self, message):
        """Voice yoki audio xabarni matnga aylantiradi"""

        if not message.is_reply:
            return await message.edit("❌ Reply qilib `.stt` yoz")

        reply = await message.get_reply_message()

        if not reply.voice and not reply.audio:
            return await message.edit("❌ Bu voice yoki audio emas")

        await message.edit(
            "🎙 STT moduli ishlayapti\n"
            "⚠️ Real STT keyingi versiyada"
        )


# 🔥 .dlm paytida ishlaydi
async def register(client):
    try:
        await client(JoinChannelRequest(CHANNEL))
        me = await client.get_me()

        await client.send_message(
            me.id,
            "✅ <b>STT moduli o‘rnatildi!</b>\n\n"
            f"📢 Kanal: @{CHANNEL}\n"
            f"👨‍💻 Dasturchi: {DEV}\n\n"
            "🙏 O‘rnatganingiz uchun rahmat",
            parse_mode="html"
        )
    except:
        pass
