import asyncio
import random
from telethon import events
from DYNAMIC.utils import admin_cmd
from telethon.tl.types import ChannelParticipantsAdmins
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/7486dce0f715ccc0576b6.jpg"
file2 = "https://telegra.ph/file/cc44dbb6c06fae646da13.jpg"
file3 = "https://telegra.ph/file/4189164cadd30a8a2d6da.jpg"
file4 = "https://telegra.ph/file/1b6d7ec6c2382fb80a094.jpg"
file5 = "https://telegra.ph/file/d57626f8b84037d156d88.jpg"
file6 = "https://telegra.ph/file/5c0bd9eacf8789ab4f4c3.jpg"
file7 = "https://telegra.ph/file/33727f0de96eb4affc714.jpg"
pm_caption = "π₯π₯ **ΓΒ₯β¦Ξ»MΕβ‘ Ι¨Φ ΦΥΌΚΙ¨ΥΌΙ..!! **π₯π₯\n\n"
pm_caption += "βοΈβοΈ **Σ²ΓΕ αΈΎΣ² αΈΎΓΕTΓΕ Γ­ ΓαΈΎ ΕΕ DΕ°TΣ² ΓΕD ΓΔΉΔΉ ΕΣ²ΕTΓαΈΎΕ ΓΕΓ αΊΕΕαΈ°Γ­ΕΗ΄ αΉΓΕFΓΔTΔΉΣ²**βοΈβοΈ\n\n"
pm_caption += "βββοΈοΈΞ»BΓUβΈ MΒ₯ $Β₯$βΈEMβββ\n\n"
pm_caption += "ββΖγTγγEγγLγγEγγTγγHγγOγγNγβγVγγEγγRγγSγγIγγOγγNγββ : 1.19.5\n"
pm_caption += "fββγDγγYγγAγγMγγIγγCγβγUγγSγγEγγRγββ>> : 0.1\n"
pm_caption += "ββγDγγYγγNγγAγγMγγIγγCγβVersionββ : 0.0.1\n"
pm_caption += "ββγSγγUγγPγγPγγOγγRγγTγβγGγγRγγOγγUγγPγββ : [GROUP](https://t.me/DARKLON_USERBOT_SUPPORT\n"
pm_caption += "ββγFγγOγγRγ γUγγPγγDγγAγγTγγEγγSγββ : [CHANNEL](https://t.me/DARKLONXOP\n"
@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file5)
    
    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file6)
    
    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file7)

    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
