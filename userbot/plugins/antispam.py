from telethon.events import ChatAction

from userbot import sclient
from userbot.Config import Var

"""Bans Spammers/Scammer At time Of Arrival 
If You Add Him The Bot Won't Restrict."""


@borg.on(ChatAction)
async def ok(event):
    if Var.ANTISPAM_FEATURE != "ENABLE":
        return
    if event.user_joined:
        juser = await event.get_user()
        user = sclient.is_banned(juser.id)
        if user.banned == True:
            await event.reply(
                f"**#ℓιgнтиιиg-ANTISPAM** \n**Detected Malicious User.** \n**User-ID :** `{juser.id}`  \n**Reason :** `{user.reason}`"
            )
            try:
                await borg.edit_permissions(
                    event.chat_id, juser.id, view_messages=False
                )
            except:
                pass
        else:
            pass
