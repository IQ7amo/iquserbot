"""QuotLy: Avaible commands: .گۆڕین
"""
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from jepthon.utils import admin_cmd

@borg.on(admin_cmd(pattern="گۆڕینی دەق ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("᯽︙ پێویستە. وەڵامدانەوەی نامەی بەکارهێنەر )")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("᯽︙ پێویستە. وەڵامدانەوەی نامەی بەکارهێنەر )")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("᯽︙ پێویستە. وەڵامدانەوەی نامەی بەکارهێنەر )")
       return
    await event.edit("᯽︙ گۆڕینی دەق بۆ ستیکەر ..🕷️🖤")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```بلۆکم لابەرە گەمژە (@QuotLyBot)```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("᯽︙ تایبەتمەندی ڕێنماییەکە دەبێت یەکەم جار هەڵوەشێتەوە 🕷️")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
             
# Copyright (C) 2021 JepThon TEAM
# FILES WRITTEN BY  @lMl10l
