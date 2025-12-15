# -*- coding: utf-8 -*-

import io
from gtts import gTTS

class TTSModule:
    """Matn → Ovoz (Text to Speech)"""

    async def ttscmd(self, message):
        """Matnni ovozli xabarga aylantiradi"""

        text = None

        if message.is_reply:
            reply = await message.get_reply_message()
            if reply and reply.text:
                text = reply.text
        else:
            parts = message.text.split(maxsplit=1)
            if len(parts) > 1:
                text = parts[1]

        if not text:
            return await message.edit("❌ `.tts matn` yoki reply matn")

        await message.edit("🔊 Ovoz yaratilmoqda...")

        try:
            tts = gTTS(text=text, lang="uz")
            audio = io.BytesIO()
            tts.write_to_fp(audio)
            audio.seek(0)
            audio.name = "tts.ogg"

            await message.delete()
            await message.client.send_file(
                message.chat_id,
                audio,
                voice_note=True
            )

        except Exception as e:
            await message.edit(f"❌ Xatolik: `{e}`")
