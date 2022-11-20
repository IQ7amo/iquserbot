import sys
import jepthon
from jepthon import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import jepiq
from .utils import (
    add_bot_to_logger_group,
    install_externalrepo,
    ipchange,
    load_plugins,
    setup_bot,
    mybot,
    startupmessage,
    verifyLoggerGroup,
    saves,
)

LOGS = logging.getLogger("IQbot")

print(jepthon.__copyright__)
print("Licensed under the terms of the " + jepthon.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("دەست پێکردنی بۆتی زیرەك👾")
    jepiq.loop.run_until_complete(setup_bot())
    LOGS.info("دامەزراندنی بۆت تەواوبوو👾✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

try:
    LOGS.info("دۆخی سەرهێڵ چالاککراوە.")
    jepiq.loop.run_until_complete(mybot())
    LOGS.info("بە سەرکەوتوویی دۆخی سەرهێڵ کاردەکات✓")
except Exception as jep:
    LOGS.error(f"- {jep}")
    sys.exit()    


class CatCheck:
    def __init__(self):
        self.sucess = True


Catcheck = CatCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        Catcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("᯽︙بـۆتـی زیـرەك بە سـەرکەوتـوویی کاردەکات 🕷️ ")
    print(
        f"چالاککردنی ئینلانی خودکار {cmdhr}فەرمانەکان بۆ بینینی فەرمانەکانی سەرچاوەکە\
        \nبۆ یارمەتی  https://t.me/VTVIT"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await saves()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return

async def externalrepo():
    if Config.VCMODE:
        await install_externalrepo("https://github.com/jepthoniq/JepVc", "jepvc", "jepthonvc")

jepiq.loop.run_until_complete(externalrepo())
jepiq.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    jepiq.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        jepiq.run_until_disconnected()
    except ConnectionError:
        pass
