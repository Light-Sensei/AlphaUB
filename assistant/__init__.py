# ALPHA - UserBot
# Copyright (C) 2021-2022 Cultured_Heaven
#
# This file is a part of < https://github.com/Light-Sensei/AlphaUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Light-Sensei/AlphaUB/blob/main/LICENSE/>.

from telethon import Button, custom

from plugins import ATRA_COL, InlinePlugin
from AlphaOP import *
from AlphaOP import _ult_cache
from AlphaOP._misc import owner_and_sudos
from AlphaOP._misc._assistant import asst_cmd, callback, in_pattern
from AlphaOP.fns.helper import *
from AlphaOP.fns.tools import get_stored_file
from strings import get_languages, get_string

OWNER_NAME = ALPHA_bot.full_name
OWNER_ID = ALPHA_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
