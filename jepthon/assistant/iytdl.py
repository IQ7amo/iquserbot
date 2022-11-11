import os
import re

try:
    from PIL import Image
except ImportError:
    Image = None
from telethon import Button
from telethon.errors.rpcerrorlist import FilePartLengthInvalidError, MediaEmptyError
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo
from telethon.tl.types import InputWebDocument as wb
from youtubesearchpython import VideosSearch
from . import LOGS
from jepthon import jepiq



ytt = "https://graph.org/file/afd04510c13914a06dd03.jpg"
_yt_base_url = "https://www.youtube.com/watch?v="
BACK_BUTTON = {}
plugin_category = "bot"

@jepiq.ar_cmd(
    pattern="گۆرانی(?:\s|$)([\s\S]*)",
    command=("گۆرانی", plugin_category),
    info={
        "header": "ytdl with inline buttons.",
        "description": "To search and download youtube videos by inline buttons.",
        "usage": "{tr}iytdl [URL / Text] or [Reply to URL / Text]",
    },
)
async def _(event):
    try:
        joker = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        fuk = event.builder.article(
            title="گەڕان لە شتێکدا.",
            thumb=wb(ytt, 0, "image/jpeg", []),
            text="**YᴏᴜTᴜʙᴇ Sᴇᴀʀᴄʜ**\n\nتۆ گەڕانت بۆ هیچ شتێك ئەنجام نەداوە.",
            buttons=Button.switch_inline(
                "دووبارە گەڕان ئەنجام بدە.",
                query="yt ",
                same_peer=True,
            ),
        )
        await event.answer([fuk])
        return
    results = []
    search = VideosSearch(joker, limit=50)
    nub = search.result()
    nibba = nub["result"]
    for v in nibba:
        ids = v["id"]
        link = _yt_base_url + ids
        title = v["title"]
        duration = v["duration"]
        views = v["viewCount"]["short"]
        publisher = v["channel"]["name"]
        published_on = v["publishedTime"]
        description = (
            v["descriptionSnippet"][0]["text"]
            if v.get("descriptionSnippet")
            and len(v["descriptionSnippet"][0]["text"]) < 500
            else "None"
        )
        thumb = f"https://i.ytimg.com/vi/{ids}/hqdefault.jpg"
        text = f"**ناونیشان🕷️: [{title}]({link})**\n\n"
        text += f"`Description: {description}\n\n"
        text += f"「 ماوە🕷️: {duration} 」\n"
        text += f"「 بینینەکان🕷️: {views} 」\n"
        text += f"「 بڵاوکەرەوە🕷️: {publisher} 」\n"
        text += f"「 بڵاوکراوەتەوە لە🕷️: {published_on} 」`"
        desc = f"{title}\n{duration}"
        file = wb(thumb, 0, "image/jpeg", [])
        buttons = [
            [
                Button.inline("دەنگ", data=f"ytdl:audio:{ids}"),
                Button.inline("ڤیدیۆ", data=f"ytdl:video:{ids}"),
            ],
            [
                Button.switch_inline(
                    "دووبارە گەڕان ئەنجام بدە.",
                    query="yt ",
                    same_peer=True,
                ),
                Button.switch_inline(
                    "هاوبەشکردن",
                    query=f"yt {string}",
                    same_peer=False,
                ),
            ],
        ]
        BACK_BUTTON.update({ids: {"text": text, "buttons": buttons}})
        results.append(
            await event.builder.article(
                type="photo",
                title=title,
                description=desc,
                thumb=file,
                content=file,
                text=text,
                include_media=True,
                buttons=buttons,
            ),
        )
    await event.answer(results[:50])
