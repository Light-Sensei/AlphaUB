# ALPHA - UserBot
# Copyright (C) 2021-2022 Cultured_Heaven
#
# This file is a part of < https://github.com/Light-Sensei/AlphaUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Light-Sensei/AlphaUB/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ALPHA_cmd

REPOMSG = """
• **ALPHA USERBOT** •\n
• Repo - [Click Here](https://github.com/Light-Sensei/AlphaUB)
• Addons - [Click Here](https://github.com/Light-Sensei/AlphaUBAddons)
• Support - @ALPHASupportChat
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/Light-Sensei/AlphaUB"),
        Button.url("Addons", "https://github.com/Light-Sensei/AlphaUBAddons"),
    ],
    [Button.url("Support Group", "t.me/ALPHASupportChat")],
]

ULTSTRING = """🎇 **Thanks for Deploying ALPHA Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ALPHA_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@ALPHA_cmd(pattern="ALPHA$")
async def useALPHA(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://graph.org/file/54a917cc9dbb94733ea5f.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
