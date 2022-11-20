# WRITED BY - @VUUZZ - @lMl10l

import io
import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument

from jepthon import jepiq

from ..core.managers import edit_or_reply
from ..helpers.functions import deEmojify, hide_inlinebot, waifutxt
from ..helpers.utils import reply_id

plugin_category = "fun"


async def get_font_file(client, channel_id, search_kw=""):
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        limit=None,
        search=search_kw,
    )
    font_file_message = random.choice(font_file_message_s)
    return await client.download_media(font_file_message)


@jepiq.ar_cmd(
    pattern="دەق(?:\s|$)([\s\S]*)",
    command=("دەق", plugin_category),
    info={
        "فەرمان": "ئەمە بابەتێکی سەرگەرمییە، خۆت تاقی بکەرەوە.",
        "بەکارهێنان": "{tr}sttxt <text>",
        "نموونەکان": "{tr}sttxt سڵاو",
    },
)
async def waifu(animu):
    " ⌔︙ئەو ئەنیمێیەی کە نووسینەکەت خۆش دەکات"
    text = animu.pattern_match.group(1)
    reply_to_id = await reply_id(animu)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            return await edit_or_reply(
                animu, "` ⌔︙تۆ هیچ دەقێکت نەنووسیوە، وایڤۆ جێدەهێڵێ.`"
            )
    text = deEmojify(text)
    await animu.delete()
    await waifutxt(text, animu.chat_id, reply_to_id, animu.client)


# 12 21 28 30
@jepiq.ar_cmd(
    pattern="ستیکەر ?(?:(.*?) ?; )?([\s\S]*)",
    command=("ستیکەر", plugin_category),
    info={
        "سەری پەڕە": "دەقەکەت وەکو ستیکەر.",
        "بەکارهێنان": [
            "{tr}ستیکەر <دەق>",
            "{tr}ستیکەر <ناوی فایلی فۆنت> ; <دەق>",
        ],
        "نموونەکان": "{tr}ستیکەر سڵاو",
    },
) # WRITED BY - @VTVIT - @IQ7amo
async def sticklet(event):
    " ⌔︙ دەقەکەت وەکو ستیکەر"
    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    reply_to_id = await reply_id(event)
    font_file_name = event.pattern_match.group(1)
    if not font_file_name:
        font_file_name = ""
    sticktext = event.pattern_match.group(2)
    reply_message = await event.get_reply_message()
    if not sticktext:
        if event.reply_to_msg_id:
            sticktext = reply_message.message
        else:
            return await edit_or_reply(event, " ⌔︙پێویستت بە شتێکە، هممم")
    await event.delete()
    sticktext = deEmojify(sticktext)
    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = "\n".join(sticktext)
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    FONT_FILE = await get_font_file(event.client, "@catfonts", font_file_name)
    font = ImageFont.truetype(FONT_FILE, size=fontsize)
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B)
    )
    image_stream = io.BytesIO()
    image_stream.name = "IQBot.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)
    # finally, reply the sticker
    await event.client.send_file(
        event.chat_id,
        image_stream,
        caption="ستیکەری پشیلە",
        reply_to=reply_to_id,
    )
    try:
        os.remove(FONT_FILE)
    except BaseException:
        pass

# WRITED BY - @VTVIT - @IQ7amo
@jepiq.ar_cmd(
    pattern="هۆنک(?:\s|$)([\s\S]*)",
    command=("هۆنک", plugin_category),
    info={
        "فەرمان": "هۆنک بە هەر شتێك بڵێ",
        "بەکارهێنان": "{tr}هۆنك <دەق/وەڵامدانەوەی نامەکە>",
        "نموونەکان": "{tr}هۆنك چۆن دەیکەیت?",
    },
)
async def honk(event):
    " ᯽︙ وای لێ بکە هۆنك هەر شتێک بڵێت."
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@honka_says_bot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "** ᯽︙ چی دەبێت بڵێت هۆنك دەقێکی پێ بدە🕷️🖤.**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@jepiq.ar_cmd(
    pattern="توییت(?:\s|$)([\s\S]*)",
    command=("توییت", plugin_category),
    info={
        "فەرمان": "توییتێکی جوان لە ئەکاونتەکەت دروست بکە",
        "بەکارھێنان": "{tr}توییت <دەق/بە وەڵامدانەوەی چات>",
        "نموونەکان": "{tr}توییت IQ_userbot",
    },
)
async def twt(event):
    " ⌔︙ توییتێکی گەورە لە ئەکاونتەکەت دروست بکە."
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@TwitterStatusBot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "**᯽︙  دەبێت چی لە تویتەرێکدا بنووسم🕷️🖤.**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@jepiq.ar_cmd(
    pattern="میم(?:\s|$)([\s\S]*)",
    command=("میم", plugin_category),
    info={
        "فەرمان": "بۆ وتنی هەر شتێك.",
        "بەکارهێنان": "{tr}میم بە وەڵامدانەوەی چات>",
        "نموونەکان": "{tr}میم پارەم پێ بدە",
    },
) # WRITED BY - @VTVIT - @IQ7amo
async def doge(event):
    " ⌔︙دروستکردنی میمی سەگ"
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@DogeStickerBot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "᯽︙ سەگەکە چی دەبێ بڵێت دەقێکی پێ ببەخشە🕷️🖤.**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)
# WRITED BY - @VUUZZ - @lMl10l

@jepiq.ar_cmd(
    pattern="گلاکس(|ر)(?:\s|$)([\s\S]*)",
    command=("گلاکس", plugin_category),
    info={
        "فەرمان": " هاوار کردنی دەقەکەت وەکو ئەژدیھا.",
        "ئاڵا": {
            "r": "پێچەوانە کردنی دەموچاوی ئەژدیھا",
        },
        "بەکارهێنان": [
            "{tr}گلاکس <دەق/بە وەڵامدانەوەی چات>",
            "{tr}گلاکس ر <دەق/بە وەڵامدانەوەی چات>",
        ],
        "examples": [
            "{tr}گلاکس بمرە",
            "{tr}گلاکس ر بمرە",
        ],
    },
) # WRITED BY - @VTVIT - @IQ7amo
async def glax(event):
    " ⌔︙وا لە ئەژدیھا بکە دەقەکەت بتەقێنێتەوە🕷️🖤."
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    bot_name = "@GlaxScremBot"
    c_lick = 1 if cmd == "ڕ" else 0
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, " ᯽︙ گلاکس چی دەبێت بڵێت دەقێکی پێ ببەخشە🕷️🖤.**"
            ) # WRITED BY - @VTVIT - @IQ7amo
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(
        event.client, bot_name, text, event.chat_id, reply_to_id, c_lick=c_lick
    )
    # WRITED BY - @VTVIT - @IQ7amo
