from jepthon import *
from jepthon import jepiq
from ..sql_helper.globals import gvarstatus

@jepiq.on(admin_cmd(pattern="(وێنەکە بهێنە|وێنەکە بهێنە|خودی|خودی|پاراستن)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    lMl10l = await event.get_reply_message()
    pic = await lMl10l.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- وێـنـەکـە بەسەرکەوتوویی هەڵگیرا ✓ 
- بێ ڕەوشت داواکاریەکە بەکاربێنە بۆ ڕەشە کوژان
- CH: @xv7amo
- Dev: @IQ7amo
  """,
    )
    await event.delete()
