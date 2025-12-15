# -*- coding: utf-8 -*-

import io
import pytesseract
from PIL import Image

class OCRModule:
    async def ocrcmd(self, message):
        """Rasmdan matnni o‘qib beradi (reply image)"""

        if not message.is_reply:
            return await message.edit("❌ Rasmga reply qilib `.ocr` yoz")

        reply = await message.get_reply_message()
        if not reply.photo:
            return await message.edit("❌ Reply qilingan xabar rasm emas")

        await message.edit("🖼 OCR qilinmoqda...")

        img_bytes = io.BytesIO()
        await reply.download_media(file=img_bytes)
        img_bytes.seek(0)

        img = Image.open(img_bytes)
        text = pytesseract.image_to_string(img, lang="eng+rus")

        if not text.strip():
            return await message.edit("❌ Matn topilmadi")

        if len(text) > 4000:
            text = text[:4000] + "..."

        await message.edit(f"📝 **OCR natija:**\n\n<code>{text}</code>", parse_mode="html")
