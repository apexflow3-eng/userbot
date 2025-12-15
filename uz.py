# -*- coding: utf-8 -*-

import io
import qrcode

class QRModule:
    async def qrcmd(self, message):
        """Link yoki matndan QR code yaratadi"""

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
            return await message.edit(
                "❌ QR uchun matn yo‘q\n"
                "Reply + .qr yoki `.qr matn/link`"
            )

        await message.edit("🔲 QR code yaratilmoqda...")

        # QR yaratish
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        bio = io.BytesIO()
        bio.name = "qr.png"
        img.save(bio, "PNG")
        bio.seek(0)

        await message.delete()
        await message.client.send_file(
            message.chat_id,
            bio,
            caption=f"🔗 QR code\n\n<code>{text}</code>",
            parse_mode="html"
        )
