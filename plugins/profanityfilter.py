# ALPHA - UserBot
# Copyright (C) 2021-2022 Cultured_Heaven
#
# This file is a part of < https://github.com/Light-Sensei/AlphaUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Light-Sensei/AlphaUB/blob/main/LICENSE/>.
"""
✘ Commands Available -

•`{i}addprofanity`
   If someone sends bad word in a chat, Then bot will delete that message.

•`{i}remprofanity`
   From chat from Profanity list.

"""

from AlphaOP.dB.nsfw_db import profan_chat, rem_profan

from . import get_string, ALPHA_cmd


@ALPHA_cmd(pattern="addprofanity$", admins_only=True)
async def addp(e):
    profan_chat(e.chat_id, "mute")
    await e.eor(get_string("prof_1"), time=10)


@ALPHA_cmd(pattern="remprofanity", admins_only=True)
async def remp(e):
    rem_profan(e.chat_id)
    await e.eor(get_string("prof_2"), time=10)
