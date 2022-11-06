import json
import os
import re

from telethon.events import CallbackQuery

from jepthon import jepiq


@jepiq.tgbot.on(CallbackQuery(data=re.compile(b"rzan_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./jepthon/secrets.txt"):
        jsondata = json.load(open("./jepthon/secrets.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, jepiq.uid]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "⌯︙ ببوورە، ئەم لیستە بۆ تۆ مەبەست نییە🕷️.  "
        except KeyError:
            reply_pop_up_alert = "⌯︙ ببوورە، ئەم لیستە چی تر لە سێرڤەرەکانی بۆتی زیرەك بوونی نیی🕷️. "
    else:
        reply_pop_up_alert = "⌯︙ببوورە، ئەم لیستە چیتر بوونی نییە🕷️.  "
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
