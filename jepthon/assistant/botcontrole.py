import asyncio
from datetime import datetime

from telethon.errors import BadRequestError, FloodWaitError, ForbiddenError

from jepthon import jepiq

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import reply_id, time_formatter
from ..helpers.utils import _format
from ..sql_helper.bot_blacklists import check_is_black_list, get_all_bl_users
from ..sql_helper.bot_starters import del_starter_from_db, get_all_starters
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID
from .botmanagers import (
    ban_user_from_bot,
    get_user_and_reason,
    progress_str,
    unban_user_from_bot,
)

LOGS = logging.getLogger(__name__)

plugin_category = "bot"
botusername = Config.TG_BOT_USERNAME
cmhd = Config.COMMAND_HAND_LER





@jepiq.bot_cmd(
    pattern="^/broadcast$",
    from_users=Config.OWNER_ID,
)
async def bot_broadcast(event):
    replied = await event.get_reply_message()
    if not replied:
        return await event.reply("وەڵامی نامەکە بدەوە بۆ ڕادیۆ !")
    start_ = datetime.now()
    br_cast = await replied.reply("بۆ هەمووان پەخش دەکرێت...")
    blocked_users = []
    count = 0
    bot_users_count = len(get_all_starters())
    if bot_users_count == 0:
        return await event.reply("هیچ کەسێك بۆتت بەکارناهێنێت")
    users = get_all_starters()
    if users is None:
        return await event.reply("**هەڵەیەك هەیە لەکاتی پشکنینی لیستی بەکارهێنەران**")
    for user in users:
        try:
            await event.client.send_message(
                int(user.user_id), "🔊 ڕادیۆیەکی نوێ وەرگیرا."
            )
            await event.client.send_message(int(user.user_id), replied)
            await asyncio.sleep(0.8)
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
        except (BadRequestError, ValueError, ForbiddenError):
            del_starter_from_db(int(user.user_id))
        except Exception as e:
            LOGS.error(str(e))
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID, f"** هەڵە هەیە لە ڕادیۆ **\n`{str(e)}`"
                )
        else:
            count += 1
            if count % 5 == 0:
                try:
                    prog_ = (
                        "🔊 ڕادیۆی گشتی...\n\n"
                        + progress_str(
                            total=bot_users_count,
                            current=count + len(blocked_users),
                        )
                        + f"\n\n• ✔️🕷️ **سەرکەوتووبوو* :  `{count}`\n"
                        + f"• ✖️ **هەڵەیە** :  `{len(blocked_users)}`"
                    )
                    await br_cast.edit(prog_)
                except FloodWaitError as e:
                    await asyncio.sleep(e.seconds)
    end_ = datetime.now()
    b_info = f"🔊 بە سەرکەوتوویی ڕادیۆ بۆ ➜  <b>{count} لە بەکارهێنەرانەوە.</b>"
    if len(blocked_users) != 0:
        b_info += f"\n🚫  <b>{len(blocked_users)} لە بەکارهێنەرانەوە</b> ئەگەر نامەکە سڕایەوە ئەوا ئەو بۆتی تۆی بلۆککرد."
    b_info += (
        f"\n⏳  <code> پڕۆسەکە ئەنجامدرا: {time_formatter((end_ - start_).seconds)}</code>."
    )
    await br_cast.edit(b_info, parse_mode="html")


@jepiq.bot_cmd(
    pattern="users$",
    command=("users", plugin_category),
    info={
        "سەری پەڕە": "بۆ بەدەستھێنانی بەکارهێنەرانی بۆت",
        "وەسف": "بۆ بینینی لیستی ئەو بەکارهێنەرانەی کە بۆتەکەتیان چالاککردووە",
        "بەکارهێنان": "{tr}بەکارهێنەرەکان",
    },
)
async def ban_starters(event):
    "بۆ بەدەستھێنانی بەکارهێنەرانی بۆت."
    ulist = get_all_starters()
    if len(ulist) == 0:
        return await edit_delete(event, "** کەس بۆتەکەتیان بەکارنەھێنا.**")
    msg = "**لیستی بەکارهێنەرانی بۆت :\n\n**"
    for user in ulist:
        msg += f"•  👤 {_format.mentionuser(user.first_name , user.user_id)}\n**ناسنامە:** `{user.user_id}`\n**ناوی بەکارهێنەر:** @{user.username}\n**بەروار: **__{user.date}__\n\n"
    await edit_or_reply(event, msg)


