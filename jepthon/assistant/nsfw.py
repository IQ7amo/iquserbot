import re

from telethon import Button
from telethon.errors import MessageNotModifiedError
from telethon.events import CallbackQuery

from jepthon import jepiq

from ..Config import Config
from ..core.logger import logging

LOGS = logging.getLogger(__name__)


@jepiq.tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_true")))
async def age_verification_true(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "بە لەبەرچاوگرتنی ئەوەی کە بڕیارێکی گەمژانەیە، من هەڵمبژاردووە پشتگوێی بخەم.",
            alert=True,
        )
    await event.answer("بەڵێ من سەرو 18م", alert=False)
    buttons = [
        Button.inline(
            text="دڵنیانییە،  / گۆڕینی بڕیار ❔",
            data="chg_of_decision_",
        )
    ]
    try:
        await event.edit(
            text="Set `ALLOW_NSFW` = True in Database Vars to access this plugin",
            file="https://telegra.ph/file/85f3071c31279bcc280ef.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@jepiq.tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_false")))
async def age_verification_false(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "بە لەبەرچاوگرتنی ئەوەی کە بڕیارێکی گەمژانەیە، من هەڵمبژاردووە پشتگوێی بخەم",
            alert=True,
        )
    await event.answer("نا من نا", alert=False)
    buttons = [
        Button.inline(
            text="دڵنیانییە، / گۆڕینی بڕیار ❔",
            data="chg_of_decision_",
        )
    ]
    try:
        await event.edit(
            text="دوورکەوە مناڵ🕷️!",
            file="https://telegra.ph/file/1140f16a883d35224e6a1.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@jepiq.tgbot.on(CallbackQuery(data=re.compile(r"^chg_of_decision_")))
async def chg_of_decision_(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "بە لەبەرچاوگرتنی ئەوەی کە بڕیارێکی گەمژانەیە، من هەڵمبژاردووە پشتگوێی بخەم.",
            alert=True,
        )
    await event.answer("دڵنیانییە", alert=False)
    buttons = [
        (
            Button.inline(text="بەڵێ من سەرو 18م", data="age_verification_true"),
            Button.inline(text="نا من نا", data="age_verification_false"),
        )
    ]
    try:
        await event.edit(
            text="**ئایا تۆ ئەوەندە پیریت بۆ ئەمە?**",
            file="https://telegra.ph/file/238f2c55930640e0e8c56.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass
