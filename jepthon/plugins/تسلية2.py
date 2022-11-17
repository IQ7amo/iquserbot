import asyncio
from collections import deque

from . import jepiq, edit_or_reply

plugin_category = "fun"


@jepiq.ar_cmd(
    pattern="بیرکردنەوە$",
    command=("بیرکردنەوە", plugin_category),
    info={
        "فەرمان": "ئەمە بابەتێکی سەرگەرمییە، خۆت تاقی بکەرەوە",
        "بەکارهێنان": "{tr}بیرکردنەوە",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "بیرکردنەوە")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jepiq.ar_cmd(
    pattern="مردم$",
    command=("مردم", plugin_category),
    info={
        "فەرمان": "ئەمە بابەتێکی سەرگەرمییە، خۆت تاقی بکەرەوە",
        "بەکارهێنان": "{tr}مردم",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "مردم")
    deq = deque(list("😹😂🤣😂😹🤣😂"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jepiq.ar_cmd(
    pattern="دڵتەنزێن$",
    command=("دڵتەزێن", plugin_category),
    info={
        "فەرمان": "ئەمە بابەتێکی سەرگەرمییە، خۆت تاقی بکەرەوە",
        "بەکارهێنان": "{tr}دڵتەزێن",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "دڵتەزێن)
    deq = deque(list("😕😞💔🙁☹️💔😕😞💔🙁"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jepiq.ar_cmd(
    pattern="کاتژمێر$",
    command=("کاتژمێر", plugin_category),
    info={
        "فەرمان": "ئەمە بابەتێکی سەرگەرمییە، خۆت تاقی بکەرەوە",
        "بەکارهێنان": "{tr}کاتژمێر",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "کاتژمێر")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jepiq.ar_cmd(
    pattern="مواح$",
    command=("مواح", plugin_category),
    info={
        "فەرمان": "ئەمە بابەتێکی سەرگەرمییە، خۆت تاقی بکرەوە",
        "بەکارهێنان": "{tr}مواح",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "مواح)
    deq = deque(list("😗😻😙😚🥰😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jepiq.ar_cmd(
    pattern="دڵ$",
    command=("دڵ", plugin_category),
    info={
        "الامر": "ئەمە بابەتێکی سەرگەرمییە، خۆت تاقی بکەرەوە",
        "بەکارهێنان": "{tr}دڵ",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "دڵ")
    deq = deque(list("❤️🧡💛💚💙💜🖤❤️‍🩹🤍💗💓"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jepiq.ar_cmd(
    pattern="جیم$",
    command=("جیم", plugin_category),
    info={
        "فەرمان": "ئەمە بابەتێکی سەرگەرمییە، خۆت تاقیکەرەوە",
        "بەکارهێنان": "{tr}جیم",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "جیم")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jepiq.ar_cmd(
    pattern="الارض$",
    command=("الارض", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}الارض",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "الارض")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jepiq.ar_cmd(
    pattern="قمر$",
    command=("قمر", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}قمر",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "مانگ")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jepiq.ar_cmd(
    pattern="اقمار$",
    command=("اقمار", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}اقمار",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "اقمار")
    animation_interval = 0.2
    animation_ttl = range(101)
    await event.edit("اقمار..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@jepiq.ar_cmd(
    pattern="قمور$",
    command=("قمور", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}قمور",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "قمور")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])