@jepiq.bot_cmd(
    pattern="^/block\s+([\s\S]*)",
    from_users=Config.OWNER_ID,
)
async def ban_botpms(event):
    user_id, reason = await get_user_and_reason(event)
    reply_to = await reply_id(event)
    if not user_id:
        return await event.client.send_message(
            event.chat_id, "لا يمكنني العثور على المستخدم", reply_to=reply_to
        )
    if not reason:
        return await event.client.send_message(
            event.chat_id, "لحظر شخص اكتب السبب اولا", reply_to=reply_to
        )
    try:
        user = await event.client.get_entity(user_id)
        user_id = user.id
    except Exception as e:
        return await event.reply(f"**هەڵەیە:**\n`{str(e)}`")
    if user_id == Config.OWNER_ID:
        return await event.reply("ناتوانم خاوەنی بۆت بلۆك بکەم🕷️.")
    check = check_is_black_list(user.id)
    if check:
        return await event.client.send_message(
            event.chat_id,
            f"#پێشتر_قەدەغەکراوە\
            \nئەم بەکارهێنەرە لە لیستی کەسە بلۆککراوەکاندایە\
            \n**هۆکاری قەدەغەکردنت\باند:** `{check.reason}`\
            \n**بەروار:** `{check.date}`.",
        )
    msg = await ban_user_from_bot(user, reason, reply_to)
    await event.reply(msg)


@jepiq.ar_cmd(
    pattern="^/unblock(?:\s|$)([\s\S]*)",
    from_users=Config.OWNER_ID,
)
async def ban_botpms(event):
    user_id, reason = await get_user_and_reason(event)
    reply_to = await reply_id(event)
    if not user_id:
        return await event.client.send_message(
            event.chat_id, "** لا استطيع ايجاد المستخـدم للحـظر**", reply_to=reply_to
        )
    try:
        user = await event.client.get_entity(user_id)
        user_id = user.id
    except Exception as e:
        return await event.reply(f"**خـطأ:**\n`{str(e)}`")
    check = check_is_black_list(user.id)
    if not check:
        return await event.client.send_message(
            event.chat_id,
            f"#الغاء البلوك من الشخصي \
            \n👤 {_format.mentionuser(user.first_name , user.id)} تم الغاء حظره من البوت بنجاح.",
        )
    msg = await unban_user_from_bot(user, reason, reply_to)
    await event.reply(msg)


@jepiq.bot_cmd(
    pattern="المحظورين$",
    command=("المحظورين", plugin_category),
    info={
        "header": "لـعـرض قـائمـة الـمستخـدمين الـمحظوريـن فـي بـوتك.",
        "الـشـرح": "لعـرض قـائمـة الـمستخـدمين الـمحظوريـن فـي بـوتك",
        "الاستـخـدام": "{tr}المحظورين",
    },
)
async def ban_starters(event):
    "لـعـرض قـائمـة الـمستخـدمين الـمحظوريـن فـي بـوتك"
    ulist = get_all_bl_users()
    if len(ulist) == 0:
        return await edit_delete(event, "** لا يوجـد شخص محـظور في البـوت الـى الان**")
    msg = "**المسـتخدميـن المحـظورين في بـوتك هـم :\n\n**"
    for user in ulist:
        msg += f"• 👤 {_format.mentionuser(user.first_name , user.chat_id)}\n**الايدي:** `{user.chat_id}`\n**المعرف:** @{user.username}\n**التاريخ: **{user.date}\n**السبب:** {user.reason}\n\n"
    await edit_or_reply(event, msg)


@jepiq.bot_cmd(
    pattern="دۆخی_دووبارەکردنەوە(چالاککردن|ناچالاککردن)$",
    command=("دۆخی_دووبارەکردنەوە", plugin_category),
    info={
        "header": "بۆ چالاککردن و نا چالاککردنی دووبارە کردنەوە لە بۆتەکەت",
        "ڕوونکردنەوە": "🕷️ئەگەر بەکارهێنەرەکە 10 نامە دووبارە بکاتەوە یان چاکی بکاتەوە، بۆتەکە بلۆکی دەکات",
        "بەکارهێنان": [
            "{tr}دۆخی_دووبارەکردنەوە چالاکە",
            "{tr}دۆخی_دووبارەکردنەوە ناچالاکە",
        ],
    },
)
async def ban_antiflood(event):
    "بۆ چالاککردن و نا چالاککردنی دووبارەکردنەوە لە بۆتەکەت."
    input_str = event.pattern_match.group(1)
    if input_str == "چالاککردن":
        if gvarstatus("bot_antif") is not None:
            return await edit_delete(event, "`دژە فلۆدی بۆت پێشتر چالاککراوە`")
        addgvar("bot_antif", True)
        await edit_delete(event, "`دژە فلۆدی بۆت چالاککراوە`")
    elif input_str == "نا چالاککردن":
        if gvarstatus("bot_antif") is None:
            return await edit_delete(event, "`دژە فلۆدی بۆت پێشتر لە کارخراوە.`")
        delgvar("bot_antif")
        await edit_delete(event, "` دژە فلۆدی بۆت لە کارخراوە.`")
