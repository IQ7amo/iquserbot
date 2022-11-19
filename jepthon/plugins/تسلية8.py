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
        "examples": "{tr}ستیکەر سڵاو",
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
    pattern="هونك(?:\s|$)([\s\S]*)",
    command=("هونك", plugin_category),
    info={
        "header": "Make honk say anything.",
        "usage": "{tr}honk <text/reply to msg>",
        "examples": "{tr}honk How you doing?",
    },
)
async def honk(event):
    " ᯽︙ اجعل هونك يقول اي شيء."
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@honka_says_bot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "** ᯽︙ ماذا يفترض أن يقول هونك أعطه نص**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@jepiq.ar_cmd(
    pattern="تغريد(?:\s|$)([\s\S]*)",
    command=("تغريد", plugin_category),
    info={
        "header": "Make a cool tweet of your account",
        "usage": "{tr}twt <text/reply to msg>",
        "examples": "{tr}twt Catuserbot",
    },
)
async def twt(event):
    " ⌔︙قم بعمل تغريدة رائعة من حسابك."
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@TwitterStatusBot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "**᯽︙ ماذا يفترض بي ان اغرد اكتي نصا**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@jepiq.ar_cmd(
    pattern="دوغي(?:\s|$)([\s\S]*)",
    command=("دوغي", plugin_category),
    info={
        "header": "Make doge say anything.",
        "usage": "{tr}doge <text/reply to msg>",
        "examples": "{tr}doge Gib money",
    },
) # WRITED BY - @VUUZZ - @lMl10l
async def doge(event):
    " ⌔︙اصنع ستيكر كلب رائع."
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@DogeStickerBot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "᯽︙ ماذا يفترض بالكلب ان يقول اعطه نصا**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)
# WRITED BY - @VUUZZ - @lMl10l

@jepiq.ar_cmd(
    pattern="غلاكس(|ر)(?:\s|$)([\s\S]*)",
    command=("غلاكس", plugin_category),
    info={
        "header": "Make glax the dragon scream your text.",
        "flags": {
            "r": "Reverse the face of the dragon",
        },
        "usage": [
            "{tr}glax <text/reply to msg>",
            "{tr}glaxr <text/reply to msg>",
        ],
        "examples": [
            "{tr}glax Die you",
            "{tr}glaxr Die you",
        ],
    },
) # WRITED BY - @VUUZZ - @lMl10l
async def glax(event):
    " ⌔︙اجعل غلاكس التنين ينفخ نصك."
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    bot_name = "@GlaxScremBot"
    c_lick = 1 if cmd == "ر" else 0
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, " ᯽︙ ماذا يفترض بـ گلاكـس ان يقول اعطه نصا**"
            ) # WRITED BY - @VUUZZ - @lMl10l
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(
        event.client, bot_name, text, event.chat_id, reply_to_id, c_lick=c_lick
    )
    # WRITED BY - @VUUZZ - @lMl10l
