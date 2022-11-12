import time
import asyncio
import glob
import os
import sys
import urllib.request
from datetime import timedelta
from pathlib import Path
import requests
from telethon import Button, functions, types, utils
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError
from jepthon import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from ..Config import Config
from ..core.logger import logging
from ..core.session import jepiq
from ..helpers.utils import install_pip
from ..helpers.utils.utils import runcmd
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
LOGS = logging.getLogger("IQBot")

cmdhr = Config.COMMAND_HAND_LER
bot = jepiq
ENV = bool(os.environ.get("ENV", False))

if ENV:
    VPS_NOLOAD = ["سێرڤەر"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["هێرۆکۆ"]

async def setup_bot():
    """
    To set up bot for jepthon
    """
    try:
        await jepiq.connect()
        config = await jepiq(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == jepiq.session.server_address:
                if jepiq.session.dc_id != option.id:
                    LOGS.warning(
                        f"⌯︙پێناسێکی لەدانیشتنی {jepiq.session.dc_id}"
                        f"⌯︙لـ  {option.id}"
                    )
                jepiq.session.set_dc(option.id, option.ip_address, option.port)
                jepiq.session.save()
                break
        bot_details = await jepiq.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        # await jepiq.start(bot_token=Config.TG_BOT_USERNAME)
        jepiq.me = await jepiq.get_me()
        jepiq.uid = jepiq.tgbot.uid = utils.get_peer_id(jepiq.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(jepiq.me)
    except Exception as e:
        LOGS.error(f"کۆد تێرمۆکس - {str(e)}")
        sys.exit()


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.CATUBLOGO = await jepiq.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/6b96d5ea58d065005ec9c.jpg",
                caption="**᯽︙ بـۆتـی زیـرەك کـاردەکـات🕷️✓ **\n**᯽︙ بنێرە`.فەرمانەکان`بۆ بینینی فەرمانەکانی سەرچاوەکە**",
                buttons=[(Button.url("سەرچاوەی بۆتی زیرەك", "https://t.me/JepthonSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await jepiq.check_testcases()
            message = await jepiq.get_messages(msg_details[0], ids=msg_details[1])
            text = (
                message.text
                + "\n\n**᯽: بەخێربێیت، تۆ بە سەرکەوتوویی بۆتی زیرەكت دەستپێکردەوە**"
            )
            
            if gvarstatus("restartupdate") is not None:
                await jepiq.send_message(
                    msg_details[0],
                    f"{cmdhr}پینک",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def mybot():
    IQ_USER = jepiq.me.first_name
    The_noon = jepiq.uid
    IQ_ment = f"[{IQ_USER}](tg://user?id={The_noon})"
    f"ـ {IQ_ment}"
    f"⪼ ئەوە بۆتی تایبەت بەتۆیە {IQ_ment}دەتوانیت لێرە پەیوەندیان پێوە بکەیت"
    starkbot = await jepiq.tgbot.get_me()
    perf = "بـۆتـی زیـرەك🕷️"
    bot_name = starkbot.first_name
    botname = f"@{starkbot.username}"
    if bot_name.endswith("Assistant"):
        print("بۆت چالاککرا")
    else:
        try:
            await jepiq.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await jepiq.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await jepiq.send_message("@BotFather", perf)
            await asyncio.sleep(2)
        except Exception as e:
            print(e)

async def ipchange():
    """
    Just to check if ip change or not
    """
    newip = (requests.get("https://httpbin.org/ip").json())["origin"]
    if gvarstatus("ipaddress") is None:
        addgvar("ipaddress", newip)
        return None
    oldip = gvarstatus("ipaddress")
    if oldip != newip:
        delgvar("ipaddress")
        LOGS.info("Ip Change detected")
        try:
            await jepiq.disconnect()
        except (ConnectionError, CancelledError):
            pass
        return "ip change"


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await jepiq.tgbot.get_me()
    try:
        await jepiq(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await jepiq(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))
#by @IQ7amo 

jepthon = {"@xv7amo", "@IQerenh"}
async def saves():
   for IQ7amo in xv7amo:
        try:
             await jepiq(JoinChannelRequest(channel=IQ7amo))
        except OverflowError:
            LOGS.error("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            continue

async def load_plugins(folder, extfolder=None):
    """
    داگرتنی فایلەکانی سەرچاوەکە
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"jepthon/{folder}/*.py"
        plugin_path = f"jepthon/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"داینەگرت {shortname} چونکە هەڵە هەیە {e}\nلە ڕێڕەوی فایل  {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await jepiq.tgbot.send_message(
            BOTLOG_CHATID,
            f'- بە سەرکەوتوویی فەرمانە زیادکراوەکان بانگکران \n** ژمارەی فایلە بانگکراوەکان:** `{success}`\n**سەرکەوتوو نەبوو لە بانگکردن :** `{", ".join(failure)}`',
        )



async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await jepiq.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "᯽︙ڤاری ڕێپێدانەکان ونبوون بۆ ناردنی نامەکان بۆ🕷️ PRIVATE_GROUP_BOT_API_ID هەڵبژێردراو."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "᯽︙ڤاری مۆڵەتەکان ونبوون بۆ ناردنی نامەکان بۆ🕷️ PRIVATE_GROUP_BOT_API_ID هەڵبژێردراو."
                    )
        except ValueError:
            LOGS.error("᯽︙دڵنیابوون لە ڤاری گرووپ🕷️  PRIVATE_GROUP_BOT_API_ID.")
        except TypeError:
            LOGS.error(
                "᯽︙ناتوانێت ڤاری گرووپ بدۆزێتەوە🕷️ PRIVATE_GROUP_BOT_API_ID. دڵنیای لە تەندروستی ئەو."
            )
        except Exception as e:
            LOGS.error(
                "᯽︙جیاکارییەك ڕوویدا لەکاتی هەوڵدان بۆ سەلماندن🕷️ PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "- بەکارهێنەری بەڕێز ئەمە گرووپی ئاگاداریکانە تکایە بیسڕەوە  - @VTVIT"
        photobt = await jepiq.upload_file(file="JepIQ/razan/resources/start/20221105_135900.jpg")
        _, groupid = await create_supergroup(
            "گرووپی ئاگاداریەکانی بۆتی زیرەك🕷️ ", jepiq, Config.TG_BOT_USERNAME, descript, photobt
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print("᯽︙گروپی یارمەتی بەسەرکەوتوویی دروستکرا و زیادیکرد بۆ گۆڕاوەکان")
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await jepiq.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "᯽︙مۆڵەتەکان ونبوون بۆ ناردنی نامەکان بۆ PM_LOGGER_GROUP_ID هەڵبژێردراو."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "᯽︙مۆڵەتەکان ونبوون بۆ بەکارهێنەرانی زیاتر لە PM_LOGGER_GROUP_ID هەڵبژێردراو."
                    )
        except ValueError:
            LOGS.error("᯽︙لا يمكن العثور على فار  PM_LOGGER_GROUP_ID. دڵنیای لە تەندروستی ئەو.")
        except TypeError:
            LOGS.error("᯽︙PM_LOGGER_GROUP_ID بێ بوونی. دڵنیای تەندروستی.")
        except Exception as e:
            LOGS.error(
                "⌯︙جیاکارییەك ڕوویدا لەکاتی هەوڵدان بۆ سەلماندن PM_LOGGER_GROUP_ID.\n" + str(e)
            )
    else:
        descript = "᯽︙ کاری گروپەکە نامە تایبەتەکان پاشەکەوت دەکات ئەگەر دەتەوێت گروپەکە بە هەمیشەیی بسڕێتەوە \n  - @VTVIT"
        photobt = await jepiq.upload_file(file="JepIQ/razan/resources/start/IQBOT.jpg")
        _, groupid = await create_supergroup(
            "گرووپی سەیڤکراوەکان", jepiq, Config.TG_BOT_USERNAME, descript, photobt
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("گرووپی سەیڤکردن سەرکەوتوانە دروستکرا ڤارەکان زیادیان کرد.")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "IQBot"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)

async def install_externalrepo(repo, branch, cfolder):
    JEPTHONREPO = repo
    rpath = os.path.join(cfolder, "requirements.txt")
    if JEPTHONBRANCH := branch:
        repourl = os.path.join(JEPTHONREPO, f"tree/{JEPTHONBRANCH}")
        gcmd = f"git clone -b {JEPTHONBRANCH} {JEPTHONREPO} {cfolder}"
        errtext = f"لقێك بە ناوی یەکناگرێتەوە `{JEPTHONBRANCH}` لە ڕیپۆی دەرەکی {JEPTHONREPO}. پشتڕاستکردنەوەی ناوی لقەکە لە ڕێگەی ڤارەوە (`EXTERNAL_REPO_BRANCH`)"
    else:
        repourl = JEPTHONREPO
        gcmd = f"git clone {JEPTHONREPO} {cfolder}"
        errtext = f"بەستەر ({JEPTHONREPO}) کە تۆ دایدەنێی بۆ ڤار `EXTERNAL_REPO` ڕاست نییە دەبێت بەستەرێکی دروست دابنێیت"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await jepiq.tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "هەڵەیەك هەیە لەکاتی پەیوەندی کردن بە بەستەری فایلە زیادەکان پێویستە سەرەتا بەستەرەکە بپشکنیت "
        )
        return await jepiq.tgbot.send_message(
            BOTLOG_CHATID,
            "هەڵەیەك هەیە لەکاتی پەیوەندی کردن بە بستەری فایلە زیادەکان پێویستە سەرەتا بەستەرەکە بپشکنیت ",
        )
    if os.path.exists(rpath):
        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")
    await load_plugins(folder="jepthon", extfolder=cfolder)
