from jepthon import jepiq
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import asyncio
from ..core.managers import edit_delete, edit_or_reply

@jepiq.ar_cmd(pattern="بەشداربوون")
async def reda(event):
    ty = event.text
    ty = ty.replace(".بەشداربوون", "")
    ty = ty.replace(" ", "")
    if len (ty) < 2:
        return await edit_delete(event, "**قم بكتابة نوع الاشتراك الاجباري كروب او خاص**")
    if ty == "گرووپ":
        if not event.is_group:
            return await edit_delete("**استعمل الأمر في الجروب المراد تفعيل الاشتراك الاجباري به**")
        if event.is_group:
            if gvarstatus ("subgroup") == event.chat_id:
                return await edit_delete(event, "**بەشداربوونی ناچاری بۆ ئەم گرووپە چالاککراوە**")
            if gvarstatus("subgroup"):
                return await edit_or_reply(event, "**بەشداربوونی ناچاری بۆ گروپێکی تر چالاك دەکرێت و هەڵدەوەشێنێتەوە بۆ ئەوەی لە گروپێکی تردا چالاك بکرێت**")
            addgvar("subgroup", f"{event.chat_id}")
            return await edit_or_reply(event, "**بەشداربوونی ناچاری بۆ ئەم گروپە چالاککراوە**")
    if ty == "تایبەت":
        if gvarstatus ("subprivate"):
            return await edit_delete(event, "**بەشداربوونی ناچاری بۆ تایبەت چالاك دەکرێت**")
        if not gvarstatus ("subprivate"):
            addgvar ("subprivate", True)
            await edit_or_reply(event, "**بەشداربوونی ناچاری بۆ تایبەت چالاککراوە**")
    if ty not in ["تایبەت", "گرووپ"]:
        return await edit_delete(event, "**جۆری بەشداربوونی ناچاری بۆ گرووپ یان تایبەت بنووسە**")
@jepiq.ar_cmd(pattern="وەستاندن")
async def reda (event):
    cc = event.text.replace(".هەڵوەشاندنەوە", "")
    cc = cc.replace(" ", "")
    if len (cc) < 2:
        return await edit_delete(event, "**جۆری بەشداربوونی ناچاری بنووسە بۆ هەڵوەشاندنەوەی**")
    if cc == "گرووپ":
        if not gvarstatus ("subgroup"):
            return await edit_delete("**بەشداربوونی ناچاریەکەت بۆ گروپەکە چالاك نەکردووە بۆ هەڵوەشاندنەوەی**")
        if gvarstatus ("subgroup"):
            delgvar ("subgroup")
            return await edit_delete(event, "**بەشداری ناچاری بۆ گروپەکە بە سەرکەوتوویی هەڵوەشێنرایەوە**")
    if cc == "تایبەت":
        if not gvarstatus ("subprivate"):
            return await edit_delete(event, "**بەشداربوونی ناچاری تایبەت چالاك نەکراوە بۆ هەڵوەشاندنەوەی **")
        if gvarstatus ("subprivate"):
            delgvar ("subprivate")
            return await edit_delete(event, "**بەشداربوونی ناچاری بۆ تایبەت هەڵوەشێنرایەوە***")
    if cc not in ["تایبەت", "گرووپ"]:
        return await edit_delete(event, "**جۆری بەشداربوونی ناچاری بنووسە بۆ هەڵوەشاندنەوەی**")

@jepiq.ar_cmd(incoming=True)
async def reda(event):
    if gvarstatus ("subprivate"):
        if event.is_private:
            await jepiq.send_message(event.chat_id, "**چیت ئەوێت، گەمژە**")
