# -*- coding: utf-8 -*-

import io
from PIL import Image
import pytesseract


class OCRModule:
    """Rasm ichidagi matnni o‘qish (OCR)"""

    async def orccmd(self, message):
        """Rasmga reply qilib matnni o‘qib beradi"""

        if not message.is_reply:
            return await message.edit("❌ Rasmga reply qilib `.ocr` yoz")

        reply = await message.get_reply_message()

        if not reply.photo:
            return await message.edit("❌ Reply qilingan xabar rasm emas")

        await message.edit("🖼 OCR qilinmoqda...")

        img_bytes = io.BytesIO()
        await reply.download_media(file=img_bytes)
        img_bytes.seek(0)

        try:
            image = Image.open(img_bytes)
            text = pytesseract.image_to_string(image, lang="eng+rus")

            if not text.strip():
                return await message.edit("❌ Matn topilmadi")

            if len(text) > 4000:
                text = text[:4000] + "..."

            await message.edit(
                "📝 <b>OCR natija:</b>\n\n"
                f"<code>{text}</code>",
                parse_mode="html"
            )

        except Exception as e:
            await message.edit(f"❌ Xatolik: <code>{e}</code>", parse_mode="html")
